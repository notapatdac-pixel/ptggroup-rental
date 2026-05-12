import reflex as rx
from component.myapplicationspage.myApplicationsPage import my_applications_page_content


def my_applications_page() -> rx.Component:
    return rx.box(my_applications_page_content())
