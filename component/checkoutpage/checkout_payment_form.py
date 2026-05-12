import reflex as rx

_INPUT_CLS = (
    "w-full bg-surface-container-low border border-outline-variant/30 rounded-lg "
    "px-4 py-3 text-on-surface placeholder-on-surface-variant/50 outline-none "
    "focus:ring-2 focus:ring-primary/20 transition-all text-sm"
)
_LABEL_CLS = "text-[10px] uppercase font-bold tracking-widest text-on-surface-variant mb-2 block"


def _field(label: str, placeholder: str, input_type: str = "text") -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name=_LABEL_CLS),
        rx.el.input(placeholder=placeholder, type=input_type, class_name=_INPUT_CLS),
        class_name="flex flex-col",
    )


def _stripe_card_element() -> rx.Component:
    """Stripe Card Element mount point — Stripe.js renders the secure iframe here."""
    return rx.el.div(
        rx.el.label("CARD DETAILS", class_name=_LABEL_CLS),
        rx.el.div(
            id="ptg-stripe-card-element",
            class_name=(
                "bg-surface-container-low border border-outline-variant/30 rounded-lg "
                "px-4 py-3.5 min-h-[46px]"
            ),
        ),
        rx.el.div(
            id="ptg-stripe-card-errors",
            role="alert",
            class_name="text-xs text-error mt-1.5 hidden",
        ),
        class_name="flex flex-col",
    )


def checkout_payment_form(plan: dict) -> rx.Component:
    save_checkbox = rx.hstack(
        rx.el.input(
            type="checkbox",
            id=f"ptg-save-payment-{plan['id']}",
            class_name="w-4 h-4 rounded border-outline-variant/40 accent-primary cursor-pointer",
        ),
        rx.text(
            "Save payment information for faster checkout next time.",
            class_name="text-on-surface-variant text-sm",
        ),
        class_name="flex items-center gap-3",
    ) if plan["show_save_checkbox"] else rx.fragment()

    gateway_note = rx.hstack(
        rx.el.span("lock", class_name="material-symbols-outlined text-on-surface-variant/50 text-base"),
        rx.text(plan["gateway_text"], class_name="text-on-surface-variant text-xs"),
        class_name="flex items-center justify-center gap-1.5",
    ) if plan["show_gateway_note"] else rx.fragment()

    legal = rx.text(
        plan["legal_text"],
        class_name="text-on-surface-variant/70 text-xs text-center leading-relaxed",
    ) if plan["show_legal_text"] else rx.fragment()

    card_icons = rx.hstack(
        rx.el.span("credit_card", class_name="material-symbols-outlined text-on-surface-variant/40 text-4xl"),
        rx.el.span("credit_card", class_name="material-symbols-outlined text-red-400/50 text-4xl"),
        rx.el.span("credit_card", class_name="material-symbols-outlined text-blue-400/50 text-4xl"),
        class_name="flex justify-center gap-3 pt-2",
    ) if plan["show_card_icons"] else rx.fragment()

    media_images = rx.el.div(
        rx.image(
            src="/image/checkout-payment-terminal.jpg",
            alt="Payment terminal",
            class_name="w-full h-40 object-cover rounded-xl",
        ),
        rx.image(
            src="/image/checkout-analytics-tablet.jpg",
            alt="Analytics dashboard",
            class_name="w-full h-40 object-cover rounded-xl",
        ),
        class_name="grid grid-cols-2 gap-4",
    ) if plan["show_media_images"] else rx.fragment()

    return rx.box(
        rx.heading(
            "Payment Details",
            as_="h2",
            class_name="font-headline text-3xl text-on-surface mb-8",
        ),
        rx.el.div(
            _field("CARDHOLDER NAME", "Johnathan Analyst"),
            _stripe_card_element(),
            save_checkbox,
            rx.el.button(
                plan["pay_label"],
                id=f"ptg-pay-btn-{plan['id']}",
                type="button",
                class_name=(
                    "w-full primary-gradient text-on-primary font-bold py-4 rounded-xl "
                    "text-base shadow-lg shadow-primary/20 hover:brightness-110 "
                    "active:scale-95 transition-all cursor-pointer border-0"
                ),
            ),
            gateway_note,
            legal,
            card_icons,
            media_images,
            class_name="flex flex-col gap-5",
        ),
        class_name="bg-white rounded-2xl p-8 shadow-sm",
    )
