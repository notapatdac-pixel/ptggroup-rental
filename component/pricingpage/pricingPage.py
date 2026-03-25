import reflex as rx

from component.landingpage.footer import footer
from component.landingpage.nav_bar import nav_bar
from component.pricingpage.pricing_cards_section import pricing_cards_section
from component.pricingpage.pricing_comparison_section import pricing_comparison_section
from component.pricingpage.pricing_hero_section import pricing_hero_section


def pricing_page_component() -> rx.Component:
    return rx.box(
        nav_bar(),
        rx.el.main(
            pricing_hero_section(),
            pricing_cards_section(),
            pricing_comparison_section(),
            class_name="pt-32 pb-24 px-6 md:px-12 max-w-7xl mx-auto",
        ),
        footer(),
        class_name="bg-background text-on-surface",
    )

