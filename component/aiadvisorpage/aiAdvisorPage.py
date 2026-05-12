import reflex as rx

from component.backoffice.backoffice_layout import backoffice_layout


def _recommendation_card(icon: str, title: str, desc: str, cta: str) -> rx.Component:
    return rx.box(
        rx.el.span(icon, class_name="material-symbols-outlined text-backoffice-primary text-2xl mb-3"),
        rx.text(title, class_name="text-sm font-bold text-on-surface mb-2"),
        rx.text(desc, class_name="text-xs text-on-surface-variant leading-relaxed mb-4"),
        rx.link(cta, href="#", class_name="text-xs font-bold text-backoffice-primary no-underline hover:underline"),
        class_name="bg-white rounded-2xl p-5 shadow-sm flex flex-col",
    )


def _prompt_chip(label: str) -> rx.Component:
    return rx.el.button(
        label,
        class_name="backoffice-time-chip text-xs",
    )


def ai_advisor_page_content() -> rx.Component:
    return backoffice_layout(
        "ai_advisor",
        rx.box(
            rx.heading("AI Retailer Advisor", as_="h1", class_name="text-2xl font-bold text-on-surface mb-6"),
            rx.hstack(
                rx.box(
                    rx.hstack(
                        rx.box(class_name="w-2 h-2 rounded-full bg-[#4a7c2f] animate-pulse"),
                        rx.text("LIVE INTELLIGENCE REPORT", class_name="text-[10px] font-bold tracking-widest uppercase text-backoffice-primary"),
                        class_name="flex items-center gap-2 mb-3",
                    ),
                    rx.text(
                        "Your Coffee Corner segment is performing 18% above rolling average.",
                        class_name="text-2xl font-bold text-on-surface leading-snug mb-3",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.text("CUSTOMER SCORE", class_name="text-[9px] text-white/60 font-bold tracking-widest uppercase mb-1"),
                            rx.text("92", class_name="text-3xl font-bold text-white"),
                        ),
                        rx.box(
                            rx.text("IN-STORE GROWTH", class_name="text-[9px] text-white/60 font-bold tracking-widest uppercase mb-1"),
                            rx.text("+18%", class_name="text-3xl font-bold text-white"),
                        ),
                        class_name="flex gap-8",
                    ),
                    class_name="bg-white rounded-2xl p-6 shadow-sm flex-1",
                ),
                rx.box(
                    rx.text("Projected Q4 Shift in Consumer Behavior", class_name="text-sm font-bold text-white mb-2"),
                    rx.text(
                        "AI models detect a 12% shift in weekday traffic patterns towards health-forward convenience items. Early adoption could accelerate market share in Q4.",
                        class_name="text-xs text-white/80 leading-relaxed mb-4",
                    ),
                    rx.el.button(
                        "View Strategy Forecast →",
                        class_name="bg-white text-backoffice-primary text-xs font-bold px-4 py-2 rounded-lg border-0 cursor-pointer",
                    ),
                    class_name="backoffice-accent-card w-64 flex-shrink-0",
                ),
                class_name="flex items-stretch gap-4 mb-6",
            ),
            rx.box(
                rx.text("Strategic Recommendations", class_name="text-base font-bold text-on-surface mb-4"),
                rx.grid(
                    _recommendation_card(
                        "event_available",
                        "Optimize Saturday Demand",
                        "Saturday traffic is trending to handle 15% higher referrals by optimizing peak foot traffic allocation.",
                        "Implement →",
                    ),
                    _recommendation_card(
                        "local_offer",
                        "Dynamic Bundling Opportunity",
                        "Two coffee + snack bundles during the 09:00-11:00 window to increase cross-spending consumer volume.",
                        "Explore more",
                    ),
                    _recommendation_card(
                        "apartment",
                        "Rama 9 Real Estate Expansion",
                        "This commercial zone area identified with a 300% status of its top-performing cluster — top-tier category.",
                        "New Insight",
                    ),
                    columns="3",
                    class_name="gap-4",
                ),
                class_name="mb-6",
            ),
            rx.box(
                rx.hstack(
                    rx.el.span("smart_toy", class_name="material-symbols-outlined text-backoffice-primary text-xl flex-shrink-0"),
                    rx.el.input(
                        placeholder="Ask about regional trends...",
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
