import reflex as rx
from component.retailer_backoffice.aiAdvisorPage import ai_advisor_page_content


def ai_advisor_page() -> rx.Component:
    return rx.box(ai_advisor_page_content())

