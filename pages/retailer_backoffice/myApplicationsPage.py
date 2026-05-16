import reflex as rx
from component.retailer_backoffice.myApplicationsPage import my_applications_page_content


def my_applications_page() -> rx.Component:
    return rx.box(my_applications_page_content())

