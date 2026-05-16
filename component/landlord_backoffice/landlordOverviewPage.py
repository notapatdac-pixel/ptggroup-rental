import reflex as rx
from component.landlord_backoffice.landlord_layout import landlord_layout


def _kpi_card(label: str, value: str, icon: str, badge: str, sub: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text(label, class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1"),
                rx.text(value, class_name="text-3xl font-bold text-on-surface leading-tight"),
                rx.hstack(
                    rx.text(badge, class_name="text-xs font-bold text-backoffice-primary"),
                    rx.text(sub, class_name="text-[11px] text-on-surface-variant uppercase tracking-wide"),
                    class_name="flex items-center gap-1.5 mt-1 flex-wrap",
                ),
                class_name="flex-1",
            ),
            rx.el.span(icon, class_name="material-symbols-outlined text-[30px] text-outline-variant/60"),
            class_name="flex items-start justify-between gap-2",
        ),
        class_name="backoffice-kpi-card flex-1",
    )


_OV_REVENUE_DATA = [
    {"month": "JAN", "gross": 58, "net": 42},
    {"month": "FEB", "gross": 64, "net": 48},
    {"month": "MAR", "gross": 90, "net": 68},
    {"month": "APR", "gross": 82, "net": 62},
    {"month": "MAY", "gross": 112, "net": 85},
    {"month": "JUN", "gross": 76, "net": 56},
]


def _revenue_chart() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("Rental Revenue Trend", class_name="text-base font-bold text-on-surface"),
            rx.text("Monthly gross vs net (THB thousands)", class_name="text-xs text-on-surface-variant"),
            class_name="flex justify-between items-center mb-4",
        ),
        rx.recharts.responsive_container(
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False, stroke="#f0f0e8"),
                rx.recharts.x_axis(data_key="month"),
                rx.recharts.y_axis(width=30),
                rx.recharts.tooltip(),
                rx.recharts.legend(),
                rx.recharts.bar(data_key="gross", fill="#344e00", name="Gross", radius=4),
                rx.recharts.bar(data_key="net", fill="#96c93e", name="Net", radius=4),
                data=_OV_REVENUE_DATA,
                bar_category_gap="40%",
            ),
            width="100%",
            height=280,
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )


def _station_card(station: str, location: str, badge: str, badge_cls: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(station, class_name="text-sm font-bold text-on-surface"),
            rx.text(location, class_name="text-[11px] text-on-surface-variant mt-0.5"),
        ),
        rx.box(rx.text(badge, class_name=f"text-[11px] font-bold px-2.5 py-1 rounded-full {badge_cls}")),
        class_name="flex items-center justify-between py-3 border-b border-outline-variant/20 last:border-0",
    )


def _space_occupancy() -> rx.Component:
    return rx.box(
        rx.text("Space Occupancy", class_name="text-base font-bold text-on-surface mb-4"),
        _station_card("Sukhumvit 62", "Bang Chak, Bangkok", "8/10 Units", "bg-primary/10 text-primary"),
        _station_card("Lat Phrao 71", "Wang Thonglang, Bangkok", "10/10 Units", "bg-secondary/10 text-secondary"),
        _station_card("Rama IV", "Khlong Toei, Bangkok", "5/6 Units", "bg-primary/10 text-primary"),
        rx.link(
            "VIEW ALL ASSETS",
            href="/landlordstations",
            class_name="text-[11px] font-bold tracking-widest text-primary no-underline block text-center pt-3 hover:underline",
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm",
    )


def _score_bar(score: int) -> rx.Component:
    return rx.hstack(
        rx.text(str(score), class_name="text-sm font-bold text-on-surface w-6 flex-shrink-0"),
        rx.box(
            rx.box(class_name="backoffice-progress-fill h-full", style={"width": f"{score}%"}),
            class_name="backoffice-progress-track flex-1",
        ),
        class_name="flex items-center gap-2",
    )


def _app_row(name: str, sub: str, station: str, category: str, score: int, status: str) -> rx.Component:
    status_cls = "backoffice-chip-reviewing" if status == "Under Review" else "backoffice-chip-submitted"
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text(name[0].upper(), class_name="text-sm font-bold text-white"),
                class_name="w-8 h-8 rounded-full bg-primary flex items-center justify-center flex-shrink-0",
            ),
            rx.box(
                rx.text(name, class_name="text-sm font-semibold text-on-surface"),
                rx.text(sub, class_name="text-xs text-on-surface-variant"),
            ),
            class_name="flex items-center gap-3",
        ),
        rx.text(station, class_name="text-sm text-on-surface"),
        rx.box(
            rx.text(category, class_name="text-[10px] font-bold tracking-wide text-on-surface-variant border border-outline-variant rounded-full px-2 py-0.5"),
        ),
        _score_bar(score),
        rx.box(rx.text(status, class_name=status_cls)),
        rx.hstack(
            rx.box(
                rx.el.span("check_circle", class_name="material-symbols-outlined text-[22px] fill-icon text-secondary"),
                class_name="cursor-pointer",
            ),
            rx.box(
                rx.el.span("cancel", class_name="material-symbols-outlined text-[22px] fill-icon text-error"),
                class_name="cursor-pointer",
            ),
            class_name="flex items-center gap-2 justify-end",
        ),
        class_name="grid items-center gap-x-6 py-3 border-b border-outline-variant/20 last:border-0",
        style={"gridTemplateColumns": "2fr 1.5fr 1fr 1.2fr 1fr auto"},
    )


