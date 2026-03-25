import reflex as rx

from component.stationdetailpage.station_detail_styles import BTN_LANDING_GHOST, BTN_LANDING_PRIMARY


def station_detail_header(station: dict) -> rx.Component:
    traffic_short = station["traffic_badge_short"]
    return rx.el.div(
        rx.el.nav(
            rx.link(
                "Explore",
                href="/explorepage",
                class_name="text-on-surface-variant text-sm hover:text-primary cursor-pointer",
            ),
            rx.el.span("/", class_name="text-outline-variant"),
            rx.el.span(station["title"], class_name="text-on-surface text-sm font-medium"),
            class_name="flex items-center gap-2 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    station["title"],
                    class_name="font-headline text-4xl md:text-5xl text-on-surface mb-2 tracking-tight",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span("location_on", class_name="material-symbols-outlined text-sm"),
                        rx.el.span(station["region_line"], class_name="text-base"),
                        class_name="flex items-center gap-1.5",
                    ),
                    rx.el.div(
                        rx.el.span(
                            rx.el.span(
                                "trending_up",
                                class_name="material-symbols-outlined text-sm text-primary",
                            ),
                            f" Traffic: {traffic_short}",
                            class_name=(
                                "bg-surface-container-high px-3 py-1 rounded-full text-xs font-bold uppercase "
                                "tracking-wider text-on-surface flex items-center gap-1"
                            ),
                        ),
                        rx.el.span(
                            rx.el.span("verified", class_name="material-symbols-outlined text-sm"),
                            " PTG Verified",
                            class_name=(
                                "bg-primary-container/20 px-3 py-1 rounded-full text-xs font-bold uppercase "
                                "tracking-wider text-primary flex items-center gap-1"
                            ),
                        ),
                        class_name="flex gap-2 flex-wrap",
                    ),
                    class_name="flex flex-col sm:flex-row sm:items-center gap-4 text-on-surface-variant",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.button("Save", type="button", class_name=BTN_LANDING_GHOST),
                rx.el.button("Sign in to Apply", type="button", class_name=BTN_LANDING_PRIMARY),
                class_name="flex gap-3 flex-shrink-0 flex-wrap",
            ),
            class_name="flex flex-col md:flex-row justify-between items-start gap-6 mb-10",
        ),
    )
