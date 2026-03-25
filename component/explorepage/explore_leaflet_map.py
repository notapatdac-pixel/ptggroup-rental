import json

import reflex as rx

from component.explorepage.stations_catalog import markers_for_leaflet


def explore_leaflet_map() -> rx.Component:
    markers_json = json.dumps(markers_for_leaflet())

    # HTML for a small “card-like” tooltip (matching the right panel summary).
    # Note: we inline styles because global Tailwind classes won't apply inside Leaflet tooltip reliably.
    js = f"""
    (() => {{
      const markers = {markers_json};

      const stationTooltipHtml = (m) => {{
        return `
          <div style="width: 240px;">
            <div style="display:flex; gap:10px; align-items:flex-start;">
              <img src="${{m.image}}" alt="${{m.title}}" style="width:64px; height:48px; object-fit:cover; border-radius:10px;" />
              <div style="flex:1; min-width:0;">
                <div style="font-weight:800; font-family: inherit; font-size:13px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                  ${{m.title}}
                </div>
                <div style="font-size:12px; opacity:0.8; margin-top:2px;">
                  ${{m.location}}
                </div>
                <div style="display:flex; gap:6px; margin-top:8px; flex-wrap:wrap;">
                  <span style="background: rgba(70,104,0,0.15); color:#466800; padding:2px 8px; border-radius:999px; font-weight:700; font-size:10px;">
                    ${{m.traffic_badge}}
                  </span>
                  <span style="background:#466800; color:#fff; padding:2px 8px; border-radius:999px; font-weight:800; font-size:10px;">
                    ${{m.match_badge}}
                  </span>
                </div>
              </div>
            </div>
          </div>
        `;
      }};

      const destinationIcon = (fill) => {{
        // Simple “destination” pin via inline SVG for a Google Maps-like look.
        return L.divIcon({{
          className: '',
          iconSize: [30, 42],
          iconAnchor: [15, 42],
          popupAnchor: [0, -42],
          html: `
            <div style="width:30px; height:42px; position:relative;">
              <svg width="30" height="42" viewBox="0 0 30 42" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 0C9.05 0 4.25 4.8 4.25 10.75C4.25 20.5 15 42 15 42C15 42 25.75 20.5 25.75 10.75C25.75 4.8 20.95 0 15 0Z" fill="${{fill}}" />
                <circle cx="15" cy="12" r="5" fill="#FFFFFF" opacity="0.95"/>
              </svg>
            </div>
          `
        }});
      }};

      const init = () => {{
        const el = document.getElementById("ptg-explore-leaflet-map");
        if (!el) return false;
        if (!window.L) return false;
        // When navigating in SPA mode, the map container can be re-rendered.
        // If we already initialized Leaflet for a previous DOM node, re-bind to the new one.
        if (
          window.__ptgExploreMap &&
          window.__ptgExploreMap.getContainer &&
          window.__ptgExploreMap.getContainer() === el
        ) {{
          try {{ window.__ptgExploreMap.invalidateSize(); }} catch (e) {{}}
          return true;
        }}

        if (window.__ptgExploreMap && window.__ptgExploreMap.remove) {{
          try {{ window.__ptgExploreMap.remove(); }} catch (e) {{}}
        }}
        window.__ptgExploreMap = null;
        window.__ptgExploreMapInited = false;

        // Leaflet can throw if the container was previously initialized.
        try {{
          if (el._leaflet_id) delete el._leaflet_id;
        }} catch (e) {{
          el._leaflet_id = undefined;
        }}

        const map = L.map(el, {{ zoomControl: false }}).setView([13.7563, 100.5018], 10);
        window.__ptgExploreMap = map;
        window.__ptgExploreMapInited = true;

        L.tileLayer("https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png", {{
          maxZoom: 19,
          attribution: "© OpenStreetMap contributors"
        }}).addTo(map);

        const icon = destinationIcon("#466800");
        const userIcon = destinationIcon("#ef4444");
        const stationMarkers = [];

        markers.forEach((m, idx) => {{
          const marker = L.marker([m.lat, m.lng], {{ icon }}).addTo(map);
          stationMarkers.push({{ marker, data: m }});

          const html = stationTooltipHtml(m);
          marker.bindTooltip(html, {{
            direction: 'top',
            offset: [0, -24],
            opacity: 1,
            sticky: true,
            className: 'ptg-leaflet-tooltip'
          }});
          marker.on('mouseover', () => marker.openTooltip());
          marker.on('mouseout', () => marker.closeTooltip());

          marker.on('click', () => {{
            window.location.href = '/stationdetailpage/' + encodeURIComponent(m.id);
          }});
        }});

        let userPin = null;

        const zoomInBtn = document.getElementById("ptg-explore-zoom-in-btn");
        const zoomOutBtn = document.getElementById("ptg-explore-zoom-out-btn");
        const locBtn = document.getElementById("ptg-explore-loc-btn");

        if (zoomInBtn) {{
          zoomInBtn.addEventListener("click", () => map.zoomIn());
        }}
        if (zoomOutBtn) {{
          zoomOutBtn.addEventListener("click", () => map.zoomOut());
        }}

        if (locBtn) {{
          locBtn.addEventListener('click', () => {{
            if (!navigator.geolocation) return;
            navigator.geolocation.getCurrentPosition((pos) => {{
              const latlng = {{ lat: pos.coords.latitude, lng: pos.coords.longitude }};
              map.setView([latlng.lat, latlng.lng], 13);

              // Replace the previous user pin (red).
              if (userPin) {{
                map.removeLayer(userPin);
              }}
              userPin = L.marker([latlng.lat, latlng.lng], {{ icon: userIcon }}).addTo(map);
              userPin.bindTooltip("Your location", {{
                direction: "top",
                offset: [0, -24],
                sticky: true,
              }}).openTooltip();
            }});
          }});
        }}

        // After route changes/layout, ensure Leaflet recalculates dimensions.
        setTimeout(() => {{
          try {{ map.invalidateSize(); }} catch (e) {{}}
        }}, 120);
        setTimeout(() => {{
          try {{ map.invalidateSize(); }} catch (e) {{}}
        }}, 420);

        // Filtering: hide/show station cards and map markers together.
        const provinceSelect = document.getElementById("ptg-explore-filter-province");
        const trafficSelect = document.getElementById("ptg-explore-filter-traffic");
        const spacesSelect = document.getElementById("ptg-explore-filter-spaces");
        const searchInput = document.getElementById("ptg-explore-search-input");

        const provinceValues = Array.from(new Set(markers.map((m) => m.province).filter(Boolean)));
        const provinceValuesLower = provinceValues.map((p) => p.toLowerCase());

        const applyFilters = () => {{
          const provinceVal = provinceSelect?.value ?? "all";
          const trafficVal = trafficSelect?.value ?? "all";
          const spacesVal = spacesSelect?.value ?? "all";

          const minSpaces = spacesVal === "all" ? null : parseInt(spacesVal, 10);
          const searchVal = (searchInput?.value ?? "").trim().toLowerCase();
          const provinceOnlyMatch = !!searchVal && provinceValuesLower.includes(searchVal);

          // Update map markers.
          stationMarkers.forEach((item) => {{
            const m = item.data;
            const okProvince = provinceVal === "all" || m.province === provinceVal;
            const okTraffic = trafficVal === "all" || m.traffic_level === trafficVal;
            const okSpaces = minSpaces === null || m.spaces_count >= minSpaces;
            const okSearch = !searchVal
              ? true
              : provinceOnlyMatch
                ? (m.province || "").toLowerCase() === searchVal
                : (`${{m.title || ""}} ${{m.province || ""}} ${{m.location || ""}}`).toLowerCase().includes(searchVal);

            const match = okProvince && okTraffic && okSpaces && okSearch;

            if (match) {{
              item.marker.addTo(map);
            }} else {{
              map.removeLayer(item.marker);
              item.marker.closeTooltip?.();
            }}
          }});

          // Update right-side station list.
          const cards = document.querySelectorAll('[id^="ptg-station-card-"]');
          cards.forEach((card) => {{
            const cardProvince = card.getAttribute("data-province") ?? "";
            const cardTraffic = card.getAttribute("data-traffic") ?? "";
            const cardSpacesStr = card.getAttribute("data-spaces") ?? "0";
            const cardSpaces = parseInt(cardSpacesStr, 10);

            const okProvince = provinceVal === "all" || cardProvince === provinceVal;
            const okTraffic = trafficVal === "all" || cardTraffic === trafficVal;
            const okSpaces = minSpaces === null || cardSpaces >= minSpaces;
            const cardText = (card.textContent ?? "").toLowerCase();
            const cardProvinceLower = (cardProvince || "").toLowerCase();
            const okSearch = !searchVal
              ? true
              : provinceOnlyMatch
                ? cardProvinceLower === searchVal
                : cardText.includes(searchVal);

            const match = okProvince && okTraffic && okSpaces && okSearch;

            card.style.display = match ? "" : "none";
          }});
        }};

        if (provinceSelect) provinceSelect.addEventListener("change", applyFilters);
        if (trafficSelect) trafficSelect.addEventListener("change", applyFilters);
        if (spacesSelect) spacesSelect.addEventListener("change", applyFilters);
        if (searchInput) searchInput.addEventListener("input", applyFilters);
        applyFilters();
        // Ensure the station cards are in the DOM before the first pass.
        setTimeout(applyFilters, 250);

        try {{
          map.invalidateSize();
        }} catch (e) {{}}

        return true;
      }};

      const tries = 25;
      let i = 0;
      const tick = () => {{
        const ok = init();
        if (ok) return;
        i += 1;
        if (i < tries) setTimeout(tick, 150);
      }};
      tick();
    }})();
    """

    return rx.el.section(
        rx.el.div(
            rx.el.div(id="ptg-explore-leaflet-map", class_name="absolute inset-0 w-full h-full z-0"),
            rx.el.div(class_name="absolute inset-0 pointer-events-none map-gradient-overlay z-[1]"),
            class_name="relative w-full h-full",
        ),
        rx.script(src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js", defer=True),
        rx.script(js, defer=True),
        class_name="absolute inset-0 z-0",
    )

