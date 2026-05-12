import reflex as rx
from component.schedulechatpage.scheduleChatPage import schedule_chat_page_content


def schedule_chat_page() -> rx.Component:
    return rx.box(schedule_chat_page_content())
