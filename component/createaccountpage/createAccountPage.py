import reflex as rx

from component.createaccountpage.create_account_form import create_account_form
from component.loginpage.login_branding import login_mini_nav


def create_account_page_component() -> rx.Component:
    return rx.box(
        login_mini_nav(),
        create_account_form(),
        class_name="bg-auth-surface text-on-surface min-h-screen",
    )
