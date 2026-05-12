import reflex as rx

from component.createaccountpage.createAccountPage import create_account_page_component


def create_account_page() -> rx.Component:
    return rx.box(create_account_page_component())
