import reflex as rx

from component.backoffice.backoffice_layout import backoffice_layout


def _progress_step(label: str, done: bool, active: bool = False) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.el.span(
                "check" if done else ("radio_button_checked" if active else "radio_button_unchecked"),
                class_name=f"material-symbols-outlined text-sm {'text-backoffice-primary' if (done or active) else 'text-on-surface-variant/30'}",
            ),
            class_name="w-5 h-5 flex items-center justify-center",
        ),
        rx.text(label, class_name=f"text-[10px] font-bold tracking-widest uppercase {'text-backoffice-primary' if (done or active) else 'text-on-surface-variant/40'}"),
        class_name="flex items-center gap-1",
    )


def _application_card(
    station: str,
    location: str,
    store_type: str,
    lease: str,
    date: str,
    status_label: str,
    status_type: str,
    step: int,
) -> rx.Component:
    steps = ["SUBMITTED", "REVIEWING", "APPROVED", "BOOKING"]
    return rx.box(
        rx.hstack(
            rx.box(
                rx.el.span("location_city", class_name="material-symbols-outlined text-on-surface-variant text-3xl"),
                class_name="w-32 h-24 bg-surface-container-high rounded-xl flex items-center justify-center flex-shrink-0",
            ),
            rx.box(
                rx.hstack(
                    rx.box(rx.text(status_label, class_name=f"backoffice-chip-{status_type}")),
                    rx.text(f"Application Date: {date}", class_name="text-xs text-on-surface-variant"),
                    class_name="flex items-center gap-3 mb-1",
                ),
                rx.text(station, class_name="text-base font-bold text-on-surface mb-0.5"),
                rx.hstack(
                    rx.el.span("location_on", class_name="material-symbols-outlined text-[14px] text-on-surface-variant"),
                    rx.text(location, class_name="text-xs text-on-surface-variant"),
                    class_name="flex items-center gap-1 mb-3",
                ),
                rx.hstack(
                    rx.box(
                        rx.text("STORE TYPE", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                        rx.text(store_type, class_name="text-xs font-semibold text-on-surface"),
                    ),
                    rx.box(
                        rx.text("LEASE TERM", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                        rx.text(lease, class_name="text-xs font-semibold text-on-surface"),
                    ),
                    class_name="flex gap-8",
                ),
            ),
            rx.box(
                rx.hstack(
                    *[
                        rx.hstack(
                            _progress_step(s, i < step, i == step),
                            rx.box(class_name="w-8 h-px bg-outline-variant/30") if i < len(steps) - 1 else rx.fragment(),
                            class_name="flex items-center",
                        )
                        for i, s in enumerate(steps)
                    ],
                    class_name="flex items-center",
                ),
                rx.hstack(
                    rx.el.button(
                        rx.el.span("calendar_today", class_name="material-symbols-outlined text-sm"),
                        class_name="bg-transparent border border-outline-variant/40 rounded-lg p-1.5 cursor-pointer hover:bg-surface-container-low",
                    ),
                    rx.el.button(
                        rx.el.span("description", class_name="material-symbols-outlined text-sm"),
                        class_name="bg-transparent border border-outline-variant/40 rounded-lg p-1.5 cursor-pointer hover:bg-surface-container-low",
                    ),
                    rx.el.button(
                        rx.el.span("more_horiz", class_name="material-symbols-outlined text-sm"),
                        class_name="bg-transparent border border-outline-variant/40 rounded-lg p-1.5 cursor-pointer hover:bg-surface-container-low",
                    ),
                    class_name="flex items-center gap-2 mt-3",
                ),
                class_name="ml-auto flex flex-col items-end flex-shrink-0",
            ),
            class_name="flex items-start gap-4 w-full",
        ),
        class_name="bg-white rounded-2xl p-5 shadow-sm",
    )


def my_applications_page_content() -> rx.Component:
    return backoffice_layout(
        "applications",
        rx.box(
            rx.hstack(
                rx.box(
                    rx.heading("My Applications", as_="h1", class_name="text-2xl font-bold text-on-surface"),
                    rx.text("Track and manage your retail space applications across premium locations.", class_name="text-sm text-on-surface-variant mt-1"),
                ),
            ),
            rx.vstack(
                _application_card(
                    station="Rama 9 Station - Retail",
                    location="Bangkok, Thailand",
                    store_type="Premium Kiosk (30sqm)",
                    lease="24 Months",
                    date="Oct 24, 2023",
                    status_label="REVIEWING STAGE",
                    status_type="reviewing",
                    step=1,
                ),
                _application_card(
                    station="Sukhumvit Prime",
                    location="Watthana, Bangkok",
                    store_type="Pop-up Corner (8sqm)",
                    lease="6 Months",
                    date="Nov 12, 2023",
                    status_label="APPLICATION SUBMITTED",
                    status_type="submitted",
                    step=0,
                ),
                class_name="gap-4 mt-6 w-full",
            ),
        ),
    )
