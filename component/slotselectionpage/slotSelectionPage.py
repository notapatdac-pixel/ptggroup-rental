import reflex as rx

from component.backoffice.backoffice_layout import backoffice_layout


def _unit_card(label: str, status: str, selected: bool = False) -> rx.Component:
    mod = ""
    if status.lower() == "occupied":
        mod = " backoffice-unit-card--occupied"
    elif status.lower() in ("under contract", "reserved"):
        mod = " backoffice-unit-card--reserved"
    elif selected:
        mod = " backoffice-unit-card--available"

    return rx.box(
        rx.hstack(
            rx.text(label, class_name=f"text-base font-bold {'text-backoffice-primary' if selected else 'text-on-surface'}"),
            rx.el.span("check_circle", class_name="material-symbols-outlined text-backoffice-primary text-sm fill-icon") if selected else rx.fragment(),
            class_name="flex items-center gap-1 justify-center mb-1",
        ),
        rx.text(status.upper(), class_name=f"text-[9px] font-bold tracking-widest uppercase {'text-backoffice-primary backoffice-chip-available' if selected else 'text-on-surface-variant/50'}"),
        class_name=f"backoffice-unit-card{mod}",
    )


def _amenity_chip(icon: str, label: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.el.span(icon, class_name="material-symbols-outlined text-backoffice-primary text-base"),
            rx.text(label, class_name="text-xs font-semibold text-on-surface"),
            class_name="flex flex-col items-center gap-0.5",
        ),
        class_name="bg-surface-container-low rounded-xl p-3 flex items-center justify-center",
    )


def slot_selection_page_content() -> rx.Component:
    return backoffice_layout(
        "applications",
        rx.box(
            rx.heading("Slot Selection", as_="h1", class_name="text-2xl font-bold text-on-surface mb-1"),
            rx.text("Select a functional unit from the master blueprint to view real-time availability and technical specs.", class_name="text-sm text-on-surface-variant mb-6"),
            rx.grid(
                rx.box(
                    rx.box(
                        rx.grid(
                            _unit_card("Unit A", "Occupied"),
                            _unit_card("Unit B", "Under Contract"),
                            _unit_card("Unit C", "Available", selected=True),
                            _unit_card("Unit D", "Reserved"),
                            columns="2",
                            class_name="gap-4",
                        ),
                        rx.hstack(
                            rx.el.button(
                                rx.el.span("zoom_in", class_name="material-symbols-outlined text-sm"),
                                class_name="bg-white border border-outline-variant/30 rounded-lg p-1.5 cursor-pointer",
                            ),
                            rx.el.button(
                                rx.el.span("zoom_out", class_name="material-symbols-outlined text-sm"),
                                class_name="bg-white border border-outline-variant/30 rounded-lg p-1.5 cursor-pointer",
                            ),
                            rx.el.button(
                                rx.el.span("layers", class_name="material-symbols-outlined text-sm"),
                                class_name="bg-white border border-outline-variant/30 rounded-lg p-1.5 cursor-pointer",
                            ),
                            class_name="flex items-center gap-2 mt-4",
                        ),
                        class_name="bg-surface-container-low rounded-2xl p-8",
                    ),
                ),
                rx.box(
                    rx.text("Unit C", class_name="text-2xl font-bold text-on-surface mb-1"),
                    rx.hstack(
                        rx.text("Details", class_name="text-2xl font-bold text-on-surface"),
                        rx.box(rx.text("AVAILABLE", class_name="text-[10px] font-bold text-backoffice-primary"), class_name="backoffice-chip-available ml-2"),
                        class_name="flex items-center mb-4",
                    ),
                    rx.box(
                        rx.box(
                            rx.el.span("storefront", class_name="material-symbols-outlined text-on-surface-variant/30 text-5xl"),
                            rx.box(rx.text("High-Demand Area", class_name="text-[9px] font-bold text-white"), class_name="absolute top-2 left-2 bg-backoffice-primary rounded-full px-2 py-0.5"),
                            class_name="w-full h-36 bg-surface-container rounded-xl flex items-center justify-center relative mb-4",
                        ),
                    ),
                    rx.hstack(
                        rx.box(
                            rx.text("Annual", class_name="text-[9px] text-on-surface-variant"),
                            rx.text("Rent", class_name="text-[9px] text-on-surface-variant"),
                        ),
                        class_name="mb-3",
                    ),
                    rx.text("TOP AMENITIES", class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-3"),
                    rx.grid(
                        _amenity_chip("bolt", "3-Phase\nPower"),
                        _amenity_chip("ac_unit", "HVAC\nReady"),
                        _amenity_chip("local_shipping", "Loading\nBay"),
                        _amenity_chip("wifi", "Fiber\nFiber"),
                        columns="2",
                        class_name="gap-2 mb-4",
                    ),
                    rx.text(
                        '"Unit C offers the highest ceiling clearance in the complex and direct visibility from the primary loading dock corridor."',
                        class_name="text-xs text-on-surface-variant italic leading-relaxed mb-5",
                    ),
                    rx.link(
                        rx.el.button(
                            rx.hstack(
                                rx.text("Next Step", class_name="font-bold"),
                                rx.el.span("arrow_forward", class_name="material-symbols-outlined text-base"),
                                class_name="flex items-center gap-2",
                            ),
                            class_name="backoffice-btn-primary w-full py-3 rounded-full border-0 cursor-pointer text-sm",
                        ),
                        href="/retailerconfirmapply",
                        class_name="no-underline",
                    ),
                ),
                columns="2",
                class_name="gap-8",
                style={"grid-template-columns": "1.2fr 1fr"},
            ),
        ),
    )
