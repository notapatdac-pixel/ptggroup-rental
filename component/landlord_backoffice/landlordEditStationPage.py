import reflex as rx
from component.landlord_backoffice.landlord_layout import landlord_layout


def _section_title(text: str) -> rx.Component:
    return rx.text(text, class_name="text-lg font-bold text-primary mb-4")


def _label(text: str, required: bool = False) -> rx.Component:
    return rx.hstack(
        rx.text(text, class_name="text-xs font-bold text-on-surface-variant uppercase tracking-wide"),
        rx.text(" *", class_name="text-error text-xs") if required else rx.fragment(),
        class_name="flex items-center mb-1.5",
    )


def _text_input(placeholder: str, value: str = "") -> rx.Component:
    return rx.el.input(
        placeholder=placeholder,
        default_value=value,
        class_name="backoffice-input italic",
    )


def _traffic_pill(label: str, desc: str, active: bool = False) -> rx.Component:
    border_cls = "border-primary bg-primary/5" if active else "border-outline-variant bg-white"
    label_cls = "text-sm font-bold text-primary" if active else "text-sm font-semibold text-on-surface"
    return rx.box(
        rx.text(label, class_name=label_cls),
        rx.text(desc, class_name="text-xs text-on-surface-variant mt-0.5"),
        class_name=f"border-2 {border_cls} rounded-xl px-5 py-3 cursor-pointer flex-1 transition-colors",
    )


def _unit_row(icon: str, name: str, spec: str, rent: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.el.span(icon, class_name="material-symbols-outlined text-[16px] text-on-surface-variant"),
            class_name="w-8 h-8 bg-surface-container rounded-lg flex items-center justify-center flex-shrink-0",
        ),
        rx.box(
            rx.text(name, class_name="text-sm font-semibold text-on-surface"),
            rx.text(spec, class_name="text-xs text-on-surface-variant"),
            class_name="flex-1",
        ),
        rx.hstack(
            rx.box(
                rx.text("MONTHLY RENT", class_name="text-[9px] font-bold tracking-widest text-on-surface-variant text-right"),
                rx.text(rent, class_name="text-sm font-bold text-on-surface text-right"),
            ),
            rx.el.span("edit", class_name="material-symbols-outlined text-[16px] text-on-surface-variant cursor-pointer"),
            class_name="flex items-center gap-2",
        ),
        class_name="flex items-center gap-3 py-3 border-b border-outline-variant/20 last:border-0",
    )


def _goal_card(icon: str, label: str, child: rx.Component) -> rx.Component:
    return rx.box(
        rx.el.span(icon, class_name="material-symbols-outlined text-[22px] text-backoffice-primary mb-2"),
        rx.text(label, class_name="text-sm font-bold text-on-surface mb-2"),
        child,
        class_name="backoffice-kpi-card flex-1",
    )


