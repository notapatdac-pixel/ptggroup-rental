import reflex as rx
from component.landlord_backoffice.landlord_layout import landlord_layout


def _summary_kpi(label: str, value: str, icon: str, sub: str, accent: bool = False) -> rx.Component:
    if accent:
        return rx.box(
            rx.text(label, class_name="text-[10px] font-bold tracking-widest uppercase text-white/70 mb-1"),
            rx.text(value, class_name="text-4xl font-bold text-white leading-tight"),
            rx.text(sub, class_name="text-xs text-white/80 italic mt-1"),
            class_name="backoffice-accent-card flex-1",
        )
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text(label, class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1"),
                rx.text(value, class_name="text-4xl font-bold text-on-surface leading-tight"),
                rx.text(sub, class_name="text-xs text-backoffice-primary font-bold mt-1"),
                class_name="flex-1",
            ),
            rx.el.span(icon, class_name="material-symbols-outlined text-[36px] text-outline-variant/50"),
            class_name="flex items-start justify-between gap-2",
        ),
        class_name="backoffice-kpi-card flex-1",
    )


def _occupancy_kpi() -> rx.Component:
    return rx.box(
        rx.text("AVG. OCCUPANCY", class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1"),
        rx.text("89%", class_name="text-4xl font-bold text-on-surface leading-tight mb-3"),
        rx.box(
            rx.box(class_name="backoffice-progress-fill h-full", style={"width": "89%"}),
            class_name="backoffice-progress-track",
        ),
        class_name="backoffice-kpi-card flex-1",
    )


def _metric_pill(label: str, value: str) -> rx.Component:
    return rx.box(
        rx.text(label, class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant"),
        rx.text(value, class_name="text-sm font-bold text-on-surface"),
        class_name="bg-surface-container-low rounded-lg px-3 py-2",
    )


def _station_card(
    name: str, location: str, photo: str,
    occupied: int, total: int,
    revenue: str, performance: str, renewal: str,
) -> rx.Component:
    return rx.box(
        rx.box(
            rx.image(src=photo, class_name="w-full h-48 object-cover"),
            class_name="rounded-t-2xl overflow-hidden",
        ),
        rx.box(
            rx.hstack(
                rx.box(
                    rx.text(name, class_name="text-xl font-bold text-on-surface"),
                    rx.hstack(
                        rx.el.span("location_on", class_name="material-symbols-outlined text-[14px] text-on-surface-variant"),
                        rx.text(location, class_name="text-xs text-on-surface-variant"),
                        class_name="flex items-center gap-0.5 mt-0.5",
                    ),
                    class_name="flex-1",
                ),
                rx.box(
                    rx.text("OCCUPANCY", class_name="text-[9px] font-bold tracking-widest text-on-surface-variant text-right"),
                    rx.hstack(
                        rx.text(str(occupied), class_name="text-2xl font-bold text-on-surface"),
                        rx.text(f"/ {total} units", class_name="text-sm text-on-surface-variant self-end pb-0.5"),
                        class_name="flex items-baseline gap-1",
                    ),
                    class_name="text-right",
                ),
                class_name="flex items-start justify-between mb-4",
            ),
            rx.hstack(
                _metric_pill("Revenue", revenue),
                _metric_pill("Performance", performance),
                _metric_pill("Renewals", renewal),
                class_name="flex gap-2 mb-4",
            ),
            rx.el.button(
                "Edit Details",
                class_name=(
                    "w-full bg-surface-container-low border border-outline-variant/40 "
                    "rounded-full px-4 py-2.5 text-sm font-bold text-on-surface cursor-pointer "
                    "hover:bg-surface-container transition-colors"
                ),
            ),
            class_name="p-5",
        ),
        class_name="bg-white rounded-2xl shadow-sm overflow-hidden",
    )


def landlord_my_stations_page_content() -> rx.Component:
    return landlord_layout(
        "stations",
        rx.box(
            rx.hstack(
                rx.heading("Stations Performance", as_="h1",
                           class_name="text-2xl font-bold text-on-surface"),
                rx.el.button(
                    rx.hstack(
                        rx.el.span("add_circle", class_name="material-symbols-outlined text-[18px]"),
                        rx.text("Add New Station", class_name="text-sm font-bold"),
                        class_name="flex items-center gap-1.5",
                    ),
                    class_name="backoffice-btn-primary border-0 rounded-full px-5 py-2.5 cursor-pointer",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.grid(
                _summary_kpi("Active Stations", "12", "ev_station", "+2 this quarter"),
                _occupancy_kpi(),
                _summary_kpi("Monthly Net Yield", "฿4.2M", "", "Surpassing forecast by 12.4%", accent=True),
                columns="3",
                class_name="gap-4 mb-8",
            ),
            rx.grid(
                _station_card(
                    "PTG Lat Phrao 71", "Lat Phrao Road, Bangkok",
                    "/image/station-ptg-latphrao71.png",
                    4, 5, "498K THB/MO", "+12%", "Oct '24",
                ),
                _station_card(
                    "PTG Sukhumvit 62", "Sukhumvit Road, Bangkok",
                    "/image/station-ptg-ramaix.png",
                    8, 8, "318K THB/MO", "+27%", "Jan '25",
                ),
                columns="2",
                class_name="gap-6",
            ),
        ),
    )
