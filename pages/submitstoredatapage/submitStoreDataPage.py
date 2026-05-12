import reflex as rx
from component.submitstoredatapage.submitStoreDataPage import submit_store_data_page_content


def submit_store_data_page() -> rx.Component:
    return rx.box(submit_store_data_page_content())
