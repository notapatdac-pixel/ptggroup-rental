import reflex as rx
from component.retailer_backoffice.retailerProfileSetupPage import retailer_profile_setup_page_content


def retailer_profile_setup_page() -> rx.Component:
    return rx.box(retailer_profile_setup_page_content())
