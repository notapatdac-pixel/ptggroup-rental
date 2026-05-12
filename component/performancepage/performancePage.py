import reflex as rx

from component.backoffice.backoffice_layout import backoffice_layout


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


def _bar(height: str, muted: bool = False) -> rx.Component:
    cls = "backoffice-bar-muted" if muted else "backoffice-bar"
    return rx.box(class_name=f"{cls} w-8", style={"height": height})


def _monthly_revenue_chart() -> rx.Component:
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN"]
    pairs = [
        ("55px", "40px"), ("65px", "45px"), ("58px", "42px"),
        ("72px", "50px"), ("68px", "48px"), ("90px", "55px"),
    ]
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("Monthly Revenue by Store", class_name="text-base font-bold text-on-surface"),
                rx.text("Comparative analysis across core retail units", class_name="text-xs text-on-surface-variant"),
            ),
            rx.hstack(
                rx.box(class_name="w-3 h-3 rounded-full bg-backoffice-primary"),
                rx.text("Coffee Corner", class_name="text-xs text-on-surface-variant"),
                rx.box(class_name="w-3 h-3 rounded-full bg-[#d4d4c0]"),
                rx.text("Quick Mart", class_name="text-xs text-on-surface-variant"),
                class_name="flex items-center gap-2",
            ),
            class_name="flex justify-between items-start mb-6",
        ),
        rx.hstack(
            *[
                rx.vstack(
                    rx.hstack(
                        _bar(h1),
                        _bar(h2, muted=True),
                        class_name="flex items-end gap-1",
                    ),
                    rx.text(m, class_name="text-[9px] font-bold text-on-surface-variant tracking-wider"),
                    class_name="flex flex-col items-center gap-1",
                )
                for (h1, h2), m in zip(pairs, months)
            ],
            class_name="flex items-end gap-6 h-24",
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
            class_name="mt-6 bg-surface-container-low rounded-xl p-4",
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )


def _efficiency_pulse() -> rx.Component:
    metrics = [
        ("Revenue vs Predicted", "118%", 100),
        ("Customer Volume", "105%", 86),
        ("Average Spend", "96%", 76),
        ("Repeat Visit Rate", "112%", 92),
    ]
    return rx.box(
        rx.hstack(
            rx.text("Efficiency Pulse", class_name="text-sm font-bold text-on-surface"),
            rx.el.span("bolt", class_name="material-symbols-outlined text-backoffice-primary text-base"),
            class_name="flex items-center gap-1 mb-4",
        ),
        rx.vstack(
            *[
                rx.box(
                    rx.hstack(
                        rx.text(label, class_name="text-xs text-on-surface-variant flex-1"),
                        rx.text(val, class_name="text-xs font-bold text-on-surface"),
                        class_name="flex items-center mb-1",
                    ),
                    rx.box(
                        rx.box(class_name="backoffice-progress-fill", style={"width": f"{pct}%"}),
                        class_name="backoffice-progress-track",
                    ),
                    class_name="w-full",
                )
                for label, val, pct in metrics
            ],
            class_name="gap-3 w-full",
        ),
        class_name="backoffice-kpi-card",
    )


def _traffic_dist_chart() -> rx.Component:
    bars = [("MON", "35px", True), ("TUE", "42px", True), ("WED", "38px", True),
            ("THU", "50px", True), ("FRI", "55px", True), ("SAT", "90px", False), ("SUN", "40px", True)]
    return rx.box(
        rx.text("Traffic Distribution", class_name="text-sm font-bold text-on-surface mb-1"),
        rx.text("Weekly yield distribution by volume", class_name="text-xs text-on-surface-variant mb-4"),
        rx.hstack(
            *[
                rx.vstack(
                    rx.box(class_name=f"{'backoffice-bar' if not m else 'backoffice-bar-muted'} w-7", style={"height": h}),
                    rx.text(day, class_name="text-[9px] text-on-surface-variant"),
                    class_name="flex flex-col items-center gap-1",
                )
                for day, h, m in bars
            ],
            class_name="flex items-end gap-1 h-24",
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
                rx.box(
                    _efficiency_pulse(),
                    _traffic_dist_chart(),
                    class_name="flex flex-col gap-4",
                ),
                columns="3",
                class_name="gap-6",
                style={"grid-template-columns": "2fr 1fr"},
            ),
        ),
    )
