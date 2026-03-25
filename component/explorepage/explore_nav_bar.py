import reflex as rx


def explore_nav_bar() -> rx.Component:
    from component.landingpage.nav_bar import nav_bar

    return nav_bar(show_search=True)

