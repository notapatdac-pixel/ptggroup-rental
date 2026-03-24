import reflex as rx


def _step(icon: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.span(
                icon,
                class_name="material-symbols-outlined text-3xl text-primary",
            ),
            class_name=(
                "w-16 h-16 rounded-xl shrink-0 flex items-center justify-center "
                "border border-lime-200/90 shadow-sm mb-6"
            ),
        ),
        rx.heading(title, as_="h3", class_name="text-2xl mb-4 text-on-surface"),
        rx.text(description, class_name="text-on-surface-variant leading-relaxed"),
        class_name="flex flex-col items-start",
    )


def how_it_works() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                rx.heading("How It Works", as_="h2", class_name="text-5xl text-on-surface mb-6"),
                rx.box(class_name="w-24 h-1 primary-gradient mx-auto rounded-full"),
                class_name="text-center mb-16 md:mb-20",
            ),
            rx.grid(
                _step(
                    "map",
                    "Explore Verified Locations",
                    "Access our nationwide database of premium retail spots within PTG’s extensive gas station network.",
                ),
                _step(
                    "psychology",
                    "Analyze with AI",
                    "Leverage ML models and our AI advisor to predict foot traffic, demographic fit, and revenue potential.",
                ),
                _step(
                    "rocket_launch",
                    "Apply and Open",
                    "Streamline your application process through our digital platform and launch your store in record time.",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-12 md:gap-10 lg:gap-16 max-w-7xl mx-auto items-start",
            ),
        ),
        class_name="py-32 md:py-44 lg:py-52 px-6 sm:px-8 bg-surface",
    )
