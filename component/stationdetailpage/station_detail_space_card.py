import reflex as rx

from component.stationdetailpage.station_detail_styles import BTN_LANDING_PRIMARY_BLOCK


def space_card(unit: str, name: str, price: str, desc: str, img: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=img,
                alt=name,
                class_name="w-full h-full object-cover opacity-90 group-hover:scale-105 transition-transform duration-500",
            ),
            rx.el.div(
                rx.el.span(
                    unit,
                    class_name="bg-on-surface/80 backdrop-blur-md text-white text-[10px] font-bold px-2 py-1 rounded",
                ),
                class_name="absolute top-4 left-4",
            ),
            class_name="h-48 bg-surface-container relative overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h5(name, class_name="font-bold text-lg text-on-surface"),
                rx.el.p(
                    rx.el.span(price, class_name="text-primary font-bold"),
                    rx.el.span(" THB/mo", class_name="text-xs text-on-surface-variant font-normal"),
                    class_name="text-primary font-bold",
                ),
                class_name="flex justify-between items-start mb-2",
            ),
            rx.el.p(desc, class_name="text-sm text-on-surface-variant mb-6 line-clamp-2"),
            rx.el.button("Apply Now", type="button", class_name=BTN_LANDING_PRIMARY_BLOCK),
            class_name="p-6",
        ),
        class_name=(
            "group bg-surface-container-lowest rounded-xl editorial-shadow overflow-hidden "
            "border border-transparent hover:border-primary/20 transition-all"
        ),
    )
