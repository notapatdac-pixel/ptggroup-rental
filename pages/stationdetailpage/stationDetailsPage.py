import reflex as rx

from component.stationdetailpage.stationDetailsPage import station_detail_page_component


def station_detail_page() -> rx.Component:
    return rx.box(station_detail_page_component())
