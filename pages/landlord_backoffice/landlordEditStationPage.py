import reflex as rx
from component.landlord_backoffice.landlordEditStationPage import landlord_edit_station_page_content


def landlord_edit_station_page() -> rx.Component:
    return rx.box(landlord_edit_station_page_content())
