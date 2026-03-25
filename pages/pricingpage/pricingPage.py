import reflex as rx

from component.pricingpage.pricingPage import pricing_page_component


def pricing_page() -> rx.Component:
    return rx.box(pricing_page_component())

