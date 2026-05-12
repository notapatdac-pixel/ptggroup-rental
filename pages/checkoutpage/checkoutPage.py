import reflex as rx

from component.checkoutpage.checkoutPage import checkout_page_component
from component.checkoutpage.checkout_plans_catalog import CHECKOUT_PLANS


def checkout_growth_page() -> rx.Component:
    return rx.box(checkout_page_component(CHECKOUT_PLANS["growth"]))


def checkout_pro_page() -> rx.Component:
    return rx.box(checkout_page_component(CHECKOUT_PLANS["pro"]))
