import reflex as rx
from component.landlord_backoffice.landlordApplicationsPage import landlord_applications_page_content


def landlord_applications_page() -> rx.Component:
    return rx.box(landlord_applications_page_content())
