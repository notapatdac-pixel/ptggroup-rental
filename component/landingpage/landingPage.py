import reflex as rx
from component.landingpage.bottom_cta import bottom_cta
from component.landingpage.featured_opportunities import featured_opportunities
from component.landingpage.footer import footer
from component.landingpage.hero_section import hero_section
from component.landingpage.how_it_works import how_it_works
from component.landingpage.nav_bar import nav_bar
from component.landingpage.pricing_preview import pricing_preview

def landing_page_component() -> rx.Component:
    return rx.box(
        nav_bar(),
        hero_section(),
        how_it_works(),
        featured_opportunities(),
        pricing_preview(),
        bottom_cta(),
        footer(),
        class_name="bg-background text-on-surface",
    )