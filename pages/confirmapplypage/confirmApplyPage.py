import reflex as rx
from component.confirmapplypage.confirmApplyPage import confirm_apply_page_content


def confirm_apply_page() -> rx.Component:
    return rx.box(confirm_apply_page_content())
