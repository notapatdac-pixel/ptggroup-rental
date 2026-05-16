import reflex as rx
from component.landlord_backoffice.landlordOverviewPage import landlord_overview_page_content


def landlord_overview_page() -> rx.Component:
    return rx.box(landlord_overview_page_content())
