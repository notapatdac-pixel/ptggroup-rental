import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout

_LABEL = "text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1.5 block"
_INPUT = "backoffice-input"


def _peak_chip(label: str, active: bool = False) -> rx.Component:
    return rx.el.span(
        label,
        class_name=f"backoffice-time-chip{'--active' if active else ''} backoffice-time-chip",
    )


def submit_store_data_page_content() -> rx.Component:
    return backoffice_layout(
        "submit_data",
        rx.box(
            rx.box(
                rx.heading("Submit Performance Data", as_="h1", class_name="text-2xl font-bold text-on-surface mb-8"),
                rx.grid(
                    rx.box(
                        rx.el.label("Select Store", class_name=_LABEL),
                        rx.el.select(
                            rx.el.option("Central Embassy - Boutique 4RE"),
                            rx.el.option("Quick Mart - Ari Station"),
                            class_name=f"{_INPUT} w-full",
                        ),
                        class_name="flex flex-col",
                    ),
                    rx.box(
                        rx.el.label("Reporting Month", class_name=_LABEL),
                        rx.el.input(type="month", value="2025-11", class_name=f"{_INPUT} w-full"),
                        class_name="flex flex-col",
                    ),
                    columns="2",
                    class_name="gap-4 mb-4",
                ),
                rx.grid(
                    rx.box(
                        rx.el.label("Monthly Revenue (THB)", class_name=_LABEL),
                        rx.el.input(placeholder="0.00", type="number", class_name=f"{_INPUT} w-full"),
                        class_name="flex flex-col",
                    ),
                    rx.box(
                        rx.el.label("Daily Customers (Avg)", class_name=_LABEL),
                        rx.el.input(placeholder="Enter average daily count", type="number", class_name=f"{_INPUT} w-full"),
                        class_name="flex flex-col",
                    ),
                    columns="2",
                    class_name="gap-4 mb-4",
                ),
                rx.box(
                    rx.el.label("Peak Traffic Hours", class_name=_LABEL),
                    rx.hstack(
                        _peak_chip("08:00 - 11:00"),
                        _peak_chip("11:00 - 14:00", active=True),
                        _peak_chip("14:00 - 17:00"),
                        _peak_chip("17:00 - 20:00", active=True),
                        _peak_chip("20:00 - 23:00"),
                        class_name="flex flex-wrap gap-2",
                    ),
                    class_name="mb-6",
                ),
                rx.el.button(
                    rx.hstack(
                        rx.el.span("upload_file", class_name="material-symbols-outlined text-base"),
                        rx.text("Submit Monthly Report", class_name="font-bold"),
                        class_name="flex items-center gap-2",
                    ),
                    class_name="backoffice-btn-primary w-full py-3.5 rounded-xl border-0 cursor-pointer text-sm",
                ),
                rx.text("CONFIDENTIAL ENCRYPTED SUBMISSION", class_name="text-[10px] text-center text-on-surface-variant/50 tracking-widest uppercase mt-3"),
                class_name="bg-white rounded-2xl p-8 shadow-sm",
            ),
            class_name="w-full",
        ),
    )

