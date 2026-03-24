import reflex as rx


def nav_bar() -> rx.Component:
    return rx.el.nav(
        rx.hstack(
            rx.hstack(
                rx.hstack(
                    rx.text("PTG", class_name="text-4xl font-serif font-bold text-lime-500"),
                    rx.text("Retail Platform", class_name="font-headline text-lg tracking-tight text-on-surface"),
                    class_name="flex items-center gap-2",
                ),
                rx.hstack(
                    rx.link(
                        "Explore Locations",
                        href="#",
                        class_name="nav-link-lime font-sans",
                    ),
                    rx.link(
                        "Pricing",
                        href="#",
                        class_name="nav-link-lime font-sans",
                    ),
                    class_name="hidden md:flex gap-10 items-center",
                ),
                class_name="flex items-center gap-14",
            ),
            rx.hstack(
                rx.el.button(
                    "Sign In",
                    type="button",
                    class_name="btn-lime-ghost inline-flex items-center justify-center bg-transparent text-slate-600 dark:text-slate-400 font-sans text-sm px-4 py-2 border-0 cursor-pointer rounded-md transition-colors",
                ),
                rx.el.button(
                    "Get Started",
                    type="button",
                    class_name="inline-flex items-center justify-center primary-gradient text-white px-6 py-2.5 rounded-md text-sm font-bold shadow-sm border-0 cursor-pointer transition-all hover:shadow-lime-500/40 hover:ring-2 hover:ring-lime-300 hover:ring-offset-2 hover:ring-offset-white/80 active:scale-95",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="w-full flex justify-between items-center px-8 h-20",
        ),
        class_name="fixed top-0 w-full bg-white/80 dark:bg-slate-900/80 backdrop-blur-md z-50",
    )
