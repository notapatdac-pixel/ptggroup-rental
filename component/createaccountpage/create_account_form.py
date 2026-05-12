import reflex as rx

_LABEL_CLS = "text-[10px] uppercase font-bold tracking-widest text-on-surface-variant mb-1.5 block"
_INPUT_CLS = (
    "w-full bg-transparent border-0 border-b border-outline-variant px-0 py-2.5 "
    "text-on-surface text-sm focus:ring-0 focus:border-primary transition-all outline-none "
    "placeholder:text-on-surface-variant/40"
)


def _field(label: str, placeholder: str, input_type: str = "text") -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name=_LABEL_CLS),
        rx.el.input(placeholder=placeholder, type=input_type, class_name=_INPUT_CLS),
        class_name="flex flex-col",
    )


def create_account_form() -> rx.Component:
    return rx.el.div(
        rx.box(
            rx.heading(
                rx.fragment("Create your", rx.el.br(), "account"),
                as_="h1",
                class_name="font-headline text-4xl text-on-surface text-center mb-3 leading-tight",
            ),
            rx.text(
                "Join the leading retail intelligence platform.",
                class_name="text-on-surface-variant text-sm text-center mb-8",
            ),
            rx.el.form(
                rx.el.div(
                    _field("FIRST NAME", "John"),
                    _field("LAST NAME", "Doe"),
                    class_name="grid grid-cols-2 gap-4",
                ),
                _field("EMAIL ADDRESS", "analyst@ptg-retail.com", "email"),
                _field("PASSWORD", "••••••••", "password"),
                rx.el.button(
                    "CREATE ACCOUNT",
                    type="submit",
                    class_name=(
                        "w-full bg-lime-500 hover:bg-lime-400 active:bg-lime-600 text-white "
                        "font-bold py-4 rounded-full text-sm tracking-widest transition-colors "
                        "cursor-pointer border-0 mt-2"
                    ),
                ),
                class_name="flex flex-col gap-5",
                action="#",
            ),
            rx.el.hr(class_name="border-outline-variant/20 my-6"),
            rx.hstack(
                rx.text("Already have an account?", class_name="text-sm text-on-surface-variant"),
                rx.link(
                    "Sign in",
                    href="/loginpage",
                    class_name="text-sm text-primary font-semibold hover:underline no-underline",
                ),
                class_name="flex items-center gap-1.5 justify-center",
            ),
            class_name="bg-white rounded-2xl p-10 shadow-sm w-full max-w-md mx-auto",
        ),
        class_name="flex items-center justify-center min-h-screen px-4",
    )
