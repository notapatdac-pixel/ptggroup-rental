import reflex as rx
from component.retailer_backoffice.mlPredictionsPage import ml_predictions_page_content


def ml_predictions_page() -> rx.Component:
    return rx.box(ml_predictions_page_content())

