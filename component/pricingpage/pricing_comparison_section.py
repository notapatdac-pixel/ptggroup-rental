import reflex as rx


def _check_cell() -> rx.Component:
    return rx.el.td(
        rx.el.span("check", class_name="material-symbols-outlined text-primary"),
        class_name="py-5 px-8 text-center",
    )


def _dash_cell() -> rx.Component:
    return rx.el.td(
        "—",
        class_name="py-5 px-8 text-center text-on-surface-variant",
    )


def pricing_comparison_section() -> rx.Component:
    return rx.el.section(
        rx.heading("Compare features", as_="h2", class_name="font-headline text-3xl text-center mb-12"),
        rx.box(
            rx.box(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Feature",
                                class_name="py-6 px-8 text-xs font-label uppercase tracking-widest text-on-surface-variant font-bold text-left",
                            ),
                            rx.el.th("Free", class_name="py-6 px-8 text-xs font-label uppercase tracking-widest text-on-surface-variant font-bold text-center"),
                            rx.el.th("Pro", class_name="py-6 px-8 text-xs font-label uppercase tracking-widest text-on-surface-variant font-bold text-center"),
                            rx.el.th("Growth", class_name="py-6 px-8 text-xs font-label uppercase tracking-widest text-on-surface-variant font-bold text-center"),
                        )
                    ),
                    rx.el.tbody(
                        rx.el.tr(
                            rx.el.td("Browse all listings", class_name="py-5 px-8 text-sm font-medium"),
                            _check_cell(),
                            _check_cell(),
                            _check_cell(),
                        ),
                        rx.el.tr(
                            rx.el.td("Apply for 2 spaces", class_name="py-5 px-8 text-sm font-medium"),
                            _check_cell(),
                            _check_cell(),
                            _check_cell(),
                        ),
                        rx.el.tr(
                            rx.el.td("AI recommendations", class_name="py-5 px-8 text-sm font-medium"),
                            _dash_cell(),
                            _check_cell(),
                            _check_cell(),
                        ),
                        rx.el.tr(
                            rx.el.td("Traffic analytics", class_name="py-5 px-8 text-sm font-medium"),
                            _dash_cell(),
                            _check_cell(),
                            _check_cell(),
                        ),
                        rx.el.tr(
                            rx.el.td("ML predictions", class_name="py-5 px-8 text-sm font-medium"),
                            _dash_cell(),
                            _dash_cell(),
                            _check_cell(),
                        ),
                        rx.el.tr(
                            rx.el.td("Retailer dashboard", class_name="py-5 px-8 text-sm font-medium"),
                            _dash_cell(),
                            _dash_cell(),
                            _check_cell(),
                        ),
                    ),
                    class_name="w-full text-left border-collapse",
                ),
                class_name="bg-surface-container-lowest rounded-lg overflow-x-auto",
            ),
            class_name="bg-surface-container-low rounded-xl overflow-hidden p-1",
        ),
        class_name="max-w-5xl mx-auto",
    )

