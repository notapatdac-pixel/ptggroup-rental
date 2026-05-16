import reflex as rx

from component.auth_state import AuthState

_LABEL_CLS = "text-[10px] uppercase font-bold tracking-widest text-on-surface-variant mb-1.5 block"
_INPUT_CLS = (
    "w-full bg-surface-container-low border-0 border-b-2 border-surface-container-highest "
    "px-1 py-3 text-on-surface text-sm focus:ring-0 focus:border-primary transition-all "
    "outline-none placeholder:text-surface-dim"
)


class SignInTabState(rx.ComponentState):
    tab: str = "retailer"

    def select_retailer(self):
        self.tab = "retailer"

    def select_landlord(self):
        self.tab = "landlord"

    @classmethod
    def get_component(cls, *children, **props) -> rx.Component:
        active_cls = (
            "flex-1 py-2.5 px-6 text-sm font-medium rounded-full bg-white text-on-surface "
            "shadow-sm transition-all cursor-pointer border-0"
        )
        inactive_cls = (
            "flex-1 py-2.5 px-6 text-sm font-medium rounded-full text-on-surface-variant "
            "transition-all cursor-pointer border-0 bg-transparent"
        )

        retailer_active = cls.tab == "retailer"

        tab_toggle = rx.el.div(
            rx.el.button(
                "Retailer",
                type="button",
                on_click=cls.select_retailer,
                class_name=rx.cond(retailer_active, active_cls, inactive_cls),
            ),
            rx.el.button(
                "Landlord",
                type="button",
                on_click=cls.select_landlord,
                class_name=rx.cond(retailer_active, inactive_cls, active_cls),
            ),
            class_name=(
                "flex bg-surface-container rounded-full p-1 mb-6"
            ),
        )

        email_label = rx.cond(retailer_active, "EMAIL ADDRESS", "CODE")

        apply_link = rx.cond(
            retailer_active,
            rx.hstack(
                rx.text("Don't have an account?", class_name="text-sm text-on-surface-variant"),
                rx.link(
                    "Apply for access",
                    href="/createaccountpage",
                    class_name="text-sm text-primary font-semibold hover:underline no-underline",
                ),
                class_name="flex items-center gap-1.5 justify-center mt-4",
            ),
            rx.fragment(),
        )

        error_msg = rx.cond(
            AuthState.login_error != "",
            rx.box(
                rx.text(AuthState.login_error, class_name="text-xs text-error font-semibold"),
                class_name="bg-error/10 border border-error/20 rounded-lg px-4 py-2",
            ),
            rx.fragment(),
        )

        mock_hint = rx.box(
            rx.text(
                rx.cond(
                    retailer_active,
                    "Test: retailer@ptg.test / retailer123",
                    "Test: landlord@ptg.test / landlord123",
                ),
                class_name="text-[10px] text-on-surface-variant/50 font-mono text-center",
            ),
            class_name="mt-2",
        )

        return rx.box(
            rx.heading(
                "Sign In",
                as_="h1",
                class_name="font-headline text-3xl text-on-surface text-center mb-6",
            ),
            tab_toggle,
            rx.el.div(
                rx.el.div(
                    rx.el.label(email_label, class_name=_LABEL_CLS),
                    rx.el.input(
                        placeholder="name@company.com",
                        type="email",
                        value=AuthState.email_input,
                        on_change=AuthState.set_email,
                        class_name=_INPUT_CLS,
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.hstack(
                        rx.el.label("PASSWORD", class_name=_LABEL_CLS),
                        rx.link(
                            "Forgot?",
                            href="#",
                            class_name=(
                                "text-[10px] uppercase font-bold tracking-widest text-primary "
                                "hover:text-primary/70 transition-colors no-underline"
                            ),
                        ),
                        class_name="flex justify-between items-center mb-1.5",
                    ),
                    rx.el.input(
                        placeholder="••••••••",
                        type="password",
                        value=AuthState.password_input,
                        on_change=AuthState.set_password,
                        class_name=_INPUT_CLS,
                    ),
                    class_name="flex flex-col",
                ),
                error_msg,
                rx.el.button(
                    "SIGN IN",
                    type="button",
                    on_click=AuthState.login,
                    class_name=(
                        "w-full primary-gradient text-on-primary font-bold py-4 rounded-full "
                        "text-sm tracking-widest uppercase shadow-lg shadow-primary/20 "
                        "hover:brightness-110 active:scale-95 transition-all cursor-pointer border-0 mt-2"
                    ),
                ),
                mock_hint,
                class_name="flex flex-col gap-5",
            ),
            apply_link,
            class_name="bg-white rounded-2xl p-10 shadow-sm w-full max-w-xl mx-auto",
            **props,
        )


def login_form_card() -> rx.Component:
    return SignInTabState.create()