def landlord_edit_station_page_content() -> rx.Component:
    return landlord_layout(
        "stations",
        rx.box(
            rx.hstack(
                rx.text("STATIONS", class_name="text-[11px] font-bold tracking-widest text-on-surface-variant"),
                rx.el.span("chevron_right", class_name="material-symbols-outlined text-[16px] text-on-surface-variant"),
                rx.text("EDIT DETAILS", class_name="text-[11px] font-bold tracking-widest text-primary"),
                class_name="flex items-center gap-1 mb-2",
            ),
            rx.heading("Edit Station Details", as_="h1",
                       class_name="text-3xl font-bold font-headline text-on-surface mb-2"),
            rx.hstack(
                rx.text("Update the analytical and operational parameters for ", class_name="text-sm text-on-surface-variant"),
                rx.text("Station PTG station lat phrao 71", class_name="text-sm font-bold text-primary"),
                rx.text(". These changes will reflect across the tenant marketplace and internal reporting.",
                        class_name="text-sm text-on-surface-variant"),
                class_name="flex items-center flex-wrap gap-0 mb-8",
            ),
            # Basic Information
            _section_title("Basic Information"),
            rx.grid(
                rx.box(
                    _label("Station Name", required=True),
                    _text_input("Station name", "PTG Prime Ratchapruek"),
                    class_name="flex flex-col",
                ),
                rx.box(
                    _label("Province / Region"),
                    rx.box(
                        rx.hstack(
                            rx.text("Nonthaburi", class_name="text-sm text-on-surface flex-1"),
                            rx.el.span("expand_more", class_name="material-symbols-outlined text-[18px] text-on-surface-variant"),
                            class_name="flex items-center gap-2",
                        ),
                        class_name="backoffice-input cursor-pointer flex",
                    ),
                    class_name="flex flex-col",
                ),
                columns="2",
                class_name="gap-6 mb-5",
            ),
            rx.box(
                _label("Traffic Level Descriptor"),
                rx.hstack(
                    _traffic_pill("High Velocity", "Over 5,000 cars/day", active=True),
                    _traffic_pill("Steady Stream", "2,000 - 5,000 cars/day"),
                    _traffic_pill("Community Local", "Under 2,000 cars/day"),
                    class_name="flex gap-3",
                ),
                class_name="mb-8",
            ),
            # Space Details
            _section_title("Space Details"),
            rx.grid(
                rx.box(
                    rx.text("Unit Inventory & Pricing",
                            class_name="text-sm font-bold text-on-surface mb-2"),
                    _unit_row("local_cafe", "Cafe Corner (B2)", "45 sq.m · Near Entrance", "฿18,500"),
                    _unit_row("store", "Main Retail (A1)", "120 sq.m · Premium Frontage", "฿45,000"),
                    rx.hstack(
                        rx.el.span("add_circle", class_name="material-symbols-outlined text-[16px] text-primary"),
                        rx.text("Add New Inventory Unit", class_name="text-sm font-semibold text-primary cursor-pointer"),
                        class_name="flex items-center gap-1.5 pt-2",
                    ),
                    class_name="bg-surface-container-low rounded-2xl p-5",
                ),
                rx.box(
                    rx.text("Portfolio Value", class_name="text-sm font-bold text-on-surface mb-1"),
                    rx.text("Estimated monthly yields based on current inventory pricing.",
                            class_name="text-xs text-on-surface-variant mb-4"),
                    rx.text("63.5k", class_name="text-4xl font-bold text-primary"),
                    class_name="backoffice-kpi-card border border-primary/20",
                ),
                columns="2",
                class_name="gap-6 mb-8",
            ),
            # Business Goals
            _section_title("Business Goals"),
            rx.grid(
                _goal_card(
                    "flag",
                    "Target Tenant Type",
                    rx.box(
                        rx.hstack(
                            rx.text("F&B Franchises", class_name="text-sm text-on-surface flex-1"),
                            rx.el.span("expand_more", class_name="material-symbols-outlined text-[16px] text-on-surface-variant"),
                            class_name="flex items-center",
                        ),
                        class_name="backoffice-input cursor-pointer flex",
                    ),
                ),
                _goal_card(
                    "savings",
                    "Annual Revenue Goal",
                    rx.el.input(
                        default_value="750000",
                        class_name="backoffice-input",
                        type="number",
                    ),
                ),
                _goal_card(
                    "trending_up",
                    "Expected Footfall Growth",
                    rx.hstack(
                        rx.el.input(
                            default_value="15",
                            class_name="backoffice-input",
                            type="number",
                            style={"width": "70px"},
                        ),
                        rx.text("% YoY", class_name="text-sm text-on-surface-variant"),
                        class_name="flex items-center gap-2",
                    ),
                ),
                columns="3",
                class_name="gap-4 mb-8",
            ),
            # Media Gallery
            _section_title("Media Gallery"),
            rx.hstack(
                rx.image(
                    src="/image/station-ptg-latphrao71.png",
                    class_name="w-40 h-28 object-cover rounded-xl",
                ),
                rx.image(
                    src="/image/station-ptg-bangna.png",
                    class_name="w-40 h-28 object-cover rounded-xl",
                ),
                rx.box(
                    rx.vstack(
                        rx.el.span("add_photo_alternate", class_name="material-symbols-outlined text-[28px] text-on-surface-variant"),
                        rx.text("Upload Station Photos", class_name="text-sm font-semibold text-on-surface text-center"),
                        rx.text("JPEG or PNG. Max 5MB", class_name="text-xs text-on-surface-variant"),
                        class_name="flex flex-col items-center gap-1",
                    ),
                    class_name=(
                        "w-56 h-28 border-2 border-dashed border-outline-variant rounded-xl "
                        "flex items-center justify-center cursor-pointer hover:border-primary transition-colors"
                    ),
                ),
                class_name="flex gap-3 mb-10",
            ),
            # Actions
            rx.hstack(
                rx.el.button(
                    "Cancel",
                    class_name=(
                        "bg-white border border-outline-variant/40 rounded-full px-8 py-3 "
                        "text-sm font-bold text-on-surface cursor-pointer hover:bg-surface-container-low transition-colors"
                    ),
                ),
                rx.el.button(
                    rx.hstack(
                        rx.el.span("check_circle", class_name="material-symbols-outlined text-[18px] fill-icon"),
                        rx.text("Save Changes", class_name="text-sm font-bold"),
                        class_name="flex items-center gap-1.5",
                    ),
                    class_name="backoffice-btn-primary border-0 rounded-full px-8 py-3 cursor-pointer",
                ),
                class_name="flex items-center justify-center gap-4",
            ),
        ),
    )
