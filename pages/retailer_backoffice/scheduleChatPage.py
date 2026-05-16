import reflex as rx
from component.retailer_backoffice.scheduleChatPage import schedule_chat_page_content


def schedule_chat_page() -> rx.Component:
    return rx.box(schedule_chat_page_content())

