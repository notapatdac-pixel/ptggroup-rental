import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout


def _bar(height: str, active: bool = False) -> rx.Component:
    return rx.box(
        class_name=f"{'backoffice-bar' if active else 'backoffice-bar-muted'} w-7",
        style={"height": height},
    )


def _space_card(badge: str, title: str, price: str, sub: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.span("storefront", class_name="material-symbols-outlined text-on-surface-variant/30 text-4xl"),
            rx.box(rx.text(badge, class_name="text-[10px] font-bold text-white"), class_name="absolute top-2 left-2 bg-backoffice-primary rounded-full px-2 py-0.5"),
            class_name="w-full h-28 bg-surface-container rounded-xl flex items-center justify-center relative mb-3",
        ),
        rx.text(title, class_name="text-sm font-bold text-on-surface mb-0.5"),
        rx.text(price, class_name="text-base font-bold text-backoffice-primary"),
        rx.text(sub, class_name="text-xs text-on-surface-variant"),
        class_name="bg-white rounded-2xl p-4 shadow-sm",
    )


def explore_location_page_content() -> rx.Component:
    return backoffice_layout(
        "dashboard",
        rx.box(
            rx.hstack(
                rx.hstack(
                    rx.link("Explore", href="/explorepage", class_name="text-xs text-on-surface-variant no-underline hover:text-on-surface"),
                    rx.el.span("chevron_right", class_name="material-symbols-outlined text-sm text-on-surface-variant"),
                    rx.text("PTG Station Lat Phrao 71", class_name="text-xs text-on-surface-variant"),
                    class_name="flex items-center gap-1",
                ),
                rx.hstack(
                    rx.box(rx.text("RANKING STATION", class_name="text-[9px] font-bold text-backoffice-primary"), class_name="backoffice-chip-reviewing"),
                    rx.box(rx.text("High Traffic Area", class_name="text-[9px] font-bold text-on-surface-variant"), class_name="bg-surface-container-low rounded-full px-3 py-1"),
                    class_name="flex items-center gap-2",
                ),
                class_name="flex justify-between items-center mb-4",
            ),
            rx.hstack(
                rx.box(
                    rx.heading("PTG Station Lat Phrao 71", as_="h1", class_name="text-2xl font-bold text-on-surface mb-1"),
                    rx.hstack(
                        rx.el.span("location_on", class_name="material-symbols-outlined text-on-surface-variant text-sm"),
                        rx.text("Lat Phrao Road, Bangkok 10310", class_name="text-xs text-on-surface-variant"),
                        class_name="flex items-center gap-1 mb-4",
                    ),
                    rx.grid(
                        rx.box(
                            rx.text("DAILY CUSTOMERS", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                            rx.text("12,450+", class_name="text-xl font-bold text-on-surface"),
                            rx.text("↑ 4% vs last month", class_name="text-[10px] text-backoffice-primary"),
                        ),
                        rx.box(
                            rx.text("AVG. DWELL TIME", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                            rx.text("18.5 min", class_name="text-xl font-bold text-on-surface"),
                            rx.text("Samurai retail link", class_name="text-[10px] text-on-surface-variant"),
                        ),
                        rx.box(
                            rx.text("EST. REVENUE", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                            rx.text("฿285k THB", class_name="text-xl font-bold text-on-surface"),
                            rx.text("↑ 5.4% in region", class_name="text-[10px] text-backoffice-primary"),
                        ),
                        columns="3",
                        class_name="gap-3 mb-5",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.text("Traffic Trend", class_name="text-sm font-bold text-on-surface"),
                            rx.box(rx.text("4G.42% At Seasonal Market", class_name="text-[9px] font-bold text-backoffice-primary"), class_name="backoffice-chip-reviewing"),
                            class_name="flex items-center gap-2 mb-1",
                        ),
                        rx.text("Hourly customer density (Mon-Sun)", class_name="text-xs text-on-surface-variant mb-3"),
                        rx.hstack(
                            _bar("30px"), _bar("45px"), _bar("60px", True), _bar("80px", True),
                            _bar("70px", True), _bar("55px"), _bar("40px"),
                            class_name="flex items-end gap-1 h-20",
                        ),
                        class_name="mb-0",
                    ),
                ),
                rx.box(
                    rx.text("AI-Driven Insights Unlocked", class_name="text-xs font-bold text-white mb-2"),
                    rx.hstack(
                        rx.box(
                            rx.el.svg(
                                rx.el.circle(cx="30", cy="30", r="24", class_name="backoffice-donut-track", stroke_width="6"),
                                rx.el.circle(
                                    cx="30", cy="30", r="24", class_name="backoffice-donut-fill",
                                    stroke_width="6",
                                    stroke_dasharray="129 151",
                                    stroke_dashoffset="38",
                                    transform="rotate(-90 30 30)",
                                    stroke="#bef464",
                                ),
                                rx.el.text("87%", x="30", y="34", text_anchor="middle", font_size="10", font_weight="700", fill="white"),
                                width="60", height="60", view_box="0 0 60 60",
                            ),
                        ),
                        rx.text("87%", class_name="text-4xl font-bold text-white"),
                        class_name="flex items-center gap-3 mb-3",
                    ),
                    rx.text("$1.2M - 1.65M+", class_name="text-sm font-bold text-white/80 mb-3"),
                    rx.link(
                        rx.el.button("View Full AI Report", class_name="bg-white text-backoffice-primary text-xs font-bold px-4 py-2 rounded-lg border-0 cursor-pointer w-full"),
                        href="#",
                        class_name="no-underline",
                    ),
                    class_name="backoffice-accent-card w-52 flex-shrink-0",
                ),
                rx.hstack(
                    rx.el.button("Save", class_name="bg-white border border-outline-variant/40 rounded-full px-5 py-2 cursor-pointer text-sm font-bold text-on-surface"),
                    rx.link(
                        rx.el.button("Apply", class_name="backoffice-btn-primary rounded-full px-5 py-2 border-0 cursor-pointer text-sm font-bold"),
                        href="/retailerslotselection",
                        class_name="no-underline",
                    ),
                    class_name="flex items-center gap-2 flex-shrink-0",
                ),
                class_name="flex items-start gap-6 bg-white rounded-2xl p-6 shadow-sm mb-6",
            ),
            rx.hstack(
                rx.text("Available Spaces", class_name="text-base font-bold text-on-surface"),
                rx.box(rx.text("3 Units Left", class_name="text-xs font-bold text-backoffice-primary"), class_name="backoffice-chip-reviewing"),
                class_name="flex items-center gap-3 mb-4",
            ),
            rx.grid(
                _space_card("UNIT A", "Corner Premium Site", "฿36,500", "43 sqm • Prime visibility"),
                _space_card("UNIT B", "Mid-Zone Retail", "฿18,000", "28 sqm • Strategic utility"),
                _space_card("UNIT C", "Compact Kiosk Space", "฿8,500", "12 sqm • Strategic utility"),
                columns="3",
                class_name="gap-4 mb-6",
            ),
            rx.grid(
                rx.box(
                    rx.text("Location Specification", class_name="text-base font-bold text-on-surface mb-4"),
                    rx.vstack(
                        *[
                            rx.hstack(
                                rx.text(k, class_name="text-xs text-on-surface-variant flex-1"),
                                rx.text(v, class_name="text-xs font-bold text-on-surface"),
                                class_name="flex items-center py-2 border-b border-outline-variant/20",
                            )
                            for k, v in [
                                ("Station Type", "Platinum Hub"),
                                ("Total Area", "1,200 sqm"),
                                ("EV Charging Points", "6 Units (DC Fast)"),
                                ("Nearby Transit", "MRT Yellow Line (1.2km)"),
                                ("Operational Status", "Full Capacity"),
                            ]
                        ],
                        class_name="gap-0 w-full",
                    ),
                    class_name="bg-white rounded-2xl p-6 shadow-sm",
                ),
                rx.box(
                    rx.box(
                        rx.el.span("map", class_name="material-symbols-outlined text-on-surface-variant/30 text-5xl"),
                        rx.box(
                            rx.el.span("location_on", class_name="material-symbols-outlined text-backoffice-primary text-xl"),
                        ),
                        class_name="w-full h-48 bg-surface-container rounded-xl flex items-center justify-center relative",
                    ),
                    rx.box(
                        rx.text("5km Radius • 240k Residents", class_name="text-xs font-bold text-on-surface"),
                        class_name="absolute bottom-4 right-4 bg-white rounded-lg px-3 py-2 shadow-sm",
                    ),
                    class_name="bg-white rounded-2xl p-4 shadow-sm relative",
                ),
                columns="2",
                class_name="gap-6",
                style={"grid-template-columns": "1.2fr 1fr"},
            ),
        ),
    )

