import reflex as rx

_NAV_ITEMS = [
    ("dashboard", "grid_view", "Dashboard", "/retailerdashboard"),
    ("performance", "trending_up", "Performance", "/retailerperformance"),
    ("ml_predictions", "hub", "ML Predictions", "/retailerml"),
    ("submit_data", "upload_file", "Submit Store Data", "/retailersubmitdata"),
    ("applications", "assignment", "My Applications", "/retailerapplications"),
    ("ai_advisor", "smart_toy", "AI Advisor", "/retaileraiadvisor"),
]


def _sidebar_item(key: str, icon: str, label: str, href: str, active: str) -> rx.Component:
    is_active = key == active
    return rx.link(
        rx.hstack(
            rx.el.span(icon, class_name="material-symbols-outlined text-[20px]"),
            rx.text(label, class_name="text-sm font-medium"),
            class_name="flex items-center gap-3 px-4 py-2.5 w-full",
        ),
        href=href,
        class_name=(
            "no-underline w-full block transition-colors "
            + (
                "border-l-[3px] border-backoffice-primary text-backoffice-primary font-semibold bg-backoffice-primary/5"
                if is_active
                else "border-l-[3px] border-transparent text-on-surface-variant hover:bg-surface-container-low hover:text-on-surface"
            )
        ),
    )


def backoffice_sidebar(active: str) -> rx.Component:
    nav_links = [_sidebar_item(k, icon, label, href, active) for k, icon, label, href in _NAV_ITEMS]
    return rx.box(
        rx.box(
            rx.link(
                rx.text("PTG Retailer", class_name="text-lg font-bold text-on-surface tracking-tight"),
                href="/retailerdashboard",
                class_name="no-underline",
            ),
            class_name="px-6 py-5 border-b border-outline-variant/20",
        ),
        rx.box(*nav_links, class_name="flex flex-col pt-3 pb-3 flex-1"),
        rx.box(
            rx.link(
                rx.hstack(
                    rx.el.span("logout", class_name="material-symbols-outlined text-[20px]"),
                    rx.text("Logout", class_name="text-sm font-medium"),
                    class_name="flex items-center gap-3 px-4 py-2.5",
                ),
                href="/loginpage",
                class_name="no-underline text-on-surface-variant hover:text-error transition-colors",
            ),
            class_name="border-t border-outline-variant/20 pb-2",
        ),
        class_name="fixed top-0 left-0 h-full w-[200px] bg-white border-r border-outline-variant/20 flex flex-col z-40",
    )


def backoffice_topnav() -> rx.Component:
    return rx.el.header(
        rx.hstack(
            rx.box(
                rx.el.span("search", class_name="material-symbols-outlined text-[18px] text-on-surface-variant absolute left-3 top-1/2 -translate-y-1/2"),
                rx.el.input(
                    placeholder="Search stores",
                    type="text",
                    class_name="w-full bg-transparent border-none outline-none text-sm pl-9 pr-3 py-2 text-on-surface placeholder-on-surface-variant/50",
                ),
                class_name="relative flex items-center bg-backoffice-search rounded-full w-48",
            ),
            rx.el.select(
                rx.el.option("All Stores"),
                class_name="bg-surface-container-low border border-outline-variant/30 rounded-full px-4 py-2 text-sm text-on-surface outline-none cursor-pointer",
            ),
            rx.hstack(
                rx.link("EXPLORE LOCATIONS", href="/explorepage", class_name="text-xs font-bold tracking-widest text-on-surface-variant hover:text-on-surface no-underline"),
                rx.link("PRICING", href="/pricingpage", class_name="text-xs font-bold tracking-widest text-on-surface-variant hover:text-on-surface no-underline"),
                class_name="flex items-center gap-6",
            ),
            rx.hstack(
                rx.el.button(
                    "Add Stores",
                    class_name="backoffice-btn-primary text-sm font-bold px-5 py-2 rounded-full cursor-pointer border-0",
                ),
                rx.el.button(
                    rx.el.span("notifications", class_name="material-symbols-outlined text-[20px]"),
                    class_name="bg-transparent border-0 cursor-pointer text-on-surface-variant hover:text-on-surface p-1",
                ),
                rx.el.button(
                    rx.el.span("account_circle", class_name="material-symbols-outlined text-[24px]"),
                    class_name="bg-transparent border-0 cursor-pointer text-on-surface-variant hover:text-on-surface p-1",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center gap-4 w-full justify-between",
        ),
        class_name="fixed top-0 left-[200px] right-0 h-14 bg-white border-b border-outline-variant/20 px-6 flex items-center z-30",
    )


def backoffice_layout(active: str, content: rx.Component) -> rx.Component:
    return rx.box(
        backoffice_sidebar(active),
        backoffice_topnav(),
        rx.box(
            content,
            class_name="ml-[200px] mt-14 min-h-screen bg-backoffice-surface p-8",
        ),
        class_name="bg-backoffice-surface",
    )
