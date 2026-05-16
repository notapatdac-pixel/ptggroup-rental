import reflex as rx
from component.retailer_backoffice.approvedDocsPage import approved_docs_page_content


def approved_docs_page() -> rx.Component:
    return rx.box(approved_docs_page_content())

