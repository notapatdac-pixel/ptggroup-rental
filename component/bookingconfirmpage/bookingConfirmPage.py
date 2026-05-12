import reflex as rx

from component.backoffice.backoffice_layout import backoffice_layout


def booking_confirm_page_content() -> rx.Component:
    return backoffice_layout(
        "applications",
        rx.box(
            rx.box(
                rx.box(
                    rx.el.span("check", class_name="material-symbols-outlined text-white text-4xl"),
                    class_name="w-16 h-16 rounded-full bg-backoffice-primary flex items-center justify-center mx-auto mb-6",
                ),
                rx.heading("Booking Confirmed", as_="h1", class_name="text-3xl font-bold text-on-surface text-center mb-2"),
                rx.text(
                    "Your reservation at the Sovereign Curator has been secured.",
                    class_name="text-sm text-on-surface-variant text-center mb-8",
                ),
                rx.box(
                    rx.grid(
                        rx.box(
                            rx.text("Reservation Summary", class_name="text-lg font-bold text-backoffice-primary font-headline italic mb-5"),
                            rx.vstack(
                                rx.box(
                                    rx.text("BOOKING ID", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                                    rx.text("#BK-7729", class_name="text-sm font-bold text-on-surface"),
                                    class_name="mb-3",
                                ),
                                rx.box(
                                    rx.text("SCHEDULED DATE", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                                    rx.hstack(
                                        rx.el.span("calendar_today", class_name="material-symbols-outlined text-sm text-on-surface-variant"),
                                        rx.text("Oct 24", class_name="text-sm font-bold text-on-surface"),
                                        class_name="flex items-center gap-1",
                                    ),
                                    class_name="mb-3",
                                ),
                                rx.box(
                                    rx.text("LOCATION", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                                    rx.hstack(
                                        rx.el.span("location_on", class_name="material-symbols-outlined text-sm text-on-surface-variant"),
                                        rx.text("Unit C, Lat Phrao 71", class_name="text-sm font-bold text-on-surface"),
                                        class_name="flex items-center gap-1",
                                    ),
                                    class_name="mb-3",
                                ),
                                rx.box(
                                    rx.text("CURATED BY", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                                    rx.hstack(
                                        rx.box(
                                            rx.el.span("person", class_name="material-symbols-outlined text-white text-sm"),
                                            class_name="w-7 h-7 rounded-full bg-backoffice-primary flex items-center justify-center",
                                        ),
                                        rx.text("Sovereign Partner", class_name="text-sm font-bold text-on-surface"),
                                        class_name="flex items-center gap-2",
                                    ),
                                ),
                                class_name="gap-0",
                            ),
                        ),
                        rx.box(
                            rx.box(
                                rx.el.span("map", class_name="material-symbols-outlined text-on-surface-variant/30 text-6xl"),
                                class_name="w-full h-full min-h-[160px] bg-surface-container rounded-xl flex items-center justify-center relative",
                            ),
                            rx.box(
                                rx.text("REGION", class_name="text-[9px] font-bold tracking-widest uppercase text-on-surface-variant mb-0.5"),
                                rx.text("Lat Phrao District", class_name="text-xs font-bold text-on-surface"),
                                class_name="absolute bottom-3 right-3 bg-white rounded-lg px-3 py-2 shadow-sm",
                            ),
                            class_name="relative",
                        ),
                        columns="2",
                        class_name="gap-6",
                    ),
                    class_name="bg-white rounded-2xl p-6 shadow-sm max-w-2xl mx-auto mb-6",
                ),
                rx.vstack(
                    rx.link(
                        rx.el.button(
                            rx.hstack(
                                rx.text("Go to My Dashboard", class_name="font-bold"),
                                rx.el.span("arrow_forward", class_name="material-symbols-outlined text-base"),
                                class_name="flex items-center gap-2",
                            ),
                            class_name="backoffice-btn-primary w-72 py-3.5 rounded-full border-0 cursor-pointer text-sm",
                        ),
                        href="/retailerdashboard",
                        class_name="no-underline",
                    ),
                    rx.el.button(
                        rx.hstack(
                            rx.el.span("download", class_name="material-symbols-outlined text-base"),
                            rx.text("Download Receipt", class_name="font-bold"),
                            class_name="flex items-center gap-2",
                        ),
                        class_name="w-72 py-3.5 rounded-full border border-outline-variant/40 bg-white text-on-surface cursor-pointer text-sm",
                    ),
                    class_name="gap-3 items-center",
                ),
                class_name="flex flex-col items-center py-8",
            ),
        ),
    )
