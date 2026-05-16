import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout
from component.auth_state import AuthState


def _step_label(num: str, title: str) -> rx.Component:
    return rx.box(
        rx.text(
            f"STEP {num}",
            class_name="text-[10px] font-bold tracking-widest uppercase text-backoffice-primary mb-2",
        ),
        rx.heading(title, as_="h2", class_name="text-2xl font-serif text-on-surface leading-snug"),
        class_name="pt-1",
    )


def _label(text: str) -> rx.Component:
    return rx.text(
        text,
        class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant mb-1.5",
    )


def _input(placeholder: str) -> rx.Component:
    return rx.el.input(
        placeholder=placeholder,
        class_name=(
            "w-full border border-outline-variant/40 rounded-lg px-3 py-2.5 text-sm "
            "text-on-surface bg-white focus:ring-2 focus:ring-primary/20 outline-none transition-all"
        ),
    )


def _select(*options: str, default: str = "") -> rx.Component:
    return rx.box(
        rx.el.select(
            *[
                rx.el.option(opt, value=opt, selected=(opt == default))
                for opt in options
            ],
            class_name=(
                "w-full appearance-none border border-outline-variant/40 rounded-lg px-3 py-2.5 "
                "text-sm text-on-surface bg-white focus:ring-2 focus:ring-primary/20 outline-none "
                "transition-all cursor-pointer pr-10"
            ),
        ),
        rx.el.span(
            "keyboard_arrow_down",
            class_name=(
                "material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 "
                "text-on-surface-variant pointer-events-none text-base"
            ),
        ),
        class_name="relative w-full",
    )


def _textarea(placeholder: str) -> rx.Component:
    return rx.el.textarea(
        placeholder=placeholder,
        rows="5",
        class_name=(
            "w-full border border-outline-variant/40 rounded-lg px-3 py-2.5 text-sm "
            "text-on-surface bg-white focus:ring-2 focus:ring-primary/20 outline-none "
            "transition-all resize-none"
        ),
    )


def _form_card(*children: rx.Component) -> rx.Component:
    return rx.box(
        *children,
        class_name="bg-white rounded-2xl border border-outline-variant/20 p-6 flex flex-col gap-4 shadow-sm",
    )


def _divider() -> rx.Component:
    return rx.box(class_name="border-t border-outline-variant/20 my-10")


def _step_grid(num: str, title: str, form: rx.Component) -> rx.Component:
    return rx.grid(
        _step_label(num, title),
        form,
        columns="2",
        class_name="gap-12 items-start",
        style={"grid_template_columns": "2fr 3fr"},
    )


# ── Step 01 ──────────────────────────────────────────────────────────────────

def _step01() -> rx.Component:
    return _step_grid(
        "01", "Business\nInformation",
        _form_card(
            rx.box(_label("Business Name"), _input("e.g. Lumina Collective")),
            rx.box(
                _label("Business Type"),
                _select(
                    "Select type...",
                    "Coffee & Beverage",
                    "Quick Mart / Convenience",
                    "Restaurant",
                    "Retail Fashion",
                    "Pharmacy",
                    "Other",
                    default="Select type...",
                ),
            ),
            rx.box(_label("Description"), _textarea("Tell us about your brand's mission and story...")),
        ),
    )


# ── Step 02 ──────────────────────────────────────────────────────────────────

def _step02() -> rx.Component:
    return _step_grid(
        "02", "Investment",
        _form_card(
            rx.box(
                _label("Budget Range (Annual)"),
                _select(
                    "$50k - $100k", "$100k - $250k", "$250k - $500k", "$500k+",
                    default="$100k - $250k",
                ),
            ),
            rx.grid(
                rx.box(
                    _label("Preferred Store Size"),
                    _select(
                        "Small (Under 1,000 sqm)",
                        "Medium (1,000–3,000 sqm)",
                        "Large (3,000+ sqm)",
                        default="Small (Under 1,000 sqm)",
                    ),
                ),
                rx.box(
                    _label("Lease Duration"),
                    _select(
                        "Short Term (1–2 years)",
                        "Medium Term (3–5 years)",
                        "Long Term (5+ years)",
                        default="Short Term (1–2 years)",
                    ),
                ),
                columns="2",
                class_name="gap-4",
            ),
        ),
    )


# ── Step 03 ──────────────────────────────────────────────────────────────────

_DEMO_TAGS = ["Gen Z", "Millennials", "Gen X", "Baby Boomers", "Luxury Segment"]


def _chip(tag: str, selected: bool = False) -> rx.Component:
    base = "px-4 py-2 rounded-full border text-xs font-semibold cursor-pointer transition-all select-none"
    active = "bg-primary/10 border-primary text-primary"
    inactive = "border-outline-variant/40 text-on-surface-variant hover:border-primary/40 hover:text-on-surface"
    return rx.box(rx.text(tag), class_name=f"{base} {active if selected else inactive}")


def _step03() -> rx.Component:
    return _step_grid(
        "03", "Target Strategy",
        _form_card(
            rx.box(
                _label("Target Customer Demographic"),
                rx.flex(
                    *[_chip(t, selected=(t == "Gen Z")) for t in _DEMO_TAGS],
                    rx.box(
                        rx.text("+ Add New", class_name="text-xs font-semibold"),
                        class_name=(
                            "px-4 py-2 rounded-full border border-dashed border-outline-variant/40 "
                            "text-on-surface-variant cursor-pointer hover:border-primary/40 "
                            "transition-all select-none text-xs"
                        ),
                    ),
                    class_name="flex flex-wrap gap-2 mt-1",
                ),
            ),
            rx.box(
                _label("Preferred Location Type"),
                _select(
                    "High Street / Premium Retail",
                    "Shopping Mall",
                    "Transit Hub",
                    "Petrol Station Forecourt",
                    "Suburban Strip",
                    default="High Street / Premium Retail",
                ),
            ),
        ),
    )


