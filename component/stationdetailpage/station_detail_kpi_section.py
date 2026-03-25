import reflex as rx


def _kpi_shell(label: str, body: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            label,
            class_name="text-xs font-bold text-outline-variant uppercase tracking-widest mb-4",
        ),
        body,
        class_name="bg-surface-container-lowest p-6 rounded-xl editorial-shadow",
    )


def station_kpi_section(station: dict) -> rx.Component:
    d = station["detail"]
    return rx.el.div(
        _kpi_shell(
            "Daily Customers",
            rx.el.div(
                rx.el.span(
                    "0",
                    class_name="ptg-count-up font-headline text-4xl text-on-surface tabular-nums",
                    custom_attrs={
                        "data-ptg-count": str(d["daily_customers_num"]),
                        "data-ptg-mode": "int",
                    },
                ),
                rx.el.span(d["daily_delta"], class_name="text-secondary text-sm font-medium"),
                class_name="flex items-baseline gap-2",
            ),
        ),
        _kpi_shell(
            "Dwell Time",
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "0",
                        class_name="ptg-count-up font-headline text-4xl text-on-surface tabular-nums",
                        custom_attrs={
                            "data-ptg-count": str(d["dwell_min_num"]),
                            "data-ptg-mode": "int",
                        },
                    ),
                    rx.el.span(" min", class_name="text-xl font-body text-on-surface-variant"),
                    class_name="flex items-baseline gap-2",
                ),
                rx.el.span("Avg", class_name="text-on-surface-variant text-sm font-medium"),
                class_name="flex items-baseline gap-2",
            ),
        ),
        _kpi_shell(
            "Est. Revenue",
            rx.el.div(
                rx.el.h3(
                    rx.el.span(
                        "0",
                        class_name="ptg-count-up font-headline text-4xl text-on-surface tabular-nums",
                        custom_attrs={
                            "data-ptg-count": str(d["est_revenue_k"]),
                            "data-ptg-mode": "k",
                        },
                    ),
                    rx.el.span("K", class_name="font-headline text-4xl text-on-surface"),
                    rx.el.span(
                        " THB",
                        class_name="text-xl font-body text-on-surface-variant font-normal",
                    ),
                    class_name="font-headline text-4xl text-on-surface flex items-baseline gap-0.5 flex-wrap",
                ),
                class_name="flex items-baseline gap-2",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span("smart_toy", class_name="material-symbols-outlined text-5xl"),
                class_name="absolute top-0 right-0 p-3 opacity-10",
            ),
            rx.el.p(
                "AI Score",
                class_name="text-xs font-bold text-outline-variant uppercase tracking-widest mb-4",
            ),
            rx.el.div(
                rx.el.h3(
                    rx.el.span(
                        "0",
                        class_name="ptg-count-up font-headline text-4xl text-primary tabular-nums",
                        custom_attrs={
                            "data-ptg-count": str(d["ai_score_num"]),
                            "data-ptg-mode": "pct",
                        },
                    ),
                    rx.el.span("%", class_name="font-headline text-4xl text-primary"),
                    class_name="font-headline text-4xl text-primary flex items-baseline gap-0.5",
                ),
                rx.el.span(
                    "OPTIMAL",
                    class_name="bg-primary/10 text-primary text-[10px] px-1.5 py-0.5 rounded font-bold",
                ),
                class_name="flex items-baseline gap-2",
            ),
            class_name="bg-surface-container-lowest p-6 rounded-xl editorial-shadow relative overflow-hidden",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6",
    )
