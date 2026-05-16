import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout


def _bar_group(h_predicted: str, h_conservative: str, h_optimistic: str) -> rx.Component:
    return rx.hstack(
        rx.box(class_name="backoffice-bar w-7", style={"height": h_predicted}),
        rx.box(class_name="backoffice-bar w-7", style={"height": h_conservative, "background-color": "#2d5a1b"}),
        rx.box(class_name="backoffice-bar-muted w-7", style={"height": h_optimistic}),
        class_name="flex items-end gap-0.5",
    )


def _quarterly_chart() -> rx.Component:
    months = ["JAN", "FEB", "MAR", "APR"]
    groups = [
        ("65px", "40px", "30px"),
        ("80px", "50px", "38px"),
        ("95px", "60px", "45px"),
        ("72px", "45px", "35px"),
    ]
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("Quarterly Forecast", class_name="text-xl font-bold text-backoffice-primary font-headline italic"),
                rx.text("Analysis", class_name="text-xl font-bold text-backoffice-primary font-headline italic"),
            ),
            rx.hstack(
                rx.box(class_name="w-3 h-3 rounded-full bg-[#4a7c2f]"),
                rx.text("Predicted", class_name="text-xs text-on-surface-variant"),
                rx.box(class_name="w-3 h-3 rounded-full bg-[#2d5a1b]"),
                rx.text("Conservative", class_name="text-xs text-on-surface-variant"),
                rx.box(class_name="w-3 h-3 rounded-full bg-[#d4d4c0]"),
                rx.text("Optimistic", class_name="text-xs text-on-surface-variant"),
                class_name="flex items-center gap-2",
            ),
            class_name="flex justify-between items-start mb-6",
        ),
        rx.hstack(
            *[
                rx.vstack(
                    _bar_group(*g),
                    rx.text(m, class_name="text-[9px] font-bold text-on-surface-variant tracking-wider"),
                    class_name="flex flex-col items-center gap-1",
                )
                for g, m in zip(groups, months)
            ],
            class_name="flex items-end gap-8 h-28",
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm flex-1",
    )


def _velocity_marker(region: str, value: str, pct: int) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(region, class_name="text-sm text-on-surface flex-1"),
            rx.text(value, class_name="text-sm font-bold text-on-surface"),
            class_name="flex items-center mb-1",
        ),
        rx.box(
            rx.box(class_name="backoffice-progress-fill", style={"width": f"{pct}%"}),
            class_name="backoffice-progress-track",
        ),
        class_name="w-full mb-3",
    )


def _regional_velocity() -> rx.Component:
    return rx.box(
        rx.text("Regional Velocity", class_name="text-base font-bold text-backoffice-primary font-headline italic mb-4"),
        rx.text("Markers", class_name="text-base font-bold text-backoffice-primary font-headline italic -mt-3 mb-4"),
        _velocity_marker("Bangkok Metropolis", "8.4x", 84),
        _velocity_marker("Eastern Seaboard", "6.2x", 62),
        _velocity_marker("Chiang Mai Cluster", "4.9x", 49),
        _velocity_marker("Southern Tourism Hubs", "7.1x", 71),
        rx.box(
            rx.text("Regional Velocity", class_name="text-xs font-bold text-backoffice-primary mb-1"),
            rx.text(
                "Measures the speed of market penetration and repeat customer acquisition relative to national averages. Values above 5.0x indicate high potential for franchise expansion.",
                class_name="text-xs text-on-surface-variant leading-relaxed",
            ),
            class_name="bg-surface-container-low rounded-xl p-4 mt-2",
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
            rx.grid(
                _quarterly_chart(),
                _regional_velocity(),
                columns="2",
                class_name="gap-6",
                style={"grid-template-columns": "2fr 1fr"},
            ),
        ),
    )

