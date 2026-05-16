import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout


def _perf_kpi(label: str, value: str, sub: str = "", badge: str = "") -> rx.Component:
    return rx.box(
        rx.text(label, class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1"),
        rx.text(value, class_name="text-2xl font-bold text-on-surface leading-tight"),
        rx.hstack(
            rx.text(sub, class_name="text-xs text-on-surface-variant") if sub else rx.fragment(),
            rx.box(rx.text(badge, class_name="text-[10px] font-bold text-backoffice-primary"), class_name="backoffice-chip-reviewing") if badge else rx.fragment(),
            class_name="flex items-center gap-2 mt-1",
        ),
        class_name="backoffice-kpi-card flex-1",
    )


_MONTHLY_DATA = [
    {"month": "JAN", "coffee": 98, "mart": 72},
    {"month": "FEB", "coffee": 118, "mart": 82},
    {"month": "MAR", "coffee": 105, "mart": 76},
    {"month": "APR", "coffee": 130, "mart": 91},
    {"month": "MAY", "coffee": 122, "mart": 87},
    {"month": "JUN", "coffee": 165, "mart": 100},
]


def _monthly_revenue_chart() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("Monthly Revenue by Store", class_name="text-base font-bold text-on-surface"),
                rx.text("Comparative analysis across core retail units (THB thousands)", class_name="text-xs text-on-surface-variant"),
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.recharts.responsive_container(
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False, stroke="#f0f0e8"),
                rx.recharts.x_axis(data_key="month"),
                rx.recharts.y_axis(),
                rx.recharts.tooltip(),
                rx.recharts.legend(),
                rx.recharts.bar(data_key="coffee", fill="#466800", name="Coffee Corner", radius=4),
                rx.recharts.bar(data_key="mart", fill="#d4d4c0", name="Quick Mart", radius=4),
                data=_MONTHLY_DATA,
                bar_category_gap="40%",
            ),
            width="100%",
            height=300,
        ),
        rx.box(
            rx.hstack(
                rx.el.span("trending_up", class_name="material-symbols-outlined text-backoffice-primary text-base"),
                rx.box(
                    rx.text("Efficiency Insight", class_name="text-xs font-bold text-on-surface"),
                    rx.text("Coffee Corner outperformed Q2 predictions by 14.8% due to extended Saturday hours.", class_name="text-xs text-on-surface-variant"),
                ),
                rx.link("View Breakdown", href="#", class_name="text-xs font-bold text-backoffice-primary no-underline ml-auto"),
                class_name="flex items-start gap-3",
            ),
            class_name="mt-4 bg-surface-container-low rounded-xl p-4",
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )



_TRAFFIC_DATA = [
    {"day": "MON", "traffic": 35},
    {"day": "TUE", "traffic": 42},
    {"day": "WED", "traffic": 38},
    {"day": "THU", "traffic": 50},
    {"day": "FRI", "traffic": 55},
    {"day": "SAT", "traffic": 90},
    {"day": "SUN", "traffic": 40},
]


def _traffic_dist_chart() -> rx.Component:
    return rx.box(
        rx.text("Traffic Distribution", class_name="text-sm font-bold text-on-surface mb-1"),
        rx.text("Weekly customer volume by day", class_name="text-xs text-on-surface-variant mb-3"),
        rx.recharts.responsive_container(
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False, stroke="#f0f0e8"),
                rx.recharts.x_axis(data_key="day"),
                rx.recharts.y_axis(width=30),
                rx.recharts.tooltip(),
                rx.recharts.bar(data_key="traffic", fill="#466800", name="Customers", radius=3),
                data=_TRAFFIC_DATA,
                bar_category_gap="30%",
            ),
            width="100%",
            height=220,
        ),
        class_name="backoffice-kpi-card",
    )


def performance_page_content() -> rx.Component:
    return backoffice_layout(
        "performance",
        rx.box(
            rx.hstack(
                rx.box(
                    rx.heading("Performance Analytics", as_="h1", class_name="font-headline text-3xl font-bold text-on-surface italic"),
                    rx.hstack(
                        rx.text("Fiscal Year 2024", class_name="text-sm text-on-surface-variant"),
                        rx.text("•", class_name="text-on-surface-variant"),
                        rx.link("Sub-tab 6B Performance Review", href="#", class_name="text-sm font-bold text-backoffice-primary no-underline"),
                        class_name="flex items-center gap-2 mt-1",
                    ),
                ),
                rx.hstack(
                    rx.el.button(
                        rx.hstack(rx.el.span("refresh", class_name="material-symbols-outlined text-base"), rx.text("Refresh", class_name="text-sm font-bold"), class_name="flex items-center gap-1.5"),
                        class_name="bg-white border border-outline-variant/40 rounded-full px-4 py-2 cursor-pointer hover:bg-surface-container-low transition-colors",
                    ),
                    rx.el.button(
                        rx.hstack(rx.el.span("upload", class_name="material-symbols-outlined text-base"), rx.text("Export Report", class_name="text-sm font-bold"), class_name="flex items-center gap-1.5"),
                        class_name="backoffice-btn-primary px-4 py-2 rounded-full border-0 cursor-pointer",
                    ),
                    class_name="flex items-center gap-3",
                ),
                class_name="flex justify-between items-start mb-6",
            ),
            rx.grid(
                _perf_kpi("YTD Revenue", "1.71M THB", "↑ 12% from last month", "Real-time"),
                _perf_kpi("Avg Basket Size", "248 THB", "4% vs target"),
                _perf_kpi("Peak Trading Day", "Saturday", "14:00 - 18:00 Peak window"),
                rx.box(
                    rx.text("YOY GROWTH", class_name="text-[10px] font-bold tracking-widest uppercase text-white/70 mb-1"),
                    rx.text("+28%", class_name="text-4xl font-bold text-white leading-tight"),
                    rx.text("Outperforming industry average by 6.4%", class_name="text-xs text-white/80 mt-1"),
                    class_name="backoffice-accent-card flex-1",
                ),
                columns="4",
                class_name="gap-4 mb-6",
            ),
            rx.grid(
                _monthly_revenue_chart(),
                _traffic_dist_chart(),
                columns="3",
                class_name="gap-6",
                style={"grid-template-columns": "2fr 1fr"},
            ),
        ),
    )

