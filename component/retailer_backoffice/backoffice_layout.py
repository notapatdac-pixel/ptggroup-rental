import reflex as rx

from component.auth_state import AuthState
from component.landingpage.nav_bar import nav_bar

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
            rx.el.span(icon, class_name="material-symbols-outlined text-[18px]"),
            rx.text(label, class_name="text-sm font-medium"),
            class_name="flex items-center gap-3 px-5 py-2.5 w-full",
        ),
        href=href,
        class_name=(
            "no-underline w-full block transition-colors "
            + (
                "border-l-[3px] border-primary text-primary font-semibold bg-primary/5"
                if is_active
                else "border-l-[3px] border-transparent text-on-surface-variant "
                     "hover:bg-surface-container-low hover:text-on-surface"
            )
        ),
    )


def backoffice_sidebar(active: str) -> rx.Component:
    nav_links = [_sidebar_item(k, icon, label, href, active) for k, icon, label, href in _NAV_ITEMS]
    return rx.box(
        rx.box(
            rx.text(
                "Retailer",
                class_name="text-[10px] font-bold tracking-widest uppercase text-on-surface-variant/60 px-5 pt-4 pb-2",
            ),
            *nav_links,
            class_name="flex flex-col flex-1 pt-1",
        ),
        rx.box(
            rx.box(
                rx.hstack(
                    rx.el.span("logout", class_name="material-symbols-outlined text-[18px]"),
                    rx.text("Logout", class_name="text-sm font-medium"),
                    class_name="flex items-center gap-3 px-5 py-2.5",
                ),
                on_click=AuthState.logout,
                class_name="text-on-surface-variant hover:text-error transition-colors cursor-pointer w-full",
            ),
            class_name="border-t border-outline-variant/10 py-2",
        ),
        class_name=(
            "fixed left-0 top-20 bottom-0 w-52 bg-white/95 backdrop-blur-sm "
            "border-r border-outline-variant/10 flex flex-col z-40"
        ),
    )


def backoffice_layout(active: str, content: rx.Component) -> rx.Component:
    return rx.box(
        nav_bar(),
        backoffice_sidebar(active),
        rx.box(
            content,
            class_name="ml-52 mt-20 min-h-screen bg-surface-container-low p-8",
        ),
    )