def _pending_applications() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading("Pending Applications", as_="h2",
                       class_name="text-xl font-bold font-headline italic text-on-surface"),
            rx.box(rx.text("4 NEW REQUESTS",
                           class_name="text-[11px] font-bold tracking-wide text-primary bg-primary/10 px-3 py-1 rounded-full")),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.box(
            rx.text("APPLICANT", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
            rx.text("PROPOSED STATION", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
            rx.text("CATEGORY", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
            rx.text("SCORE", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
            rx.text("STATUS", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
            rx.text("ACTIONS", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
            class_name="grid items-center gap-x-6 pb-2 border-b border-outline-variant/20",
            style={"gridTemplateColumns": "2fr 1.5fr 1fr 1.2fr 1fr auto"},
        ),
        _app_row("Artisan Brew Co.", "Kasemsawat S.", "Sukhumvit 62 (B-04)", "FOOD & BEVERAGE", 92, "Under Review"),
        _app_row("PureHealth Pharma", "Nongnooch T.", "Rama IV (C-02)", "WELLNESS", 88, "In Verification"),
        class_name="bg-white rounded-2xl p-6 shadow-sm mt-6",
    )


def _fab() -> rx.Component:
    return rx.box(
        rx.el.span("add", class_name="material-symbols-outlined text-white text-[24px]"),
        class_name=(
            "fixed bottom-8 right-8 w-14 h-14 rounded-full backoffice-btn-primary "
            "flex items-center justify-center cursor-pointer shadow-lg z-30"
        ),
    )


def landlord_overview_page_content() -> rx.Component:
    return landlord_layout(
        "overview",
        rx.box(
            rx.hstack(
                rx.box(
                    rx.heading("Executive Overview", as_="h1",
                               class_name="text-3xl font-bold font-headline italic text-on-surface"),
                    rx.hstack(
                        rx.text("Welcome back, your retail ecosystem is performing ",
                                class_name="text-sm text-on-surface-variant"),
                        rx.text("12% above benchmark", class_name="text-sm font-bold text-primary"),
                        rx.text(" this month.", class_name="text-sm text-on-surface-variant"),
                        class_name="flex items-center flex-wrap gap-0 mt-1",
                    ),
                ),
                rx.hstack(
                    rx.el.button(
                        "Last 30 Days",
                        class_name="bg-white border border-outline-variant/40 rounded-full px-4 py-2 cursor-pointer text-on-surface text-sm",
                    ),
                    rx.el.button(
                        rx.hstack(
                            rx.el.span("download", class_name="material-symbols-outlined text-[16px]"),
                            rx.text("Export", class_name="text-sm font-medium"),
                            class_name="flex items-center gap-1",
                        ),
                        class_name="bg-white border border-outline-variant/40 rounded-full px-4 py-2 cursor-pointer text-on-surface",
                    ),
                    class_name="flex items-center gap-3",
                ),
                class_name="flex items-start justify-between mb-6",
            ),
            rx.grid(
                _kpi_card("Total Revenue", "฿4.2M", "attach_money", "+8.4%", "VS LAST MONTH"),
                _kpi_card("Occupancy", "94.2%", "apartment", "Optimal", "2 UNITS VACANT"),
                _kpi_card("Pending Reviews", "12", "pending_actions", "4 Urgent", "EXPIRING SOON"),
                _kpi_card("Active Tenants", "7", "groups", "+1 this month", "ACTIVE LEASES"),
                columns="4",
                class_name="gap-4 mb-6",
            ),
            rx.grid(
                _revenue_chart(),
                _space_occupancy(),
                columns="2",
                class_name="gap-6 mb-6",
            ),
            _pending_applications(),
            _fab(),
        ),
    )
