import reflex as rx

from component.stationdetailpage.station_detail_styles import BTN_LANDING_PRIMARY_ON_DARK


def station_pro_insights_card(_station: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                "Pro Access",
                class_name=(
                    "bg-lime-400/90 text-on-primary-container text-[10px] font-black px-2 py-0.5 rounded "
                    "uppercase tracking-wider mb-4 inline-block"
                ),
            ),
            rx.el.h4(
                "Unlock Granular AI Insights",
                class_name="font-headline text-2xl md:text-3xl mb-3 leading-tight text-white",
            ),
            rx.el.p(
                "Get predictive analytics on fuel prices, competitor heatmaps, and hourly visitor forecasting.",
                class_name="text-white/70 text-sm mb-8 leading-relaxed",
            ),
            rx.el.button("Start 14-Day Pro Trial", type="button", class_name=BTN_LANDING_PRIMARY_ON_DARK),
            class_name="relative z-10 p-8 h-full flex flex-col justify-between flex-1 min-h-0",
        ),
        class_name=(
            "relative h-full min-h-0 flex flex-col rounded-xl overflow-hidden border border-white/10 "
            "bg-black shadow-lg"
        ),
    )
