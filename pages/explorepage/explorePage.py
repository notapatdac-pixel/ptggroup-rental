import reflex as rx

from component.explorepage.explorePage import explore_page_component


def explore_page() -> rx.Component:
    return rx.box(explore_page_component())

