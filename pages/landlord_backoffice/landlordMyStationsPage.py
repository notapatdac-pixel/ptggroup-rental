import reflex as rx
from component.landlord_backoffice.landlordMyStationsPage import landlord_my_stations_page_content


def landlord_my_stations_page() -> rx.Component:
    return rx.box(landlord_my_stations_page_content())
