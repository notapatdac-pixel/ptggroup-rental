import reflex as rx


def _pricing_plan_card(
    *,
    title: str,
    price: str,
    currency_suffix: str,
    subtitle: str,
    description: str,
    items: list[str],
    button_text: str,
    href: str,
    featured: bool = False,
) -> rx.Component:
    # Use the same plan styling language as the landing page preview cards.
    card_content = rx.fragment(
        rx.text(
            title,
            class_name=f"text-xs font-bold uppercase tracking-widest {'text-primary' if featured else 'text-on-surface-variant'} mb-4",
        ),
        rx.box(
            rx.hstack(
                rx.text(price, class_name="font-headline text-5xl text-on-surface"),
                rx.text(
                    currency_suffix,
                    class_name="text-on-surface-variant font-label text-sm uppercase tracking-wider",
                ),
                class_name="gap-1 items-baseline",
            ),
            rx.text(subtitle, class_name="text-on-surface-variant text-[10px] uppercase"),
            class_name="flex flex-col items-start mb-10",
        ),
        rx.text(description, class_name="text-on-surface-variant text-sm h-10 mb-2"),
        rx.el.ul(
            *[
                rx.el.li(
                    rx.hstack(
                        rx.el.span("check_circle", class_name="material-symbols-outlined text-primary text-xl"),
                        rx.text(item, class_name="text-sm"),
                        class_name="flex items-center gap-3",
                    )
                )
                for item in items
            ],
            class_name="space-y-4 mb-12 flex-grow",
        ),
        rx.link(
            button_text,
            href=href,
            class_name=(
                "w-full py-4 px-6 rounded-md font-bold text-xs tracking-widest uppercase transition-all cursor-pointer no-underline inline-flex items-center justify-center"
                + (
                    " primary-gradient text-on-primary shadow-lg shadow-primary/20 hover:brightness-110 active:scale-95"
                    if featured
                    else " bg-white border border-outline-variant/20 text-primary transition-colors hover:opacity-95"
                )
            ),
        ),
    )

    badge = rx.box(
        "Most Popular",
        class_name=(
            "absolute -top-4 left-1/2 -translate-x-1/2 bg-primary text-white text-[10px] "
            "font-bold px-4 py-1 rounded-full uppercase tracking-widest"
        ),
    )

    return rx.box(
        rx.cond(featured, badge, rx.fragment()),
        card_content,
        class_name=(
            "p-8 rounded-2xl border-2 border-primary flex flex-col relative h-full bg-surface-container-lowest scale-105 z-10"
            if featured
            else "p-8 rounded-2xl border border-outline-variant/20 flex flex-col h-full bg-surface-container-lowest"
        ),
    )


def pricing_cards_section() -> rx.Component:
    return rx.el.section(
        rx.grid(
            _pricing_plan_card(
                title="Free",
                price="0",
                currency_suffix="THB",
                subtitle="",
                description="Start exploring retail opportunities.",
                items=["Browse all listings", "Apply for 2 spaces"],
                button_text="Get started free",
                href="/createaccountpage",
            ),
            _pricing_plan_card(
                title="Pro",
                price="499",
                currency_suffix="THB",
                subtitle="/month",
                description="Unlock AI insights to find the best locations.",
                items=["Everything in Free", "AI recommendations", "Traffic analytics"],
                button_text="Start Pro",
                href="/checkoutpage/pro",
                featured=True,
            ),
            _pricing_plan_card(
                title="Growth",
                price="1,000",
                currency_suffix="THB",
                subtitle="/month",
                description="Full platform with ML predictions and analytics.",
                items=["Everything in Pro", "ML predictions", "Retailer dashboard"],
                button_text="Start Growth",
                href="/checkoutpage/growth",
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-8 mb-32 items-stretch max-w-7xl mx-auto",
        ),
    )

