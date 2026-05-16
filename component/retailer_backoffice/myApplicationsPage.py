import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout

_STEP_DATA = [
    ("SUBMITTED",  "check",          0),
    ("REVIEWING",  "fact_check",     1),
    ("APPROVED",   "verified",       2),
    ("BOOKING",    "calendar_today", 3),
]


def _progress_node(icon: str, done: bool, active: bool) -> rx.Component:
    if done:
        return rx.box(
            rx.el.span("check", class_name="material-symbols-outlined text-white text-base"),
            class_name="w-9 h-9 rounded-full bg-backoffice-primary flex items-center justify-center flex-shrink-0",
        )
    if active:
        return rx.box(
            rx.el.span(icon, class_name="material-symbols-outlined text-backoffice-primary text-base"),
            class_name=(
                "w-9 h-9 rounded-full border-2 border-backoffice-primary bg-white "
                "flex items-center justify-center flex-shrink-0"
            ),
        )
    return rx.box(
        rx.el.span(icon, class_name="material-symbols-outlined text-on-surface-variant/30 text-base"),
        class_name=(
            "w-9 h-9 rounded-full border-2 border-outline-variant/20 "
            "flex items-center justify-center flex-shrink-0"
        ),
    )


def _progress_track(step: int) -> rx.Component:
    items = []
    for i, (label, icon, idx) in enumerate(_STEP_DATA):
        done   = idx < step
        active = idx == step
        node = rx.box(
            _progress_node(icon, done, active),
            rx.text(
                label,
                class_name=(
                    "text-[9px] font-bold tracking-widest uppercase mt-2 text-center "
                    + ("text-backoffice-primary" if (done or active) else "text-on-surface-variant/30")
                ),
            ),
            class_name="flex flex-col items-center",
        )
        items.append(node)
        if i < len(_STEP_DATA) - 1:
            line_cls = "bg-backoffice-primary" if idx < step else "bg-outline-variant/20"
            items.append(rx.box(class_name=f"flex-1 h-0.5 self-start mt-[18px] {line_cls}"))

    return rx.hstack(
        *items,
        class_name="flex items-start w-full border-t border-outline-variant/10 pt-4 mt-5",
    )


def _application_card(
    station: str,
    location: str,
    store_type: str,
    lease: str,
    date: str,
    step: int,
    image: str = "",
) -> rx.Component:
    return rx.box(
        rx.hstack(
            # ── Left image panel ─────────────────────────────────────────
            rx.box(
                rx.box(
                    rx.hstack(
                        rx.box(class_name="w-1.5 h-1.5 rounded-full bg-[#96c93e]"),
                        rx.text("Active Application", class_name="text-xs font-semibold text-white"),
                        class_name="flex items-center gap-1.5",
                    ),
                    class_name=(
                        "absolute top-3 left-3 z-10 bg-[#2d5a1b]/75 backdrop-blur-sm "
                        "px-3 py-1.5 rounded-full"
                    ),
                ),
                class_name="relative flex-shrink-0 overflow-hidden rounded-l-2xl",
                style={
                    "width": "230px",
                    "background": f"url('{image}') center/cover no-repeat" if image else "#e8eddc",
                    "min_height": "200px",
                },
            ),
            # ── Right content panel ───────────────────────────────────────
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.text(station, class_name="text-xl font-bold text-on-surface mb-1"),
                        rx.hstack(
                            rx.el.span("location_on", class_name="material-symbols-outlined text-sm text-on-surface-variant"),
                            rx.text(location, class_name="text-sm text-on-surface-variant"),
                            class_name="flex items-center gap-0.5",
                        ),
                    ),
                    rx.box(
                        rx.text("APPLIED DATE", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                        rx.text(date, class_name="text-base font-bold text-on-surface"),
                        class_name="text-right flex-shrink-0",
                    ),
                    class_name="flex justify-between items-start mb-4",
                ),
                rx.grid(
                    rx.box(
                        rx.text("SPACE TYPE", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-1"),
                        rx.text(store_type, class_name="text-sm font-semibold text-on-surface"),
                        class_name="border border-outline-variant/30 rounded-lg p-3 bg-surface-container-low/30",
                    ),
                    rx.box(
                        rx.text("LEASE TERM", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-1"),
                        rx.text(lease, class_name="text-sm font-semibold text-on-surface"),
                        class_name="border border-outline-variant/30 rounded-lg p-3 bg-surface-container-low/30",
                    ),
                    columns="2",
                    class_name="gap-3",
                ),
                _progress_track(step),
                class_name="flex-1 p-6 flex flex-col",
            ),
            class_name="flex items-stretch",
        ),
        class_name="bg-white rounded-2xl shadow-sm overflow-hidden w-full",
    )


def my_applications_page_content() -> rx.Component:
    return backoffice_layout(
        "applications",
        rx.box(
            rx.box(
                rx.heading("My Applications", as_="h1", class_name="text-2xl font-bold text-on-surface"),
                rx.text(
                    "Track and manage your retail space applications across premium locations.",
                    class_name="text-sm text-on-surface-variant mt-1",
                ),
                class_name="mb-6",
            ),
            rx.box(
                _application_card(
                    station="Rama 9 Station - Retail",
                    location="Bangkok, Thailand",
                    store_type="Premium Kiosk (12sqm)",
                    lease="24 Months",
                    date="Oct 24, 2023",
                    step=2,
                    image="/image/station-ptg-ramaix.png",
                ),
                _application_card(
                    station="Sukhumvit Prime",
                    location="Sukhumvit, Bangkok",
                    store_type="Pop-up Corner (8sqm)",
                    lease="6 Months",
                    date="Nov 12, 2023",
                    step=1,
                    image="/image/station-ptg-bangna.png",
                ),
                class_name="flex flex-col gap-4 w-full",
            ),
            class_name="w-full",
        ),
    )
