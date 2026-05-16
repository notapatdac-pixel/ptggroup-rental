import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout

_LABEL = "text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1.5 block"
_INPUT = "backoffice-input"


def _lease_chip(label: str, active: bool = False) -> rx.Component:
    return rx.el.button(
        label,
        class_name=f"backoffice-time-chip{'--active' if active else ''} backoffice-time-chip",
    )


def confirm_apply_page_content() -> rx.Component:
    return backoffice_layout(
        "applications",
        rx.grid(
            rx.box(
                rx.text("Unit Selection Summary", class_name="text-sm font-bold text-on-surface mb-4"),
                rx.box(
                    rx.box(
                        rx.el.span("storefront", class_name="material-symbols-outlined text-on-surface-variant/30 text-4xl"),
                        rx.box(rx.text("Reserved", class_name="text-[9px] font-bold text-white"), class_name="absolute top-2 right-2 bg-backoffice-primary rounded-full px-2 py-0.5"),
                        class_name="w-full h-36 bg-surface-container rounded-xl flex items-center justify-center relative mb-4",
                    ),
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text("Space Reference", class_name="text-xs text-on-surface-variant flex-1"),
                        rx.text("Unit C", class_name="text-xs font-bold text-on-surface"),
                        class_name="flex items-center",
                    ),
                    rx.hstack(
                        rx.text("Floor Area", class_name="text-xs text-on-surface-variant flex-1"),
                        rx.text("48 sqm", class_name="text-xs font-bold text-on-surface"),
                        class_name="flex items-center",
                    ),
                    rx.hstack(
                        rx.text("Monthly Investment", class_name="text-xs text-on-surface-variant flex-1"),
                        rx.text("15,000 /mo", class_name="text-base font-bold text-backoffice-primary"),
                        class_name="flex items-center",
                    ),
                    class_name="gap-2 mb-4",
                ),
                rx.box(
                    rx.text(
                        '"You are currently in a priority reservation window for this unit. Complete the profile details to secure your position."',
                        class_name="text-xs text-on-surface-variant italic leading-relaxed",
                    ),
                    class_name="bg-surface-container-low rounded-xl p-4 border-l-4 border-backoffice-primary",
                ),
                class_name="bg-white rounded-2xl p-6 shadow-sm",
            ),
            rx.box(
                rx.heading("Retailer Profile Details", as_="h1", class_name="text-2xl font-bold text-on-surface mb-2"),
                rx.text("Tell us more about your brand essence and operational requirements to tailor our leasing proposal.", class_name="text-sm text-on-surface-variant mb-6"),
                rx.text("IDENTITY & ENTITY", class_name=f"{_LABEL} mb-4"),
                rx.grid(
                    rx.box(
                        rx.el.label("BUSINESS NAME", class_name=_LABEL),
                        rx.el.input(placeholder="e.g. Atelier Vert", class_name=f"{_INPUT} w-full"),
                        class_name="flex flex-col",
                    ),
                    rx.box(
                        rx.el.label("BUSINESS TYPE", class_name=_LABEL),
                        rx.el.select(
                            rx.el.option("Boutique Apparel"),
                            rx.el.option("Food & Beverage"),
                            rx.el.option("Electronics"),
                            rx.el.option("Health & Beauty"),
                            rx.el.option("Other"),
                            class_name=f"{_INPUT} w-full",
                        ),
                        class_name="flex flex-col",
                    ),
                    columns="2",
                    class_name="gap-4 mb-6",
                ),
                rx.text("OPERATIONS & INTENT", class_name=f"{_LABEL} mb-4"),
                rx.grid(
                    rx.box(
                        rx.el.label("MONTHLY BUDGET RANGE", class_name=_LABEL),
                        rx.hstack(
                            rx.el.input(value="12,000", class_name=f"{_INPUT} w-full"),
                            rx.text("—", class_name="text-on-surface-variant font-bold"),
                            rx.el.input(value="18,000", class_name=f"{_INPUT} w-full"),
                            class_name="flex items-center gap-2",
                        ),
                        class_name="flex flex-col",
                    ),
                    rx.box(
                        rx.el.label("LEASE DURATION", class_name=_LABEL),
                        rx.hstack(
                            _lease_chip("1 MO"),
                            _lease_chip("3 MOS", active=True),
                            _lease_chip("6 MOS"),
                            _lease_chip("12 MOS+"),
                            class_name="flex flex-wrap gap-2",
                        ),
                        class_name="flex flex-col",
                    ),
                    columns="2",
                    class_name="gap-4 mb-4",
                ),
                rx.box(
                    rx.el.label("PROJECT DESCRIPTION", class_name=_LABEL),
                    rx.el.textarea(
                        placeholder="Describe your brand's vision, target audience, and how you plan to utilize the Unit C space...",
                        rows="4",
                        class_name=f"{_INPUT} w-full resize-none",
                    ),
                    class_name="flex flex-col mb-8",
                ),
                rx.hstack(
                    rx.link(
                        rx.el.button("Back", class_name="bg-white border border-outline-variant/40 rounded-full px-8 py-3 cursor-pointer text-sm font-bold text-on-surface"),
                        href="/retailerslotselection",
                        class_name="no-underline",
                    ),
                    rx.el.button(
                        rx.hstack(
                            rx.text("Continue to Review", class_name="font-bold"),
                            rx.el.span("arrow_forward", class_name="material-symbols-outlined text-base"),
                            class_name="flex items-center gap-2",
                        ),
                        class_name="backoffice-btn-primary rounded-full px-8 py-3 border-0 cursor-pointer text-sm",
                    ),
                    class_name="flex justify-end gap-3",
                ),
            ),
            columns="2",
            class_name="gap-8",
            style={"grid-template-columns": "1fr 2fr"},
        ),
    )

