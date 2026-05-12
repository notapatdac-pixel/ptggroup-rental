import reflex as rx

from component.backoffice.backoffice_layout import backoffice_layout


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


def _bar(height: str, muted: bool = False) -> rx.Component:
    cls = "backoffice-bar-muted" if muted else "backoffice-bar"
    return rx.box(class_name=f"{cls} w-5", style={"height": height})


def _revenue_trend_chart() -> rx.Component:
    bars_data = [
        ("40px", True), ("55px", False), ("48px", True), ("62px", False),
        ("50px", True), ("70px", False), ("58px", True), ("80px", False),
        ("65px", True), ("90px", False), ("72px", True), ("95px", False),
    ]
    bars = [_bar(h, m) for h, m in bars_data]
    return rx.box(
        rx.hstack(
            rx.text("Revenue Trend", class_name="text-base font-bold text-on-surface"),
            rx.hstack(
                rx.box(class_name="w-3 h-3 rounded-full bg-backoffice-primary"),
                rx.text("COFFEE CORNER", class_name="text-[10px] text-on-surface-variant"),
                rx.box(class_name="w-3 h-3 rounded-full bg-backoffice-bar-muted bg-[#d4d4c0]"),
                rx.text("QUICK MART", class_name="text-[10px] text-on-surface-variant"),
                class_name="flex items-center gap-2",
            ),
            class_name="flex justify-between items-center mb-4",
        ),
        rx.text("Performance by store", class_name="text-xs text-on-surface-variant mb-4"),
        rx.hstack(*bars, class_name="flex items-end gap-1.5 h-24"),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )


def _ai_tip_card() -> rx.Component:
    return rx.box(
        rx.text("AI INSIGHT", class_name="text-[10px] font-bold tracking-widest text-white/60 mb-2"),
        rx.text(
            "Coffee Corner is performing 15% above forecast.",
            class_name="text-sm font-bold text-white mb-2 leading-snug",
        ),
        rx.text(
            "Add seasonal menu items during 7–9am to capture high-density commuter traffic. Leveraging franchise incentives.",
            class_name="text-xs text-white/80 mb-4 leading-relaxed",
        ),
        rx.el.button(
            "Apply Suggested Strategy →",
            class_name="bg-white text-backoffice-primary text-xs font-bold px-4 py-2 rounded-lg border-0 cursor-pointer",
        ),
        class_name="backoffice-accent-card",
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


def _data_quality_donut() -> rx.Component:
    r = 36
    circ = 2 * 3.14159 * r
    fill = circ * 0.92
    return rx.box(
        rx.text("Data Quality Score", class_name="text-sm font-bold text-on-surface mb-3"),
        rx.el.svg(
            rx.el.circle(cx="44", cy="44", r=str(r), class_name="backoffice-donut-track", stroke_width="8"),
            rx.el.circle(
                cx="44", cy="44", r=str(r), class_name="backoffice-donut-fill",
                stroke_width="8",
                stroke_dasharray=f"{fill:.1f} {circ:.1f}",
                stroke_dashoffset=str(circ * 0.25),
                transform="rotate(-90 44 44)",
            ),
            rx.el.text("92%", x="44", y="48", text_anchor="middle", font_size="14", font_weight="700", fill="#2d5a1b"),
            width="88", height="88", view_box="0 0 88 88",
        ),
        rx.text("Optimal Health", class_name="text-xs text-on-surface-variant mt-2"),
        rx.el.button(
            "Submit Store Data",
            class_name="backoffice-btn-primary text-xs font-bold px-4 py-2 rounded-lg border-0 cursor-pointer w-full mt-3",
        ),
        class_name="backoffice-kpi-card",
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
                rx.box(class_name="flex-1"),
                columns="4",
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
                ),
                rx.box(
                    _ai_tip_card(),
                    _data_quality_donut(),
                    _traffic_distribution(),
                    class_name="flex flex-col gap-4",
                ),
                columns="2",
                class_name="gap-6",
            ),
        ),
    )
