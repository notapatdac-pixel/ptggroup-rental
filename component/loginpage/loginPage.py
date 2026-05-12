import reflex as rx

from component.loginpage.login_branding import login_mini_nav
from component.loginpage.login_form_card import login_form_card
from component.loginpage.login_images_strip import login_images_strip


def login_page_component() -> rx.Component:
    return rx.box(
        login_mini_nav(),
        rx.el.main(
            rx.el.div(
                login_form_card(),
                class_name="flex items-center justify-center min-h-screen px-4 pt-16 pb-10",
            ),
            rx.el.div(
                login_images_strip(),
                class_name="pb-16",
            ),
        ),
        class_name="bg-auth-surface text-on-surface min-h-screen",
    )
