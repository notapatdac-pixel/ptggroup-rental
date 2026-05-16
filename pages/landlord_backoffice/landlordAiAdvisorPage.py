import reflex as rx
from component.landlord_backoffice.landlordAiAdvisorPage import landlord_ai_advisor_page_content


def landlord_ai_advisor_page() -> rx.Component:
    return rx.box(landlord_ai_advisor_page_content())
