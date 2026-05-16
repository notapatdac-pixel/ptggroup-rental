import reflex as rx
from component.landlord_backoffice.landlord_layout import landlord_layout


def _intelligence_panel() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(class_name="w-2 h-2 rounded-full bg-secondary"),
            rx.text("LIVE INTELLIGENCE REPORT",
                    class_name="text-[10px] font-bold tracking-widests text-on-surface-variant"),
            class_name="flex items-center gap-2 mb-5",
        ),
        rx.hstack(
            rx.text("Your portfolio is performing ", class_name="text-2xl font-bold text-on-surface"),
            rx.text("14% above market", class_name="text-2xl font-bold font-headline italic text-primary"),
            rx.text(" in the Lat Phrao district.", class_name="text-2xl font-bold text-on-surface"),
            class_name="flex items-baseline flex-wrap gap-1 mb-6",
        ),
        rx.hstack(
            rx.box(
                rx.text("OCCUPANCY EFFICIENCY",
                        class_name="text-[10px] font-bold tracking-widest text-on-surface-variant mb-1"),
                rx.text("89.4%", class_name="text-3xl font-bold text-on-surface"),
            ),
            rx.box(class_name="w-px h-10 bg-outline-variant/30 mx-8"),
            rx.box(
                rx.text("RETAIL YIELD YOY",
                        class_name="text-[10px] font-bold tracking-widest text-on-surface-variant mb-1"),
                rx.text("+22%", class_name="text-3xl font-bold text-backoffice-primary"),
            ),
            class_name="flex items-center",
        ),
        class_name="bg-white rounded-2xl p-8 shadow-sm",
    )


def _expansion_card() -> rx.Component:
    return rx.box(
        rx.text("EXPANSION FORECAST",
                class_name="text-[10px] font-bold tracking-widests text-white/70 mb-3"),
        rx.heading("Projected Growth for Sukhumvit 62", as_="h3",
                   class_name="text-2xl font-bold text-white mb-3"),
        rx.text(
            "Based on local traffic patterns and the upcoming rail extension, this node shows a 35% increase in retail demand by Q4.",
            class_name="text-sm text-white/85 leading-relaxed mb-6",
        ),
        rx.el.button(
            "View Detailed Forecast",
            class_name=(
                "bg-white text-primary text-sm font-bold px-5 py-2.5 rounded-full "
                "border-0 cursor-pointer hover:bg-surface-container-low transition-colors"
            ),
        ),
        class_name="backoffice-accent-card h-full",
    )


def _recommendation_card(icon: str, title: str, body: str, cta: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.span(icon, class_name="material-symbols-outlined text-[22px] text-on-surface-variant"),
            class_name="w-10 h-10 bg-surface-container rounded-xl flex items-center justify-center mb-4",
        ),
        rx.text(title, class_name="text-base font-bold text-on-surface mb-2"),
        rx.text(body, class_name="text-sm text-on-surface-variant leading-relaxed mb-4 flex-1"),
        rx.link(
            cta,
            href="#",
            class_name="text-[11px] font-bold tracking-widest text-primary no-underline hover:underline",
        ),
        class_name="bg-white rounded-2xl p-6 shadow-sm flex flex-col",
    )


def _suggestion_chip(text: str) -> rx.Component:
    return rx.box(
        rx.text(f'"{text}"', class_name="text-sm text-on-surface"),
        class_name=(
            "bg-white border border-outline-variant rounded-full px-4 py-2 "
            "cursor-pointer hover:border-primary hover:text-primary transition-colors"
        ),
    )


def _chat_input() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.el.span("support_agent", class_name="material-symbols-outlined text-[20px] text-white fill-icon"),
                class_name="w-9 h-9 rounded-full backoffice-btn-primary flex items-center justify-center flex-shrink-0",
            ),
            rx.el.input(
                placeholder="Ask about regional trends...",
                class_name="flex-1 border-0 bg-transparent text-sm text-on-surface outline-none",
                style={"fontFamily": "DM Sans, sans-serif"},
            ),
            rx.box(
                rx.el.span("arrow_upward", class_name="material-symbols-outlined text-[20px] text-white"),
                class_name="w-9 h-9 rounded-full backoffice-btn-primary flex items-center justify-center cursor-pointer flex-shrink-0",
            ),
            class_name="flex items-center gap-3",
        ),
        class_name="bg-white rounded-full px-4 py-3 shadow-sm",
    )


def landlord_ai_advisor_page_content() -> rx.Component:
    return landlord_layout(
        "ai_advisor",
        rx.box(
            rx.heading("AI Landlord Advisor", as_="h1",
                       class_name="text-2xl font-bold text-on-surface mb-6"),
            rx.grid(
                _intelligence_panel(),
                _expansion_card(),
                columns="2",
                class_name="gap-6 mb-8",
                style={"gridTemplateColumns": "2fr 1fr"},
            ),
            rx.text("Strategic Recommendations",
                    class_name="text-lg font-bold text-on-surface mb-4"),
            rx.grid(
                _recommendation_card(
                    "groups",
                    "Optimize Tenant Mix for Lat Phrao 71",
                    "Current EV station dwell time suggests a 15% higher demand for quick-service retail than currently allocated.",
                    "IMPLEMENT NOW>",
                ),
                _recommendation_card(
                    "account_balance_wallet",
                    "Revenue Growth Opportunity",
                    "Dynamic pricing models for high-traffic weekend slots could increase secondary revenue streams by $4.2k/mo.",
                    "VIEW ANALYSIS>",
                ),
                _recommendation_card(
                    "security",
                    "Risk Mitigation",
                    "Localized power grid volatility detected in the Bang Kapi area. Recommend backup battery station expansion.",
                    "EVALUATE RISK>",
                ),
                columns="3",
                class_name="gap-4 mb-6",
            ),
            rx.box(
                _chat_input(),
                rx.hstack(
                    _suggestion_chip("Compare yield with Nonthaburi"),
                    _suggestion_chip("Best performing retail tenant"),
                    _suggestion_chip("Forecast for 2025 expansion"),
                    class_name="flex items-center gap-3 mt-4 flex-wrap",
                ),
                class_name="bg-surface-container-low rounded-2xl p-6",
            ),
        ),
    )