# ── Step 04 ──────────────────────────────────────────────────────────────────

def _counter_box(label: str) -> rx.Component:
    return rx.box(
        _label(label),
        rx.text("0", class_name="text-4xl font-bold text-on-surface mt-1 mb-3"),
        rx.hstack(
            rx.box(
                rx.el.span("remove", class_name="material-symbols-outlined text-sm"),
                class_name=(
                    "w-7 h-7 rounded-full border border-outline-variant/40 flex items-center "
                    "justify-center cursor-pointer hover:bg-surface-container-low transition-colors"
                ),
            ),
            rx.box(
                rx.el.span("add", class_name="material-symbols-outlined text-sm"),
                class_name=(
                    "w-7 h-7 rounded-full border border-outline-variant/40 flex items-center "
                    "justify-center cursor-pointer hover:bg-surface-container-low transition-colors"
                ),
            ),
            class_name="flex items-center gap-2",
        ),
        class_name="flex flex-col",
    )


def _step04() -> rx.Component:
    return _step_grid(
        "04", "Experience",
        rx.box(
            rx.grid(
                rx.box(
                    _counter_box("Years of Experience"),
                    class_name="pr-6 border-r border-outline-variant/20",
                ),
                rx.box(
                    _counter_box("Existing Stores"),
                    class_name="pl-6",
                ),
                columns="2",
                class_name="gap-0",
            ),
            class_name="bg-white rounded-2xl border border-outline-variant/20 p-6 shadow-sm",
        ),
    )


# ── Step 05 ──────────────────────────────────────────────────────────────────

def _step05() -> rx.Component:
    return _step_grid(
        "05", "Brand Assets",
        _form_card(
            rx.box(
                rx.el.span(
                    "upload_file",
                    class_name="material-symbols-outlined text-3xl text-on-surface-variant mb-3",
                ),
                rx.text("Upload Brand Identity", class_name="text-sm font-bold text-on-surface mb-1"),
                rx.text(
                    "Drag and drop your brand guidelines, logo files, or lookbooks here (PDF, JPG, PNG)",
                    class_name="text-xs text-on-surface-variant text-center mb-4 leading-relaxed max-w-xs",
                ),
                rx.el.button(
                    "Browse Files",
                    class_name=(
                        "border border-primary text-primary text-xs font-bold px-5 py-2 "
                        "rounded-full bg-white hover:bg-primary/5 cursor-pointer transition-colors"
                    ),
                ),
                class_name=(
                    "border-2 border-dashed border-outline-variant/40 rounded-xl p-8 "
                    "flex flex-col items-center"
                ),
            ),
            rx.box(
                _label("Current Assets"),
                rx.hstack(
                    rx.box(
                        class_name="w-20 h-20 rounded-xl bg-surface-container",
                        style={"background": "url('/image/station-ptg-latphrao71.png') center/cover"},
                    ),
                    rx.box(
                        class_name="w-20 h-20 rounded-xl bg-surface-container",
                        style={"background": "url('/image/station-ptg-ramaix.png') center/cover"},
                    ),
                    rx.box(
                        rx.el.span("add_circle", class_name="material-symbols-outlined text-on-surface-variant text-xl mb-1"),
                        rx.text("ADD MORE", class_name="text-[9px] font-bold tracking-widest text-on-surface-variant"),
                        class_name=(
                            "w-20 h-20 rounded-xl border-2 border-dashed border-outline-variant/40 "
                            "flex flex-col items-center justify-center cursor-pointer "
                            "hover:border-primary/40 transition-colors"
                        ),
                    ),
                    class_name="flex items-center gap-3 mt-1",
                ),
            ),
        ),
    )


# ── Bottom action bar ─────────────────────────────────────────────────────────

def _bottom_bar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.el.button(
                "Save as Draft",
                class_name=(
                    "text-sm font-semibold text-on-surface-variant bg-transparent border-0 "
                    "cursor-pointer hover:text-on-surface transition-colors px-6 py-3"
                ),
            ),
            rx.el.button(
                "Complete Profile",
                on_click=AuthState.complete_profile,
                class_name="backoffice-btn-primary px-8 py-3 rounded-full border-0 cursor-pointer text-sm font-bold",
            ),
            class_name="flex items-center gap-4",
        ),
        class_name=(
            "fixed bottom-0 left-52 right-0 bg-white/95 backdrop-blur-sm "
            "border-t border-outline-variant/10 flex justify-end items-center px-8 py-4 z-30"
        ),
    )


# ── Page assembly ─────────────────────────────────────────────────────────────

def retailer_profile_setup_page_content() -> rx.Component:
    return rx.fragment(
        backoffice_layout(
            "profile_setup",
            rx.box(
                rx.box(
                    rx.heading(
                        "Retailer Profile Setup",
                        as_="h1",
                        class_name="text-4xl font-serif text-on-surface mb-2",
                    ),
                    rx.text(
                        "Configure your brand identity and requirements to match with premium "
                        "retail opportunities across our global marketplace.",
                        class_name="text-sm text-on-surface-variant leading-relaxed max-w-xl",
                    ),
                    class_name="mb-10",
                ),
                _step01(),
                _divider(),
                _step02(),
                _divider(),
                _step03(),
                _divider(),
                _step04(),
                _divider(),
                _step05(),
                rx.box(class_name="h-24"),
            ),
        ),
        _bottom_bar(),
    )
