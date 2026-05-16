import reflex as rx
from component.landlord_backoffice.landlord_layout import landlord_layout


def _summary_card(icon: str, label: str, value: str, sub: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.span(icon, class_name="material-symbols-outlined text-[22px] text-on-surface-variant"),
            class_name="w-10 h-10 bg-surface-container rounded-xl flex items-center justify-center mb-3",
        ),
        rx.text(label, class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1"),
        rx.text(value, class_name="text-3xl font-bold text-on-surface"),
        rx.text(sub, class_name="text-xs text-backoffice-primary font-bold mt-1"),
        class_name="backoffice-kpi-card flex-1",
    )


def _avatar(letter: str, color: str) -> rx.Component:
    return rx.box(
        rx.text(letter, class_name="text-sm font-bold text-white"),
        class_name="w-9 h-9 rounded-full flex items-center justify-center flex-shrink-0",
        style={"backgroundColor": color},
    )


def _tenant_row(
    letter: str, color: str, name: str, sub: str,
    btype: str, station: str, unit: str,
    rent: str,
    expiry: str, months: str, urgent: bool = False,
) -> rx.Component:
    expiry_cls = "text-sm font-bold text-error" if urgent else "text-sm font-bold text-on-surface"
    months_cls = "text-xs text-error font-semibold" if urgent else "text-xs text-on-surface-variant"
    months_label = "Renewing Soon" if urgent else months
    return rx.box(
        rx.hstack(
            _avatar(letter, color),
            rx.box(
                rx.text(name, class_name="text-sm font-bold text-on-surface"),
                rx.text(sub, class_name="text-xs text-on-surface-variant"),
            ),
            class_name="flex items-center gap-3",
        ),
        rx.box(rx.text(btype, class_name="backoffice-chip-reviewing")),
        rx.box(
            rx.text(station, class_name="text-sm font-semibold text-on-surface"),
            rx.text(unit, class_name="text-xs text-on-surface-variant"),
        ),
        rx.text(f"฿{rent}/mo", class_name="text-sm font-bold text-on-surface"),
        rx.box(
            rx.text(expiry, class_name=expiry_cls),
            rx.text(months_label, class_name=months_cls),
        ),
        class_name="grid items-center gap-x-6 py-4 border-b border-outline-variant/20 last:border-0",
        style={"gridTemplateColumns": "2fr 1fr 1.5fr 1.5fr 1.5fr"},
    )


def _fab() -> rx.Component:
    return rx.box(
        rx.el.span("add", class_name="material-symbols-outlined text-white text-[24px]"),
        class_name=(
            "fixed bottom-8 right-8 w-14 h-14 rounded-full backoffice-btn-primary "
            "flex items-center justify-center cursor-pointer shadow-lg z-30"
        ),
    )


def landlord_tenants_page_content() -> rx.Component:
    return landlord_layout(
        "tenants",
        rx.box(
            rx.hstack(
                rx.heading("Active Tenants", as_="h1", class_name="text-2xl font-bold text-on-surface"),
                rx.el.button(
                    rx.hstack(
                        rx.el.span("download", class_name="material-symbols-outlined text-[16px]"),
                        rx.text("Export Report", class_name="text-sm font-bold"),
                        class_name="flex items-center gap-1.5",
                    ),
                    class_name="backoffice-btn-primary border-0 rounded-full px-5 py-2.5 cursor-pointer",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.grid(
                _summary_card("groups", "Total Tenants", "7", "+1 this month"),
                _summary_card("event", "Upcoming Renewals", "2", "This quarter"),
                columns="2",
                class_name="gap-4 mb-8",
            ),
            rx.box(
                rx.hstack(
                    rx.text("Lease Registry", class_name="text-lg font-bold text-on-surface"),
                    rx.hstack(
                        rx.text("Filter by type...", class_name="text-sm text-on-surface-variant"),
                        rx.el.span("expand_more", class_name="material-symbols-outlined text-[18px] text-on-surface-variant"),
                        class_name="flex items-center gap-1 bg-surface-container-low rounded-full px-4 py-2 cursor-pointer",
                    ),
                    class_name="flex items-center justify-between mb-4",
                ),
                rx.box(
                    rx.text("TENANT NAME", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
                    rx.text("BUSINESS TYPE", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
                    rx.text("STATION / UNIT", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
                    rx.text("MONTHLY RENT", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
                    rx.text("LEASE EXPIRY", class_name="text-[10px] font-bold tracking-widest text-on-surface-variant"),
                    class_name="grid items-center gap-x-6 pb-3 border-b border-outline-variant/20",
                    style={"gridTemplateColumns": "2fr 1fr 1.5fr 1.5fr 1.5fr"},
                ),
                _tenant_row(
                    "B", "#466800", "Bean & Uoast Co.", "Coffee & Bakery",
                    "Quick-Service", "PTG Main Station", "Unit A-12",
                    "124,000", "Oct 12, 2025", "18 months left",
                ),
                _tenant_row(
                    "E", "#737a66", "Eco-Mart Express", "Retail",
                    "Convenience", "PTG West Bypass", "Unit B-04",
                    "42,000", "May 30, 2024", "Renewing Soon", urgent=True,
                ),
                _tenant_row(
                    "S", "#006e2d", "Sparkle Detailing", "Automotive Services",
                    "Service", "PTG North Hub", "Bay 02",
                    "88,000", "Jan 15, 2026", "21 months left",
                ),
                _tenant_row(
                    "G", "#96388e", "Green Garden Florals", "Retail",
                    "Boutique", "PTG Main Station", "Unit C-01",
                    "36,000", "July 04, 2025", "15 months left",
                ),
                rx.hstack(
                    rx.text("Showing 1 to 7 of 7 tenants",
                            class_name="text-sm text-on-surface-variant flex-1"),
                    rx.hstack(
                        rx.box(
                            rx.el.span("chevron_left", class_name="material-symbols-outlined text-[18px] text-on-surface-variant"),
                            class_name="w-8 h-8 flex items-center justify-center rounded-lg border border-outline-variant cursor-pointer",
                        ),
                        rx.box(
                            rx.text("1", class_name="text-sm font-bold text-white"),
                            class_name="w-8 h-8 flex items-center justify-center rounded-lg bg-primary cursor-pointer",
                        ),
                        rx.box(
                            rx.el.span("chevron_right", class_name="material-symbols-outlined text-[18px] text-on-surface-variant"),
                            class_name="w-8 h-8 flex items-center justify-center rounded-lg border border-outline-variant cursor-pointer",
                        ),
                        class_name="flex items-center gap-1",
                    ),
                    class_name="flex items-center justify-between mt-4 pt-4 border-t border-outline-variant/20",
                ),
                class_name="bg-white rounded-2xl p-6 shadow-sm",
            ),
            _fab(),
        ),
    )
