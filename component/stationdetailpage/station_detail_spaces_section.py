import reflex as rx

from component.stationdetailpage.station_detail_space_card import space_card


def station_spaces_section(station: dict) -> rx.Component:
    d = station["detail"]
    return rx.el.div(
        rx.el.div(
            rx.el.h4("Available Spaces", class_name="font-headline text-2xl text-on-surface"),
            rx.link(
                "View Store Map",
                href="#",
                class_name=(
                    "text-primary text-sm font-bold border-b border-primary/20 hover:border-primary cursor-pointer"
                ),
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            *[
                space_card(sp["unit"], sp["name"], sp["price"], sp["desc"], sp["img"])
                for sp in d["spaces"]
            ],
            class_name="grid grid-cols-1 md:grid-cols-3 gap-6",
        ),
        class_name="",
    )
