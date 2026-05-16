import reflex as rx
from component.landlord_backoffice.landlord_layout import landlord_layout


def _kpi_card(label: str, value: str, delta: str, sub: str, positive: bool = True, has_check: bool = False) -> rx.Component:
    delta_cls = "text-backoffice-primary" if positive else "text-error"
    return rx.box(
        rx.text(label, class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1"),
        rx.hstack(
            rx.text(value, class_name="text-2xl font-bold text-on-surface"),
            rx.hstack(
                rx.text(delta, class_name=f"text-xs font-bold {delta_cls}"),
                rx.el.span("check_circle", class_name="material-symbols-outlined text-[14px] fill-icon text-secondary") if has_check else rx.fragment(),
                class_name="flex items-center gap-0.5",
            ),
            class_name="flex items-baseline gap-2",
        ),
        rx.text(sub, class_name="text-xs text-on-surface-variant mt-0.5"),
        class_name="backoffice-kpi-card flex-1",
    )


_REVENUE_DATA = [
    {"day": "MON", "gross": 105, "net": 70},
    {"day": "TUE", "gross": 118, "net": 79},
    {"day": "WED", "gross": 140, "net": 98},
    {"day": "THU", "gross": 196, "net": 154},
    {"day": "FRI", "gross": 182, "net": 136},
    {"day": "SAT", "gross": 154, "net": 112},
    {"day": "SUN", "gross": 84, "net": 50},
]


def _revenue_chart() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("Filtered Revenue Trends", class_name="text-base font-bold text-on-surface"),
                rx.text("Daily yield tracking across all primary corridors (THB thousands)",
                        class_name="text-xs text-on-surface-variant mt-0.5"),
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.recharts.responsive_container(
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False, stroke="#f0f0e8"),
                rx.recharts.x_axis(data_key="day"),
                rx.recharts.y_axis(width=30),
                rx.recharts.tooltip(),
                rx.recharts.legend(),
                rx.recharts.bar(data_key="gross", fill="#344e00", name="Gross Yield", radius=4),
                rx.recharts.bar(data_key="net", fill="#96c93e", name="Net Profit", radius=4),
                data=_REVENUE_DATA,
                bar_category_gap="35%",
            ),
            width="100%",
            height=320,
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )


def landlord_revenue_page_content() -> rx.Component:
    return landlord_layout(
        "revenue",
        rx.box(
            rx.hstack(
                rx.heading("Revenue Portfolio", as_="h1",
                           class_name="text-3xl font-bold font-headline italic text-primary"),
                rx.hstack(
                    rx.el.button(
                        rx.hstack(
                            rx.el.span("calendar_month", class_name="material-symbols-outlined text-[16px]"),
                            rx.text("Last 30 Days", class_name="text-sm"),
                            class_name="flex items-center gap-1",
                        ),
                        class_name="bg-white border border-outline-variant/40 rounded-full px-4 py-2 text-on-surface cursor-pointer",
                    ),
                    rx.el.button(
                        rx.hstack(
                            rx.el.span("download", class_name="material-symbols-outlined text-[16px]"),
                            rx.text("Export PDF", class_name="text-sm font-bold"),
                            class_name="flex items-center gap-1",
                        ),
                        class_name="backoffice-btn-primary border-0 rounded-full px-5 py-2 cursor-pointer",
                    ),
                    class_name="flex items-center gap-3",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.grid(
                _kpi_card("This Month", "฿4.2M", "~8.4%", "vs. Last Month (3.87M)"),
                _kpi_card("YTD Revenue", "฿21M", "~4.2%", "vs. Projections (19.8M)"),
                _kpi_card("Avg Per Space", "฿84,000", "~+7.1%", "Market Avg: ฿78,500"),
                columns="3",
                class_name="gap-4 mb-6",
            ),
            _revenue_chart(),
        ),
    )
