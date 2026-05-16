import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout


def _calendar_day(day: str, active: bool = False, dim: bool = False) -> rx.Component:
    return rx.box(
        rx.text(
            day,
            class_name=(
                "text-sm font-bold w-8 h-8 flex items-center justify-center rounded-full "
                + ("bg-backoffice-primary text-white" if active else "text-on-surface-variant/30" if dim else "text-on-surface hover:bg-surface-container-low cursor-pointer")
            ),
        ),
        class_name="flex items-center justify-center",
    )


def _time_slot(label: str, active: bool = False) -> rx.Component:
    return rx.el.button(
        label,
        class_name=f"backoffice-time-chip{'--active' if active else ''} backoffice-time-chip",
    )


def _chat_msg(sender: str, text: str, is_user: bool = False) -> rx.Component:
    return rx.box(
        rx.text(text, class_name=f"backoffice-chat-bubble-{'user' if is_user else 'agent'}"),
        class_name="flex" + (" justify-end" if is_user else ""),
    )


def schedule_chat_page_content() -> rx.Component:
    return backoffice_layout(
        "applications",
        rx.box(
            rx.heading("Finalize Walkthrough & Coordination", as_="h1", class_name="text-2xl font-bold text-on-surface mb-1"),
            rx.text("Review site logistics, select your preferred walkthrough window, and coordinate final details with the regional property manager.", class_name="text-sm text-on-surface-variant mb-6"),
            rx.grid(
                rx.box(
                    rx.box(
                        rx.hstack(
                            rx.text("Site Walkthrough", class_name="text-base font-bold text-on-surface"),
                            rx.hstack(
                                rx.el.span("calendar_today", class_name="material-symbols-outlined text-base text-on-surface-variant"),
                                rx.text("OCTOBER 2024", class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant"),
                                class_name="flex items-center gap-1",
                            ),
                            class_name="flex justify-between items-center mb-4",
                        ),
                        rx.grid(
                            *[rx.text(d, class_name="text-[9px] font-bold tracking-widest text-center text-on-surface-variant") for d in ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]],
                            columns="7",
                            class_name="gap-1 mb-2",
                        ),
                        rx.grid(
                            _calendar_day("", dim=True),
                            _calendar_day("", dim=True),
                            _calendar_day("1"),
                            _calendar_day("2"),
                            _calendar_day("3"),
                            _calendar_day("4"),
                            _calendar_day("5"),
                            _calendar_day("6"),
                            _calendar_day("7"),
                            _calendar_day("8"),
                            _calendar_day("9"),
                            _calendar_day("10"),
                            _calendar_day("11"),
                            _calendar_day("12"),
                            _calendar_day("13"),
                            _calendar_day("14"),
                            _calendar_day("15"),
                            _calendar_day("16"),
                            _calendar_day("17"),
                            _calendar_day("18"),
                            _calendar_day("19"),
                            _calendar_day("20"),
                            _calendar_day("21"),
                            _calendar_day("22"),
                            _calendar_day("23"),
                            _calendar_day("24", active=True),
                            _calendar_day("25"),
                            _calendar_day("26"),
                            _calendar_day("27"),
                            _calendar_day("28"),
                            _calendar_day("29"),
                            _calendar_day("30"),
                            _calendar_day("31"),
                            columns="7",
                            class_name="gap-1",
                        ),
                        class_name="mb-4",
                    ),
                    rx.box(
                        rx.text("AVAILABLE WINDOWS", class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-3"),
                        rx.hstack(
                            _time_slot("09:00 AM"),
                            _time_slot("11:30 AM", active=True),
                            _time_slot("02:30 PM"),
                            _time_slot("04:30 PM"),
                            class_name="flex flex-wrap gap-2",
                        ),
                        class_name="mb-4",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.el.span("description", class_name="material-symbols-outlined text-on-surface-variant text-base"),
                            rx.text("Walkthrough Notes", class_name="text-xs font-bold text-on-surface"),
                            class_name="flex items-center gap-2 mb-2",
                        ),
                        rx.el.ul(
                            rx.el.li("Registration documents", class_name="text-xs text-on-surface-variant"),
                            rx.el.li("Financial proof", class_name="text-xs text-on-surface-variant"),
                            rx.el.li("Lease agreement details", class_name="text-xs text-on-surface-variant"),
                            rx.el.li("Authorized signatory documents", class_name="text-xs text-on-surface-variant"),
                            class_name="list-disc list-inside space-y-1",
                        ),
                        class_name="bg-surface-container-low rounded-xl p-4",
                    ),
                    class_name="bg-white rounded-2xl p-6 shadow-sm",
                ),
                rx.box(
                    rx.box(
                        rx.hstack(
                            rx.box(
                                rx.el.span("person", class_name="material-symbols-outlined text-white text-base"),
                                class_name="w-8 h-8 rounded-full bg-backoffice-primary flex items-center justify-center flex-shrink-0",
                            ),
                            rx.text("Siriporn K.", class_name="text-xs font-bold text-on-surface"),
                            class_name="flex items-center gap-2 mb-4",
                        ),
                        rx.vstack(
                            _chat_msg("agent", "Hello! I've seen your request for the site walkthrough at Station 033. I'm very comfortable with the 11:30 AM slot today!"),
                            _chat_msg("user", "Hi Siriporn! I'll see the area works perfectly for me. We'll finalizing the structural reports and have ready at the site. See you then!", is_user=True),
                            _chat_msg("agent", "Great. I'll take the structural reports and have ready at the main entrance. See you then!"),
                            class_name="gap-3",
                        ),
                        rx.box(
                            rx.el.input(
                                placeholder="Write a coordination note...",
                                class_name="flex-1 bg-transparent border-none outline-none text-sm text-on-surface placeholder-on-surface-variant/50",
                            ),
                            rx.el.button(
                                rx.el.span("send", class_name="material-symbols-outlined text-white text-sm"),
                                class_name="backoffice-btn-primary rounded-full w-8 h-8 border-0 cursor-pointer flex items-center justify-center flex-shrink-0",
                            ),
                            class_name="flex items-center gap-2 mt-4 bg-surface-container-low rounded-full px-4 py-2",
                        ),
                        class_name="bg-white rounded-2xl p-5 shadow-sm h-full flex flex-col",
                    ),
                ),
                columns="2",
                class_name="gap-6 mb-6",
            ),
            rx.hstack(
                rx.hstack(
                    rx.el.span("calendar_today", class_name="material-symbols-outlined text-on-surface-variant text-sm"),
                    rx.text("Walkthrough - Oct 24, 11:30 AM", class_name="text-xs font-bold text-on-surface"),
                    rx.text("•", class_name="text-on-surface-variant"),
                    rx.hstack(
                        rx.el.span("location_on", class_name="material-symbols-outlined text-on-surface-variant text-sm"),
                        rx.text("Unit C - North Wing", class_name="text-xs text-on-surface-variant"),
                        class_name="flex items-center gap-1",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.hstack(
                    rx.el.button("Reschedule", class_name="bg-white border border-outline-variant/40 rounded-full px-5 py-2.5 cursor-pointer text-sm font-bold text-on-surface"),
                    rx.link(
                        rx.el.button("CONFIRM BOOKING TIME", class_name="backoffice-btn-primary rounded-full px-6 py-2.5 border-0 cursor-pointer text-sm font-bold"),
                        href="/retailerbookingconfirm",
                        class_name="no-underline",
                    ),
                    class_name="flex items-center gap-3",
                ),
                class_name="flex justify-between items-center bg-white rounded-2xl px-6 py-4 shadow-sm",
            ),
        ),
    )

