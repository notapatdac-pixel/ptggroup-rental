import reflex as rx
from component.landlord_backoffice.landlordRevenuePage import landlord_revenue_page_content


def landlord_revenue_page() -> rx.Component:
    return rx.box(landlord_revenue_page_content())
