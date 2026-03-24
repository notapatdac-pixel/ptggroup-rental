import reflex as rx


def bottom_cta() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                rx.heading("Ready to find your next store?", as_="h2", class_name="text-5xl lg:text-6xl mb-8 leading-tight"),
                rx.text(
                    "Join 3,890+ retailers scaling their businesses across PTG’s premium nationwide energy and retail network.",
                    class_name="text-xl mb-12 opacity-90 max-w-2xl mx-auto font-body",
                ),
                rx.el.button(
                    "Get started free",
                    type="button",
                    class_name="btn-lime-white-cta inline-flex items-center justify-center bg-white text-on-surface px-10 py-5 rounded-md text-lg font-bold shadow-xl border-0 cursor-pointer transition-all active:scale-95",
                ),
                class_name="relative z-10",
            ),
            rx.box(class_name="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full blur-3xl -mr-32 -mt-32"),
            rx.box(class_name="absolute bottom-0 left-0 w-96 h-96 bg-black/10 rounded-full blur-3xl -ml-48 -mb-48"),
            class_name="max-w-full primary-gradient p-12 lg:p-40 relative overflow-hidden text-center text-white",
        ),
    )
