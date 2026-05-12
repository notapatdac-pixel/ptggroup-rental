import reflex as rx


class LoginFormCardState(rx.ComponentState):
    password_visible: bool = False

    def toggle_password_visibility(self):
        self.password_visible = not self.password_visible

    @classmethod
    def get_component(cls, *children, **props) -> rx.Component:
        pwd_type = rx.cond(cls.password_visible, "text", "password")
        visibility_icon = rx.cond(
            cls.password_visible,
            rx.el.span(
                "visibility_off",
                class_name="material-symbols-outlined text-[20px]",
            ),
            rx.el.span(
                "visibility",
                class_name="material-symbols-outlined text-[20px]",
            ),
        )
        return rx.el.div(
            rx.el.header(
                rx.el.h2(
                    "Sign In",
                    class_name="text-2xl font-headline text-on-surface mb-2",
                ),
                rx.el.p(
                    "Enter your credentials to manage your portfolio.",
                    class_name="text-sm text-on-surface-variant",
                ),
                class_name="mb-8",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Email Address",
                        html_for="login-email",
                        class_name="block text-[10px] uppercase tracking-[0.05em] font-bold text-on-surface-variant",
                    ),
                    rx.el.div(
                        rx.el.input(
                            id="login-email",
                            name="email",
                            type="email",
                            placeholder="name@company.com",
                            class_name=(
                                "w-full bg-surface-container-lowest border-0 border-b-2 "
                                "border-surface-container-highest px-0 py-3 text-on-surface "
                                "focus:ring-0 focus:border-primary focus:bg-surface-bright "
                                "transition-all placeholder:text-surface-dim"
                            ),
                        ),
                        class_name="relative",
                    ),
                    class_name="space-y-1.5",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Password",
                            html_for="login-password",
                            class_name="block text-[10px] uppercase tracking-[0.05em] font-bold text-on-surface-variant",
                        ),
                        rx.link(
                            "Forgot?",
                            href="#",
                            class_name=(
                                "text-[10px] uppercase tracking-[0.05em] font-bold text-primary "
                                "hover:text-primary-container transition-colors no-underline"
                            ),
                        ),
                        class_name="flex justify-between items-end",
                    ),
                    rx.el.div(
                        rx.el.input(
                            id="login-password",
                            name="password",
                            type=pwd_type,
                            placeholder="••••••••",
                            class_name=(
                                "w-full bg-surface-container-lowest border-0 border-b-2 "
                                "pr-10 border-surface-container-highest px-0 py-3 text-on-surface "
                                "focus:ring-0 focus:border-primary focus:bg-surface-bright "
                                "transition-all placeholder:text-surface-dim"
                            ),
                        ),
                        rx.el.button(
                            visibility_icon,
                            type="button",
                            on_click=cls.toggle_password_visibility,
                            class_name=(
                                "absolute right-0 top-1/2 -translate-y-1/2 "
                                "text-on-surface-variant/50 hover:text-on-surface border-0 bg-transparent cursor-pointer p-1"
                            ),
                        ),
                        class_name="relative",
                    ),
                    class_name="space-y-1.5",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.el.span("Sign In to Portal"),
                        rx.el.span(
                            "arrow_forward",
                            class_name=(
                                "material-symbols-outlined text-[18px] "
                                "group-hover:translate-x-0.5 transition-transform"
                            ),
                        ),
                        type="submit",
                        class_name=(
                            "w-full primary-gradient text-on-primary font-bold py-4 rounded-lg "
                            "shadow-lg shadow-primary/10 hover:brightness-110 active:scale-[0.98] "
                            "transition-all flex items-center justify-center gap-2 group border-0 cursor-pointer"
                        ),
                    ),
                    class_name="pt-4",
                ),
                action="#",
                class_name="space-y-6",
            ),
            rx.el.footer(
                rx.el.p(
                    rx.el.span("Don't have an account? "),
                    rx.link(
                        "Apply for Access",
                        href="/pricingpage",
                        class_name="text-primary font-bold hover:underline",
                    ),
                    class_name="text-sm text-on-surface-variant",
                ),
                class_name="mt-8 pt-8 border-t border-outline-variant/10 text-center",
            ),
            class_name=(
                "bg-surface-container-lowest rounded-xl p-10 editorial-shadow "
                "border border-outline-variant/10"
            ),
            **props,
        )


def login_form_card() -> rx.Component:
    return LoginFormCardState.create()
