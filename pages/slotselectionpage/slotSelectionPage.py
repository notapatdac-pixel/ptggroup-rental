import reflex as rx
from component.slotselectionpage.slotSelectionPage import slot_selection_page_content


def slot_selection_page() -> rx.Component:
    return rx.box(slot_selection_page_content())
