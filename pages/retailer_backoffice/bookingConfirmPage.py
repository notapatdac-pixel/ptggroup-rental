import reflex as rx
from component.retailer_backoffice.bookingConfirmPage import booking_confirm_page_content


def booking_confirm_page() -> rx.Component:
    return rx.box(booking_confirm_page_content())

