import reflex as rx


def _spec_status_class(status: str) -> str:
    if status == "VERIFIED":
        return "bg-secondary/10 text-secondary text-[10px] font-bold px-2 py-1 rounded"
    return "bg-primary/10 text-primary text-[10px] font-bold px-2 py-1 rounded"


def _spec_row(attr: str, detail: str, status: str) -> rx.Component:
    return rx.el.tr(
        rx.el.td(attr, class_name="px-8 py-5 font-bold text-on-surface text-sm"),
        rx.el.td(detail, class_name="px-8 py-5 text-on-surface-variant text-sm"),
        rx.el.td(
            rx.el.span(status, class_name=_spec_status_class(status)),
            class_name="px-8 py-5",
        ),
        class_name="hover:bg-surface-container-low transition-colors",
    )


def location_specification_table(station: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h4("Location Specification", class_name="font-headline text-2xl text-on-surface"),
            class_name="px-8 py-6 border-b border-outline-variant/10",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th("Attribute", class_name="px-8 py-4"),
                        rx.el.th("Details", class_name="px-8 py-4"),
                        rx.el.th("Status", class_name="px-8 py-4"),
                        class_name=(
                            "bg-surface-container-low text-[10px] font-black text-outline-variant uppercase tracking-widest"
                        ),
                    ),
                ),
                rx.el.tbody(
                    *[_spec_row(a, b, c) for a, b, c in station["detail"]["specs"]],
                    class_name="divide-y divide-outline-variant/5",
                ),
                class_name="w-full text-left",
            ),
            class_name="overflow-x-auto",
        ),
        class_name="bg-surface-container-lowest rounded-xl editorial-shadow overflow-hidden",
    )
