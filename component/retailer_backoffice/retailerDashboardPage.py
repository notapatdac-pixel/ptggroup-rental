import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout


def _kpi_card(label: str, value: str, sub: str, growth: str = "") -> rx.Component:
    return rx.box(
        rx.text(label, class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1"),
        rx.text(value, class_name="text-3xl font-bold text-on-surface leading-tight"),
        rx.hstack(
            rx.text(growth, class_name="text-xs font-bold text-backoffice-primary") if growth else rx.fragment(),
            rx.text(sub, class_name="text-xs text-on-surface-variant"),
            class_name="flex items-center gap-2 mt-1",
        ),
        class_name="backoffice-kpi-card flex-1",
    )


_REVENUE_DATA = [
    {"month": "Jan", "coffee": 55, "mart": 40},
    {"month": "Feb", "coffee": 62, "mart": 48},
    {"month": "Mar", "coffee": 70, "mart": 50},
    {"month": "Apr", "coffee": 80, "mart": 58},
    {"month": "May", "coffee": 90, "mart": 65},
    {"month": "Jun", "coffee": 95, "mart": 72},
]


def _revenue_trend_chart() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("Revenue Trend", class_name="text-base font-bold text-on-surface"),
            rx.text("Performance by store (THB thousands)", class_name="text-xs text-on-surface-variant"),
            class_name="flex justify-between items-center mb-2",
        ),
        rx.recharts.responsive_container(
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False, stroke="#f0f0e8"),
                rx.recharts.x_axis(data_key="month"),
                rx.recharts.y_axis(width=30),
                rx.recharts.tooltip(),
                rx.recharts.legend(),
                rx.recharts.bar(data_key="coffee", fill="#466800", name="Coffee Corner", radius=3),
                rx.recharts.bar(data_key="mart", fill="#d4d4c0", name="Quick Mart", radius=3),
                data=_REVENUE_DATA,
                bar_category_gap="40%",
            ),
            width="100%",
            height=220,
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )



def _store_row(img_placeholder: str, name: str, loc: str, revenue: str, status: str, score: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.el.span("storefront", class_name="material-symbols-outlined text-on-surface-variant"),
            class_name="w-10 h-10 bg-surface-container rounded-lg flex items-center justify-center flex-shrink-0",
        ),
        rx.box(
            rx.text(name, class_name="text-sm font-semibold text-on-surface"),
            rx.text(loc, class_name="text-xs text-on-surface-variant"),
            class_name="flex-1",
        ),
        rx.text(revenue, class_name="text-sm font-bold text-on-surface w-28"),
        rx.box(
            rx.text(status, class_name=f"backoffice-chip-{'reviewing' if status == 'ACTIVE' else 'submitted'}"),
        ),
        rx.text(score, class_name="text-sm font-bold text-backoffice-primary w-10 text-right"),
        class_name="flex items-center gap-4 py-3 border-b border-outline-variant/20 last:border-0",
    )



def _traffic_distribution() -> rx.Component:
    rows = [
        ("MORNING", "62%", 62), ("AFTERNOON", "24%", 24), ("EVENING", "10%", 10), ("NIGHT", "4%", 4),
    ]
    return rx.box(
        rx.text("Traffic Distribution", class_name="text-sm font-bold text-on-surface mb-4"),
        rx.vstack(
            *[
                rx.box(
                    rx.hstack(
                        rx.text(label, class_name="text-[10px] font-bold tracking-widest text-on-surface-variant w-20"),
                        rx.box(
                            rx.box(class_name="backoffice-progress-fill", style={"width": f"{pct}%"}),
                            class_name="backoffice-progress-track flex-1",
                        ),
                        rx.text(val, class_name="text-xs font-bold text-on-surface w-8 text-right"),
                        class_name="flex items-center gap-3",
                    ),
                    class_name="w-full",
                )
                for label, val, pct in rows
            ],
            class_name="gap-3 w-full",
        ),
        class_name="backoffice-kpi-card",
    )


def retailer_dashboard_page_content() -> rx.Component:
    return backoffice_layout(
        "dashboard",
        rx.box(
            rx.hstack(
                rx.box(
                    rx.heading("Welcome back, Siriporn.", as_="h1", class_name="text-2xl font-bold text-on-surface"),
                    rx.text("Here's what happened with your retail network today.", class_name="text-sm text-on-surface-variant mt-1"),
                ),
                rx.hstack(
                    rx.el.button(
                        rx.hstack(
                            rx.el.span("refresh", class_name="material-symbols-outlined text-base"),
                            rx.text("Refresh", class_name="text-sm font-bold"),
                            class_name="flex items-center gap-1.5",
                        ),
                        class_name="bg-white border border-outline-variant/40 rounded-full px-4 py-2 cursor-pointer text-on-surface hover:bg-surface-container-low transition-colors",
                    ),
                    rx.el.button(
                        rx.hstack(
                            rx.el.span("upload", class_name="material-symbols-outlined text-base"),
                            rx.text("Export Report", class_name="text-sm font-bold"),
                            class_name="flex items-center gap-1.5",
                        ),
                        class_name="backoffice-btn-primary px-4 py-2 rounded-full border-0 cursor-pointer",
                    ),
                    class_name="flex items-center gap-3",
                ),
                class_name="flex justify-between items-start mb-6",
            ),
            rx.grid(
                _kpi_card("Monthly Revenue", "฿5k", "from last month", "+10% growth"),
                _kpi_card("Daily Customers", "340", "avg/day", "+5% growth"),
                _kpi_card("Active Stores", "2", "0 closed today"),
                columns="3",
                class_name="gap-4 mb-6",
            ),
            rx.grid(
                rx.box(
                    _revenue_trend_chart(),
                    rx.box(
                        rx.hstack(
                            rx.text("My Stores", class_name="text-base font-bold text-on-surface"),
                            rx.link("View All", href="#", class_name="text-xs font-bold text-backoffice-primary no-underline"),
                            class_name="flex justify-between items-center mb-3",
                        ),
                        _store_row("", "Coffee Corner - Rama IX", "Bangkok, Thailand", "฿142,000 THB", "ACTIVE", "94"),
                        _store_row("", "Quick Mart - Ari Station", "Bangkok, Thailand", "฿142,000 THB", "ACTIVE", "92%"),
                        class_name="bg-white rounded-2xl p-6 shadow-sm mt-4",
                    ),
                    class_name="flex flex-col gap-0",
                    style={"grid_column": "span 2"},
                ),
                _traffic_distribution(),
                columns="3",
                class_name="gap-6",
            ),
        ),
    )

