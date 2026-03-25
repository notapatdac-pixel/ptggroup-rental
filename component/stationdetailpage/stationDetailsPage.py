import reflex as rx

from component.explorepage.stations_catalog import STATIONS_BY_ID
from component.landingpage.footer import footer
from component.landingpage.nav_bar import nav_bar
from component.stationdetailpage.station_detail_block import station_detail_content


def _station_page_shell(station: dict, content: rx.Component) -> rx.Component:
    """Full-width station photo at low opacity over surface, content above."""
    img = station["image"]
    return rx.box(
        rx.el.div(class_name="absolute inset-0 z-0 bg-surface"),
        rx.el.div(
            class_name=(
                "absolute inset-0 z-[1] bg-cover bg-center bg-no-repeat opacity-[0.11] "
                "pointer-events-none"
            ),
            style={"backgroundImage": f"url('{img}')"},
        ),
        rx.box(
            content,
            class_name="relative z-10 max-w-[1200px] mx-auto w-full px-6 py-8 pt-28 pb-28",
        ),
        class_name="relative flex-1 min-h-screen w-full",
    )


def station_detail_page_component() -> rx.Component:
    default_station = STATIONS_BY_ID["latphrao71"]
    return rx.box(
        nav_bar(),
        rx.el.main(
            rx.match(
                rx.State.station_id,
                ("latphrao71", _station_page_shell(STATIONS_BY_ID["latphrao71"], station_detail_content(STATIONS_BY_ID["latphrao71"]))),
                ("ramaix", _station_page_shell(STATIONS_BY_ID["ramaix"], station_detail_content(STATIONS_BY_ID["ramaix"]))),
                ("bangna", _station_page_shell(STATIONS_BY_ID["bangna"], station_detail_content(STATIONS_BY_ID["bangna"]))),
                _station_page_shell(default_station, station_detail_content(default_station)),
            ),
            class_name="flex-1 bg-surface text-on-surface font-body min-h-screen relative",
        ),
        footer(),
        class_name="bg-surface text-on-surface antialiased",
    )
