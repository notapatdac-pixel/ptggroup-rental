import reflex as rx
from component.retailer_backoffice.exploreLocationPage import explore_location_page_content


def explore_location_page() -> rx.Component:
    return rx.box(explore_location_page_content())

