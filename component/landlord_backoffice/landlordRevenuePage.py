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


def _dual_bar(gross_h: int, net_h: int, label: str) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(class_name="w-4 rounded-t-sm", style={"height": f"{gross_h}px", "backgroundColor": "#e1e3e2", "alignSelf": "flex-end"}),
            rx.box(class_name="w-4 rounded-t-sm", style={"height": f"{net_h}px", "backgroundColor": "#96c93e", "alignSelf": "flex-end"}),
            class_name="flex items-end gap-0.5",
        ),
        rx.text(label, class_name="text-[9px] text-on-surface-variant mt-1"),
        class_name="flex flex-col items-center gap-0",
    )


def _revenue_chart() -> rx.Component:
    days = [
        ("MON", 38, 20), ("TUE", 42, 28), ("WED", 50, 35),
        ("THU", 70, 55), ("FRI", 65, 48), ("SAT", 55, 40), ("SUN", 30, 18),
    ]
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("Filtered Revenue Trends", class_name="text-base font-bold text-on-surface"),
                rx.text("Daily yield tracking across all primary corridors",
                        class_name="text-xs text-on-surface-variant mt-0.5"),
            ),
            rx.hstack(
                rx.box(class_name="w-2.5 h-2.5 rounded-full", style={"backgroundColor": "#e1e3e2"}),
                rx.text("GROSS YIELD", class_name="text-[10px] text-on-surface-variant"),
                rx.box(class_name="w-2.5 h-2.5 rounded-full", style={"backgroundColor": "#96c93e"}),
                rx.text("NET PROFIT", class_name="text-[10px] text-on-surface-variant"),
                class_name="flex items-center gap-1.5",
            ),
            class_name="flex justify-between items-start mb-5",
        ),
        rx.hstack(
            *[_dual_bar(g, n, d) for d, g, n in days],
            class_name="flex items-end gap-4",
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )


def _dist_row(label: str, pct: int) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(label, class_name="text-[11px] font-bold text-on-surface-variant flex-1"),
            rx.text(f"{pct}%", class_name="text-[11px] font-bold text-on-surface"),
            class_name="flex items-center mb-1.5",
        ),
        rx.box(
            rx.box(class_name="backoffice-progress-fill h-full", style={"width": f"{pct}%"}),
            class_name="backoffice-progress-track",
        ),
        class_name="mb-3 last:mb-0",
    )


def _space_distribution() -> rx.Component:
    return rx.box(
        rx.text("Space Distribution", class_name="text-base font-bold text-on-surface mb-1"),
        rx.text("Monthly contribution by unit type", class_name="text-xs text-on-surface-variant mb-4"),
        _dist_row("ANCHOR RETAIL", 42),
        _dist_row("BOUTIQUE UNITS", 28),
        _dist_row("POPUP / KIOSKS", 18),
        _dist_row("DINING TERRACE", 12),
        rx.box(
            rx.text("PORTFOLIO HEALTH", class_name="text-[9px] font-bold tracking-widest text-on-surface-variant mb-1"),
            rx.text("Low exposure to anchor churn; strong boutique growth.",
                    class_name="text-xs text-on-surface-variant leading-relaxed"),
            class_name="bg-surface-container-low rounded-xl p-4 mt-4",
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )


def _event_row(month: str, day: str, title: str, sub: str, accent: bool = False) -> rx.Component:
    border_cls = "border-l-4 border-primary" if accent else "border-l-4 border-transparent"
    return rx.hstack(
        rx.box(
            rx.text(month, class_name="text-[9px] font-bold text-on-surface-variant text-center"),
            rx.text(day, class_name="text-lg font-bold text-on-surface text-center leading-tight"),
            class_name="w-10 flex-shrink-0 text-center",
        ),
        rx.box(
            rx.text(title, class_name="text-sm font-semibold text-on-surface"),
            rx.text(sub, class_name="text-xs text-on-surface-variant"),
            class_name="flex-1",
        ),
        rx.el.span("arrow_forward", class_name="material-symbols-outlined text-[18px] text-on-surface-variant"),
        class_name=f"flex items-center gap-3 py-3 pl-3 pr-2 border-b border-outline-variant/20 last:border-0 {border_cls}",
    )


def _upcoming_events() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("Upcoming Events", class_name="text-base font-bold text-on-surface"),
            rx.link("View Calendar", href="#",
                    class_name="text-sm font-bold text-primary no-underline hover:underline"),
            class_name="flex justify-between items-center mb-2",
        ),
        _event_row("OCT", "12", "Rent due: Global Coffee Co.", "Auto-payment scheduled for unit A-12"),
        _event_row("OCT", "15", "Lease review: Modish Wear", "Term expires in 60 days. Initial review set."),
        _event_row("OCT", "18", "Maintenance check: HVAC Unit 4", "Quarterly inspection for South Wing", accent=True),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )


def _map_panel() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.hstack(
                    rx.box(class_name="w-2 h-2 rounded-full bg-secondary animate-pulse"),
                    rx.text("LIVE UPDATES", class_name="text-[10px] font-bold tracking-widest text-secondary"),
                    class_name="flex items-center gap-1.5",
                ),
                rx.text("Station Coverage", class_name="text-sm font-bold text-on-surface"),
                rx.text("Northside & Downtown Corridor", class_name="text-xs text-on-surface-variant"),
                class_name="absolute bottom-4 left-4 bg-white/90 backdrop-blur-sm rounded-xl p-3",
            ),
            class_name="relative w-full h-full",
        ),
        class_name="bg-inverse-surface rounded-2xl overflow-hidden relative",
        style={"minHeight": "250px"},
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
                _kpi_card("This Month", "142,500", "~12%", "vs. Last Month (127k)"),
                _kpi_card("YTD Revenue", "1.24M", "~4.2%", "vs. Projections (1.19M)"),
                _kpi_card("Avg Per Space", "3,840", "~-0.8%", "Market Avg: 3,660", positive=False),
                _kpi_card("Occupancy", "94.2%", "", "Active: 48 / 51 Spaces", has_check=True),
                columns="4",
                class_name="gap-4 mb-6",
            ),
            rx.grid(
                _revenue_chart(),
                _space_distribution(),
                columns="3",
                class_name="gap-6 mb-6",
                style={"gridTemplateColumns": "2fr 1fr"},
            ),
            rx.grid(
                _upcoming_events(),
                _map_panel(),
                columns="2",
                class_name="gap-6",
            ),
        ),
    )
