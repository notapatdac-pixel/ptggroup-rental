import reflex as rx


def login_branding() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "PTG Retail Platform",
            class_name="text-4xl font-headline italic text-primary mb-2",
        ),
        rx.el.p(
            "Access your retail workspace",
            class_name="text-on-surface-variant font-body tracking-tight",
        ),
        class_name="text-center mb-10",
    )
