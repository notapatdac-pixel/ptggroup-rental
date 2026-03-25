import reflex as rx


def traffic_trend_chart(station: dict) -> rx.Component:
    d = station["detail"]
    heights = d["chart_heights_pct"]
    peak_label = d["chart_peak_label"]
    peak_idx = max(range(len(heights)), key=lambda i: heights[i])
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    bars: list[rx.Component] = []
    for i, h in enumerate(heights):
        if i == peak_idx:
            inner = rx.el.div(
                rx.el.div(
                    peak_label,
                    class_name=(
                        "absolute -top-10 left-1/2 -translate-x-1/2 bg-on-surface text-white "
                        "text-[10px] py-1 px-2 rounded font-bold whitespace-nowrap"
                    ),
                ),
                class_name="w-full bg-primary rounded-t-sm relative cursor-pointer",
                style={"height": f"{h}%"},
            )
        else:
            inner = rx.el.div(
                class_name=(
                    "w-full bg-surface-container rounded-t-sm hover:bg-primary/20 "
                    "transition-all cursor-pointer"
                ),
                style={"height": f"{h}%"},
            )
        bars.append(rx.el.div(inner, class_name="w-full flex flex-col justify-end h-full min-h-0"))

    return rx.el.div(
        rx.el.div(
            rx.el.h4("Traffic Trend", class_name="font-headline text-2xl text-on-surface"),
            rx.el.span("Jan - Jun 2024", class_name="text-xs font-bold text-on-surface-variant"),
            class_name="flex justify-between items-center mb-8",
        ),
        rx.el.div(
            *bars,
            class_name="h-64 flex items-end justify-between gap-4 px-2",
        ),
        rx.el.div(
            *[
                rx.el.span(
                    m,
                    class_name="text-[10px] font-bold text-outline-variant uppercase tracking-widest",
                )
                for m in months
            ],
            class_name="flex justify-between mt-4 px-2",
        ),
        class_name=(
            "lg:col-span-2 h-full min-h-0 flex flex-col bg-surface-container-lowest p-8 rounded-xl "
            "editorial-shadow"
        ),
    )
