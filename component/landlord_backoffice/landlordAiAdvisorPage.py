import reflex as rx
from component.landlord_backoffice.landlord_layout import landlord_layout


def _prompt_chip(label: str) -> rx.Component:
    return rx.el.button(
        label,
        class_name=(
            "backoffice-time-chip text-xs px-4 py-2 rounded-full border border-outline-variant "
            "bg-white text-on-surface cursor-pointer hover:border-primary hover:text-primary transition-colors"
        ),
    )


def landlord_ai_advisor_page_content() -> rx.Component:
    return landlord_layout(
        "ai_advisor",
        rx.box(
            rx.hstack(
                rx.box(
                    rx.heading("AI Landlord Advisor", as_="h1",
                               class_name="text-2xl font-bold text-on-surface"),
                    rx.text(
                        "Get personalized insights on portfolio performance, tenant management, and revenue optimization.",
                        class_name="text-sm text-on-surface-variant mt-1",
                    ),
                ),
                class_name="flex justify-between items-start mb-6",
            ),
            rx.box(
                rx.vstack(
                    rx.el.span("smart_toy", class_name="material-symbols-outlined text-5xl text-on-surface-variant/20 mb-4"),
                    rx.text(
                        "How can I help you today?",
                        class_name="text-xl font-bold text-on-surface mb-2",
                    ),
                    rx.text(
                        "Ask me about your portfolio performance, tenant health, or rental market trends.",
                        class_name="text-sm text-on-surface-variant text-center max-w-sm",
                    ),
                    class_name="flex flex-col items-center justify-center",
                ),
                class_name="bg-white rounded-2xl shadow-sm mb-4 flex items-center justify-center min-h-[360px]",
            ),
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.el.span("support_agent", class_name="material-symbols-outlined text-[20px] text-white fill-icon"),
                        class_name="w-9 h-9 rounded-full backoffice-btn-primary flex items-center justify-center flex-shrink-0",
                    ),
                    rx.el.input(
                        placeholder="Ask about your portfolio, tenants, or revenue trends...",
                        class_name="flex-1 border-0 bg-transparent text-sm text-on-surface outline-none",
                        style={"fontFamily": "DM Sans, sans-serif"},
                    ),
                    rx.box(
                        rx.el.span("arrow_upward", class_name="material-symbols-outlined text-[20px] text-white"),
                        class_name="w-9 h-9 rounded-full backoffice-btn-primary flex items-center justify-center cursor-pointer flex-shrink-0",
                    ),
                    class_name="flex items-center gap-3 bg-surface-container-low rounded-full px-4 py-3 mb-4",
                ),
                rx.hstack(
                    _prompt_chip("Optimize tenant mix for Lat Phrao 71"),
                    _prompt_chip("Best performing station this month"),
                    _prompt_chip("Forecast Q4 rental revenue"),
                    _prompt_chip("Upcoming lease renewals"),
                    class_name="flex items-center gap-3 flex-wrap",
                ),
                class_name="bg-white rounded-2xl p-5 shadow-sm",
            ),
        ),
    )
