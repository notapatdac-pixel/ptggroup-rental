import reflex as rx

from component.loginpage.login_branding import login_branding
from component.loginpage.login_form_card import login_form_card


def login_page_component() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                login_branding(),
                login_form_card(),
                rx.el.p(
                    "© 2024 PTG Retail Platform. All Rights Reserved.",
                    class_name="mt-8 text-center text-[10px] uppercase tracking-widest text-on-surface-variant/40",
                ),
                class_name="w-full max-w-[480px]",
            ),
            class_name="flex-grow flex items-center justify-center px-4 py-12",
        ),
    )

