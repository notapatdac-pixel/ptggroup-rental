import reflex as rx
from component.retailerdashboardpage.retailerDashboardPage import retailer_dashboard_page_content


def retailer_dashboard_page() -> rx.Component:
    return rx.box(retailer_dashboard_page_content())
