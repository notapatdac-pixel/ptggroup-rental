import reflex as rx


def station_detail_tabs() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.button(
                "Overview",
                type="button",
                class_name="pb-4 text-sm font-bold border-b-2 border-primary text-on-surface cursor-pointer",
            ),
            rx.el.button(
                "Insights",
                type="button",
                class_name="pb-4 text-sm font-medium text-on-surface-variant hover:text-on-surface cursor-pointer",
            ),
            rx.el.button(
                "Spaces",
                type="button",
                class_name="pb-4 text-sm font-medium text-on-surface-variant hover:text-on-surface cursor-pointer",
            ),
            rx.el.button(
                rx.el.span("Analytics ", class_name=""),
                rx.el.span("lock", class_name="material-symbols-outlined text-sm"),
                type="button",
                class_name="pb-4 text-sm font-medium text-outline flex items-center gap-1.5 cursor-not-allowed",
            ),
            rx.el.button(
                rx.el.span("AI Insights ", class_name=""),
                rx.el.span("lock", class_name="material-symbols-outlined text-sm"),
                type="button",
                class_name="pb-4 text-sm font-medium text-outline flex items-center gap-1.5 cursor-not-allowed",
            ),
            class_name="flex gap-8 min-w-max",
        ),
        class_name="border-b border-outline-variant/10 mb-8 overflow-x-auto",
    )
