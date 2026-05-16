import reflex as rx

from component.retailer_backoffice.backoffice_layout import backoffice_layout



def _prompt_chip(label: str) -> rx.Component:
    return rx.el.button(
        label,
        class_name="backoffice-time-chip text-xs",
    )


def ai_advisor_page_content() -> rx.Component:
    return backoffice_layout(
        "ai_advisor",
        rx.box(
            rx.hstack(
                rx.box(
                    rx.heading("AI Retailer Advisor", as_="h1", class_name="text-2xl font-bold text-on-surface"),
                    rx.text("Get personalized insights and recommendations for your retail operations.", class_name="text-sm text-on-surface-variant mt-1"),
                ),
                class_name="flex justify-between items-start mb-6",
            ),
            rx.box(
                rx.vstack(
                    rx.el.span("smart_toy", class_name="material-symbols-outlined text-5xl text-on-surface-variant/20 mb-4"),
                    rx.text("How can I help you today?", class_name="text-lg font-bold text-on-surface mb-1"),
                    rx.text(
                        "Ask me about your store performance, market trends, or expansion opportunities.",
                        class_name="text-sm text-on-surface-variant text-center max-w-sm leading-relaxed",
                    ),
                    class_name="flex flex-col items-center",
                ),
                class_name="bg-white rounded-2xl shadow-sm mb-4 flex items-center justify-center min-h-[360px]",
            ),
            rx.box(
                rx.hstack(
                    rx.el.span("smart_toy", class_name="material-symbols-outlined text-backoffice-primary text-xl flex-shrink-0"),
                    rx.el.input(
                        placeholder="Ask about regional trends, store performance, or expansion...",
                        class_name="flex-1 bg-transparent border-none outline-none text-sm text-on-surface placeholder-on-surface-variant/50",
                    ),
                    rx.el.button(
                        rx.el.span("send", class_name="material-symbols-outlined text-white text-base"),
                        class_name="backoffice-btn-primary rounded-full w-9 h-9 border-0 cursor-pointer flex items-center justify-center",
                    ),
                    class_name="flex items-center gap-3 mb-3",
                ),
                rx.hstack(
                    _prompt_chip("What are my competitors doing?"),
                    _prompt_chip("What is my top retail consultant?"),
                    _prompt_chip("Identify saturation in market"),
                    class_name="flex flex-wrap gap-2",
                ),
                class_name="bg-white rounded-2xl p-5 shadow-sm",
            ),
        ),
    )

