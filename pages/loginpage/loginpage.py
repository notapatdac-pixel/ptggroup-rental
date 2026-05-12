import reflex as rx

from component.loginpage.loginPage import login_page_component


def login_page() -> rx.Component:
    return rx.box(
        login_page_component(),
        class_name="bg-background text-on-background min-h-screen flex flex-col",
    )