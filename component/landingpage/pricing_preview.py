import reflex as rx


def _plan(
    title: str,
    price: str,
    subtitle: str,
    items: list[str],
    button_text: str,
    featured: bool = False,
) -> rx.Component:
    item_rows = [
        rx.el.li(
            rx.hstack(
                rx.el.span("check_circle", class_name="material-symbols-outlined text-primary text-xl"),
                rx.text(item),
                class_name=f"flex items-center gap-3 text-sm {'text-on-surface' if featured else 'text-on-surface-variant'}",
            )
        )
        for item in items
    ]
    return rx.box(
        rx.cond(
            featured,
            rx.box(
                "Most Popular",
                class_name="absolute -top-4 left-1/2 -translate-x-1/2 bg-primary text-white text-[10px] font-bold px-4 py-1 rounded-full uppercase tracking-widest",
            ),
            rx.fragment(),
        ),
        rx.text(title, class_name=f"text-xs font-bold uppercase tracking-widest {'text-primary' if featured else 'text-on-surface-variant'} mb-4"),
        rx.text(
            rx.fragment(
                price,
                rx.el.span(f" {subtitle}", class_name="text-lg font-sans text-on-surface-variant"),
            ),
            class_name="text-4xl font-headline text-on-surface mb-8",
        ),
        rx.el.ul(*item_rows, class_name="space-y-4 mb-12 flex-grow"),
        rx.el.button(
            button_text,
            type="button",
            class_name=(
                "inline-flex items-center justify-center w-full py-4 rounded-md cursor-pointer font-bold "
                + (
                    "primary-gradient text-white border-0 shadow-lg transition-all hover:shadow-lime-500/40 hover:ring-2 hover:ring-lime-300 active:scale-95"
                    if featured
                    else (
                        "btn-lime-outline bg-white border border-primary text-primary transition-colors"
                        if title == "Starter"
                        else "btn-lime-outline bg-white border border-outline text-on-surface transition-colors"
                    )
                )
            ),
        ),
        class_name=(
            "p-8 rounded-2xl border-2 border-primary ring-4 ring-primary/5 flex flex-col h-full bg-surface-container-lowest relative scale-105 z-10"
            if featured
            else "p-8 rounded-2xl border border-outline-variant/20 flex flex-col h-full bg-surface-container-lowest"
        ),
    )


def pricing_preview() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                rx.heading("Choose Your Growth Path", as_="h2", class_name="text-5xl text-on-surface mb-6"),
                rx.text(
                    "Transparent plans designed for every stage of your retail business journey.",
                    class_name="text-on-surface-variant text-lg max-w-2xl mx-auto",
                ),
                class_name="text-center mb-24",
            ),
            rx.grid(
                _plan("Starter", "0", "THB /mo", ["Search all locations", "Basic site details", "Digital applications"], "Start for Free"),
                _plan(
                    "Professional",
                    "499",
                    "THB /mo",
                    [
                        "Everything in Starter",
                        "AI Recommendations",
                        "Advanced Traffic Heatmaps",
                        "Competitor proximity report",
                    ],
                    "Upgrade to Pro",
                    featured=True,
                ),
                _plan(
                    "Enterprise",
                    "1,000",
                    "THB /mo",
                    ["Everything in Pro", "ML Revenue Predictions", "Multi-site portfolio analysis", "API Access"],
                    "Contact Sales",
                ),
                class_name="grid md:grid-cols-3 gap-8",
            ),
            class_name="max-w-7xl mx-auto",
        ),
        class_name="py-32 px-8 bg-surface mb-12",
    )
