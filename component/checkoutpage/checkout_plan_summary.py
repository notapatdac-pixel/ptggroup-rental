import reflex as rx


def _feature_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.el.span("check_circle", class_name="material-symbols-outlined fill-icon text-primary text-xl flex-shrink-0"),
        rx.text(text, class_name="text-on-surface text-sm"),
        class_name="flex items-center gap-3",
    )


def _security_card(plan: dict) -> rx.Component:
    """Inline security badge used inside the Growth Plan card."""
    return rx.hstack(
        rx.el.span("shield", class_name="material-symbols-outlined text-on-surface-variant text-3xl flex-shrink-0"),
        rx.box(
            rx.text(
                plan["security_eyebrow"],
                class_name="text-[10px] uppercase font-bold tracking-widest text-on-surface-variant mb-0.5",
            ) if plan["security_eyebrow"] else rx.fragment(),
            rx.text(plan["security_text"], class_name="text-sm font-bold text-on-surface"),
            class_name="flex flex-col",
        ),
        class_name="flex items-center gap-4 bg-surface-container-low rounded-xl px-5 py-4 mt-6",
    )


def _security_note_inline(plan: dict) -> rx.Component:
    """Security note below the Pro Plan inner card (no eyebrow)."""
    return rx.hstack(
        rx.el.span("shield", class_name="material-symbols-outlined text-on-surface-variant flex-shrink-0"),
        rx.text(plan["security_text"], class_name="text-on-surface-variant text-sm leading-relaxed"),
        class_name="flex items-start gap-3 bg-surface-container-low rounded-xl px-5 py-4",
    )


def checkout_plan_summary(plan: dict) -> rx.Component:
    features = [_feature_item(f) for f in plan["features"]]

    if plan["mode"] == "card":
        return rx.box(
            rx.heading(
                plan["title"],
                as_="h2",
                class_name="font-headline text-4xl text-on-surface mb-2",
            ),
            rx.text(
                plan["tagline"],
                class_name="text-on-surface-variant text-sm leading-relaxed mb-6",
            ),
            rx.hstack(
                rx.text(
                    plan["price"],
                    class_name="font-headline text-7xl font-bold text-on-surface leading-none",
                ),
                rx.text(
                    plan["price_unit"],
                    class_name="text-lg text-on-surface-variant self-end pb-2 ml-1",
                ),
                class_name="flex items-end",
            ),
            rx.el.hr(class_name="border-outline-variant/20 my-6"),
            rx.box(*features, class_name="flex flex-col gap-3"),
            _security_card(plan),
            class_name="bg-white rounded-2xl p-8 shadow-sm",
        )

    # split mode — Pro Plan
    order_summary = rx.box(
        rx.el.hr(class_name="border-outline-variant/20 mb-4"),
        rx.hstack(
            rx.text(plan["vat_label"], class_name="text-on-surface-variant text-sm"),
            rx.text(plan["vat"], class_name="text-on-surface text-sm"),
            class_name="flex justify-between mb-2",
        ),
        rx.hstack(
            rx.text("Subtotal", class_name="text-on-surface-variant text-sm"),
            rx.text(plan["subtotal"], class_name="text-on-surface text-sm"),
            class_name="flex justify-between mb-3",
        ),
        rx.hstack(
            rx.text("Total", class_name="text-on-surface font-bold"),
            rx.text(plan["total"], class_name="text-on-surface font-bold"),
            class_name="flex justify-between",
        ),
    ) if plan["show_order_summary"] else rx.fragment()

    inner_card = rx.box(
        rx.hstack(
            rx.text(
                plan["badge"],
                class_name="text-[10px] font-bold uppercase tracking-wider text-lime-800 bg-lime-200/70 px-3 py-1 rounded-full",
            ),
            rx.text(
                f"{plan['price']} THB",
                class_name="font-headline text-2xl font-bold text-primary",
            ),
            class_name="flex items-center justify-between mb-2",
        ),
        rx.hstack(
            rx.heading(
                plan["inner_plan_name"],
                as_="h3",
                class_name="font-headline text-xl text-on-surface",
            ),
            rx.text(
                plan["price_unit"],
                class_name="text-on-surface-variant text-sm",
            ),
            class_name="flex items-baseline justify-between mb-5",
        ),
        rx.box(*features, class_name="flex flex-col gap-3"),
        order_summary,
        class_name="bg-white rounded-2xl p-6 shadow-sm mb-4",
    )

    return rx.box(
        rx.heading(
            plan["title"],
            as_="h1",
            class_name="font-headline text-5xl text-on-surface mb-3 leading-tight",
        ),
        rx.text(plan["tagline"], class_name="text-on-surface-variant mb-6"),
        inner_card,
        _security_note_inline(plan),
    )
