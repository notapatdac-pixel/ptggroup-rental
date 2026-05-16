import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout


def _doc_row(icon: str, title: str, subtitle: str, action: str, pending: bool = False) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.el.span(icon, class_name="material-symbols-outlined text-on-surface-variant text-xl"),
            class_name="w-12 h-12 bg-surface-container-low rounded-xl flex items-center justify-center flex-shrink-0",
        ),
        rx.box(
            rx.text(title, class_name="text-sm font-bold text-on-surface"),
            rx.text(subtitle, class_name="text-xs text-on-surface-variant"),
            class_name="flex-1",
        ),
        rx.el.button(
            rx.hstack(
                rx.el.span("schedule" if pending else "upload", class_name="material-symbols-outlined text-sm"),
                rx.text(action, class_name="text-sm font-bold"),
                class_name="flex items-center gap-1.5",
            ),
            class_name=(
                "bg-surface-container-low border border-outline-variant/40 rounded-full px-5 py-2 cursor-not-allowed text-on-surface-variant"
                if pending
                else "backoffice-btn-primary rounded-full px-5 py-2 border-0 cursor-pointer"
            ),
        ),
        class_name="flex items-center gap-4 py-4 px-5 border border-outline-variant/20 rounded-2xl bg-white",
    )


def approved_docs_page_content() -> rx.Component:
    return backoffice_layout(
        "applications",
        rx.grid(
            rx.box(
                rx.heading("Application Status:", as_="h1", class_name="text-3xl font-bold text-on-surface leading-tight"),
                rx.heading("Approved", as_="h1", class_name="text-3xl font-bold text-on-surface"),
                rx.box(
                    rx.hstack(
                        rx.el.span("verified", class_name="material-symbols-outlined text-backoffice-primary text-xl flex-shrink-0"),
                        rx.box(
                            rx.text("Your slot has been approved!", class_name="text-sm font-bold text-backoffice-primary"),
                            rx.text("Please provide the remaining documentation to finalize your retail placement.", class_name="text-xs text-on-surface-variant"),
                        ),
                        class_name="flex items-center gap-3",
                    ),
                    class_name="border-l-4 border-backoffice-primary bg-surface-container-low rounded-r-xl p-4 mt-6 mb-6",
                ),
                rx.hstack(
                    rx.text("Required Documents", class_name="text-base font-bold text-on-surface"),
                    rx.text("3 Files Total", class_name="text-xs text-on-surface-variant"),
                    class_name="flex items-center gap-3 mb-4",
                ),
                rx.vstack(
                    _doc_row("description", "Business License", "Valid registration (Max 10MB, PDF)", "Upload"),
                    _doc_row("badge", "ID Card", "Government issued (Photo or PDF)", "Upload"),
                    _doc_row("account_balance_wallet", "Proof of Funds", "Awaiting review", "Pending", pending=True),
                    class_name="gap-3 w-full",
                ),
                rx.box(
                    rx.text("Estimated Review Time", class_name="text-sm font-bold text-on-surface mb-2"),
                    rx.text(
                        "Once all documents are submitted, our compliance team typically completes the final verification within 24–48 business hours. You will receive an automated notification via the platform and email.",
                        class_name="text-xs text-on-surface-variant leading-relaxed",
                    ),
                    class_name="bg-surface-container-low rounded-2xl p-5 mt-6",
                ),
            ),
            rx.box(
                rx.box(
                    rx.box(
                        rx.el.span("person", class_name="material-symbols-outlined text-on-surface-variant text-4xl"),
                        class_name="w-20 h-20 rounded-2xl bg-surface-container flex items-center justify-center mx-auto mb-3",
                    ),
                    rx.text("Sarah Sterliãą", class_name="text-base font-bold text-on-surface text-center"),
                    rx.text("Onboarding Specialist", class_name="text-xs text-on-surface-variant text-center mb-5"),
                    rx.el.button(
                        rx.hstack(
                            rx.el.span("chat", class_name="material-symbols-outlined text-base"),
                            rx.text("Message Sarah", class_name="text-sm font-bold"),
                            class_name="flex items-center gap-2 justify-center",
                        ),
                        class_name="backoffice-btn-primary w-full py-3 rounded-xl border-0 cursor-pointer mb-3",
                    ),
                    rx.el.button(
                        rx.hstack(
                            rx.el.span("calendar_today", class_name="material-symbols-outlined text-base"),
                            rx.text("Schedule a Call", class_name="text-sm font-bold"),
                            class_name="flex items-center gap-2 justify-center",
                        ),
                        class_name="w-full py-3 rounded-xl border border-outline-variant/40 cursor-pointer bg-white text-on-surface mb-3",
                    ),
                    rx.text("AVAILABLE 9AM - 5PM EST", class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant/50 text-center"),
                    class_name="bg-white rounded-2xl p-6 shadow-sm mb-4",
                ),
                rx.box(
                    rx.text("QUICK TIPS", class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-3"),
                    rx.vstack(
                        rx.hstack(
                            rx.el.span("info", class_name="material-symbols-outlined text-backoffice-primary text-base flex-shrink-0"),
                            rx.text("Use high-resolution scans for faster ID verification.", class_name="text-xs text-on-surface-variant leading-relaxed"),
                            class_name="flex items-start gap-2",
                        ),
                        rx.hstack(
                            rx.el.span("lock", class_name="material-symbols-outlined text-backoffice-primary text-base flex-shrink-0"),
                            rx.text("All data is encrypted and stored according to ISO 27001 standards.", class_name="text-xs text-on-surface-variant leading-relaxed"),
                            class_name="flex items-start gap-2",
                        ),
                        class_name="gap-3",
                    ),
                    class_name="bg-white rounded-2xl p-5 shadow-sm mb-4",
                ),
                rx.link(
                    rx.el.button(
                        "Back to My Applications",
                        class_name="backoffice-btn-primary w-full py-3 rounded-xl border-0 cursor-pointer font-bold text-sm",
                    ),
                    href="/retailerapplications",
                    class_name="no-underline block",
                ),
            ),
            columns="2",
            class_name="gap-8",
            style={"grid-template-columns": "1.5fr 1fr"},
        ),
    )

