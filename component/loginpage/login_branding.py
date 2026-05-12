import reflex as rx


def login_mini_nav() -> rx.Component:
    """Minimal top bar used on Sign In and Create Account pages."""
    return rx.el.nav(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.text("PTG", class_name="text-2xl font-serif font-bold text-lime-600"),
                    rx.text(
                        "Retail Platform",
                        class_name="font-semibold text-on-surface tracking-tight text-base",
                    ),
                    class_name="flex items-center gap-1.5",
                ),
                href="/",
                class_name="no-underline",
            ),
            rx.link(
                "Back",
                href="/",
                class_name="auth-back-link text-on-surface text-sm font-medium no-underline",
            ),
            class_name="flex justify-between items-center w-full px-8 h-16",
        ),
        class_name="fixed top-0 w-full bg-auth-surface z-50",
    )
