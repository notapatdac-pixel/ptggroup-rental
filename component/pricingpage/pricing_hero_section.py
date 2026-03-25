import reflex as rx


def pricing_hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.span(
            "Pricing",
            class_name="text-primary font-label tracking-[0.2em] uppercase text-xs font-bold mb-4 block",
        ),
        rx.heading(
            "Simple, transparent pricing",
            as_="h1",
            class_name="font-headline text-5xl md:text-7xl text-on-surface mb-6 leading-tight",
        ),
        rx.text(
            "Start free, upgrade as your business grows. No hidden fees, just pure data-driven growth.",
            class_name="text-on-surface-variant text-lg md:text-xl max-w-2xl mx-auto font-body",
        ),
        class_name="text-center mb-20",
    )

