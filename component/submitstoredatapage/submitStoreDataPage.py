import reflex as rx

from component.backoffice.backoffice_layout import backoffice_layout

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
        rx.grid(
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
            rx.box(
                rx.box(
                    rx.text("Why Submit?", class_name="text-sm font-bold text-on-surface mb-4"),
                    rx.vstack(
                        rx.hstack(
                            rx.el.span("benchmark", class_name="material-symbols-outlined text-backoffice-primary text-lg flex-shrink-0"),
                            rx.box(
                                rx.text("Precision Benchmarking", class_name="text-xs font-bold text-on-surface"),
                                rx.text("See how your stores compare to competitors in the region.", class_name="text-xs text-on-surface-variant leading-relaxed"),
                            ),
                            class_name="flex items-start gap-3",
                        ),
                        rx.hstack(
                            rx.el.span("psychology", class_name="material-symbols-outlined text-backoffice-primary text-lg flex-shrink-0"),
                            rx.box(
                                rx.text("AI Forecasting", class_name="text-xs font-bold text-on-surface"),
                                rx.text("Power our ML models to predict future traffic and revenue.", class_name="text-xs text-on-surface-variant leading-relaxed"),
                            ),
                            class_name="flex items-start gap-3",
                        ),
                        rx.hstack(
                            rx.el.span("lock", class_name="material-symbols-outlined text-backoffice-primary text-lg flex-shrink-0"),
                            rx.box(
                                rx.text("Data Sovereignty", class_name="text-xs font-bold text-on-surface"),
                                rx.text("Your data is encrypted and aggregated, ensuring anonymity at all times.", class_name="text-xs text-on-surface-variant leading-relaxed"),
                            ),
                            class_name="flex items-start gap-3",
                        ),
                        class_name="gap-4",
                    ),
                    class_name="bg-white rounded-2xl p-6 shadow-sm mb-4",
                ),
                rx.box(
                    rx.text("Contribution Stats", class_name="text-xs font-bold text-on-surface mb-3"),
                    rx.hstack(
                        rx.box(
                            rx.text("24/30", class_name="text-2xl font-bold text-on-surface"),
                            rx.text("Days submitted", class_name="text-[10px] text-on-surface-variant"),
                        ),
                        rx.box(
                            rx.text("Top", class_name="text-xs text-on-surface-variant"),
                            rx.text("15%", class_name="text-2xl font-bold text-backoffice-primary"),
                            rx.text("PLATFORM\nRANKING", class_name="text-[9px] font-bold text-on-surface-variant tracking-widest"),
                        ),
                        class_name="flex gap-6",
                    ),
                    class_name="bg-white rounded-2xl p-5 shadow-sm",
                ),
            ),
            columns="2",
            class_name="gap-6",
            style={"grid-template-columns": "2fr 1fr"},
        ),
    )
