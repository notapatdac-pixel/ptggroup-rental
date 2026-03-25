import reflex as rx

from component.explorepage.explore_leaflet_map import explore_leaflet_map
from component.explorepage.explore_nav_bar import explore_nav_bar
from component.explorepage.explore_station_list import explore_station_list


def explore_page_component() -> rx.Component:
    return rx.box(
        explore_nav_bar(),
        rx.el.main(
            rx.el.section(
                explore_leaflet_map(),
                rx.el.div(
                    rx.el.button(
                        rx.el.span("add", class_name="material-symbols-outlined"),
                        type="button",
                        class_name="bg-white p-3 rounded-xl shadow-xl hover:bg-surface-container-low transition-colors text-on-surface-variant cursor-pointer",
                        id="ptg-explore-zoom-in-btn",
                        title="Zoom in",
                    ),
                    rx.el.button(
                        rx.el.span("remove", class_name="material-symbols-outlined"),
                        type="button",
                        class_name="bg-white p-3 rounded-xl shadow-xl hover:bg-surface-container-low transition-colors text-on-surface-variant cursor-pointer",
                        id="ptg-explore-zoom-out-btn",
                        title="Zoom out",
                    ),
                    rx.el.button(
                        rx.el.span("my_location", class_name="material-symbols-outlined text-primary"),
                        type="button",
                        class_name="bg-white p-3 rounded-xl shadow-xl hover:bg-surface-container-low transition-colors text-primary cursor-pointer",
                        id="ptg-explore-loc-btn",
                        title="My location",
                    ),
                    class_name="absolute bottom-8 left-8 flex flex-col gap-2 z-10",
                ),
                class_name="flex-1 relative bg-surface-container-high overflow-hidden",
            ),
            explore_station_list(),
            class_name="flex h-screen pt-20",
        ),
        rx.el.div(
            rx.el.button(
                rx.el.span("analytics", class_name="material-symbols-outlined fill-icon"),
                rx.el.span("Open Market Insights", class_name="text-sm font-bold tracking-tight"),
                type="button",
                class_name="pointer-events-auto bg-on-surface text-white px-6 py-4 rounded-full shadow-2xl flex items-center gap-3 transform transition-transform hover:scale-105 active:scale-95",
            ),
            class_name="fixed bottom-8 right-[500px] z-10 pointer-events-none",
        ),
        class_name="bg-surface text-on-surface antialiased overflow-hidden",
    )

