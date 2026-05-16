import reflex as rx
from component.landlord_backoffice.landlordTenantsPage import landlord_tenants_page_content


def landlord_tenants_page() -> rx.Component:
    return rx.box(landlord_tenants_page_content())
