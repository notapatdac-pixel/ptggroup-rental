import reflex as rx

from component.landingpage.landingPage import landing_page_component


def landing_page() -> rx.Component:
    return rx.box(landing_page_component())
