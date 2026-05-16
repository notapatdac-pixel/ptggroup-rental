import reflex as rx
from component.retailer_backoffice.performancePage import performance_page_content


def performance_page() -> rx.Component:
    return rx.box(performance_page_content())

