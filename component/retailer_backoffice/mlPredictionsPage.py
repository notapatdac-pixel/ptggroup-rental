import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout


_QUARTERLY_DATA = [
    {"month": "JAN", "predicted": 65, "conservative": 40, "optimistic": 30},
    {"month": "FEB", "predicted": 80, "conservative": 50, "optimistic": 38},
    {"month": "MAR", "predicted": 95, "conservative": 60, "optimistic": 45},
    {"month": "APR", "predicted": 72, "conservative": 45, "optimistic": 35},
]


def _quarterly_chart() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("Quarterly Forecast Analysis", class_name="text-xl font-bold text-backoffice-primary font-headline italic"),
                rx.text("Revenue projections across three confidence scenarios (THB millions)", class_name="text-xs text-on-surface-variant mt-1"),
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
                rx.recharts.bar(data_key="predicted", fill="#466800", name="Predicted", radius=4),
                rx.recharts.bar(data_key="conservative", fill="#2d5a1b", name="Conservative", radius=4),
                rx.recharts.bar(data_key="optimistic", fill="#c8d4b0", name="Optimistic", radius=4),
                data=_QUARTERLY_DATA,
                bar_category_gap="35%",
            ),
            width="100%",
            height=380,
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )



def _donut_accuracy() -> rx.Component:
    r = 38
    circ = 2 * 3.14159 * r
    fill = circ * 0.942
    return rx.box(
        rx.el.svg(
            rx.el.circle(cx="46", cy="46", r=str(r), class_name="backoffice-donut-track", stroke_width="8"),
            rx.el.circle(
                cx="46", cy="46", r=str(r), class_name="backoffice-donut-fill",
                stroke_width="8",
                stroke_dasharray=f"{fill:.1f} {circ:.1f}",
                stroke_dashoffset=str(circ * 0.25),
                transform="rotate(-90 46 46)",
            ),
            rx.el.text("94%", x="46", y="50", text_anchor="middle", font_size="13", font_weight="700", fill="#2d5a1b"),
            width="92", height="92", view_box="0 0 92 92",
        ),
        rx.text("MODEL ACCURACY", class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mt-2"),
        rx.text("94.2%", class_name="text-xl font-bold text-on-surface"),
        rx.text("Variance: ±0.8%", class_name="text-xs text-on-surface-variant"),
        class_name="bg-white rounded-2xl p-5 shadow-sm flex flex-col items-center",
    )


def ml_predictions_page_content() -> rx.Component:
    return backoffice_layout(
        "ml_predictions",
        rx.box(
            rx.hstack(
                rx.box(
                    rx.heading("ML Growth Intelligence", as_="h1", class_name="text-2xl font-bold text-backoffice-primary"),
                    rx.text("Predictive modeling for retail expansion and quarterly revenue optimization.", class_name="text-sm text-on-surface-variant mt-1"),
                ),
                rx.hstack(
                    rx.el.button(
                        rx.hstack(rx.el.span("refresh", class_name="material-symbols-outlined text-base"), rx.text("Refresh", class_name="text-sm font-bold"), class_name="flex items-center gap-1.5"),
                        class_name="bg-white border border-outline-variant/40 rounded-full px-4 py-2 cursor-pointer hover:bg-surface-container-low",
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
                rx.box(
                    rx.text("NEXT MONTH FORECAST", class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-2"),
                    rx.hstack(
                        rx.text("$4.2M", class_name="text-3xl font-bold text-on-surface"),
                        rx.box(rx.text("+12.4%", class_name="text-xs font-bold text-backoffice-primary"), class_name="backoffice-chip-reviewing ml-2"),
                        class_name="flex items-center",
                    ),
                    rx.box(
                        rx.box(class_name="backoffice-progress-fill", style={"width": "70%"}),
                        class_name="backoffice-progress-track mt-2 mb-1",
                    ),
                    rx.text("Trending above seasonal baseline", class_name="text-xs text-on-surface-variant"),
                    class_name="backoffice-kpi-card flex-1",
                ),
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.text("Q2 PROJECTED REVENUE", class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-2"),
                            rx.text("$18.9M", class_name="text-3xl font-bold text-on-surface"),
                            rx.text("Est. Range: $17M–$20M", class_name="text-xs text-on-surface-variant mt-1"),
                            rx.box(
                                rx.box(class_name="backoffice-progress-fill", style={"width": "60%"}),
                                class_name="backoffice-progress-track mt-2 mb-1",
                            ),
                            rx.text("Confidence level: High (89%)", class_name="text-xs text-on-surface-variant"),
                        ),
                        rx.el.span("trending_up", class_name="material-symbols-outlined text-backoffice-primary text-2xl ml-auto"),
                        class_name="flex items-start w-full",
                    ),
                    class_name="backoffice-kpi-card flex-2",
                ),
                _donut_accuracy(),
                columns="3",
                class_name="gap-4 mb-6",
            ),
            _quarterly_chart(),
        ),
    )

