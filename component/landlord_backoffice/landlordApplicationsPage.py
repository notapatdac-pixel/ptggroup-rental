import reflex as rx
from component.landlord_backoffice.landlord_layout import landlord_layout


def _financial_bar(fill: int) -> rx.Component:
    return rx.box(
        rx.box(class_name="backoffice-progress-fill h-full", style={"width": f"{fill}%"}),
        class_name="backoffice-progress-track",
        style={"width": "32px", "height": "6px"},
    )


def _financial_health() -> rx.Component:
    return rx.box(
        rx.text("FINANCIAL HEALTH", class_name="text-[9px] font-bold tracking-widest text-on-surface-variant mb-2"),
        rx.hstack(
            _financial_bar(90),
            _financial_bar(75),
            _financial_bar(85),
            _financial_bar(60),
            class_name="flex gap-1.5",
        ),
        class_name="bg-surface-container-low rounded-xl p-3",
    )


def _ai_badge() -> rx.Component:
    return rx.hstack(
        rx.el.span("auto_awesome", class_name="material-symbols-outlined text-[14px] text-primary fill-icon"),
        rx.text("AI RECOMMENDATION", class_name="text-[9px] font-bold tracking-widest text-primary"),
        class_name="flex items-center gap-1 mb-2",
    )


def _applicant_card(
    name: str,
    category: str,
    experience: str,
    ai_score: str,
    ai_score_color: str,
    ai_text: str,
    revenue: str,
    traffic: str,
    image_placeholder_color: str,
) -> rx.Component:
    return rx.box(
        rx.hstack(
            # Left: portrait photo placeholder
            rx.box(
                rx.box(
                    rx.box(
                        rx.text(category, class_name="text-[10px] font-bold text-white bg-on-surface/70 px-2.5 py-1 rounded-full"),
                        class_name="absolute bottom-12 left-4",
                    ),
                    rx.text(name, class_name="absolute bottom-4 left-4 text-lg font-bold text-white"),
                    class_name="relative w-full h-full",
                ),
                class_name="w-48 flex-shrink-0 rounded-l-2xl relative overflow-hidden",
                style={"backgroundColor": image_placeholder_color, "minHeight": "220px"},
            ),
            # Right: details
            rx.box(
                rx.grid(
                    rx.box(
                        rx.text("EXPERIENCE", class_name="text-[9px] font-bold tracking-widest text-on-surface-variant mb-0.5"),
                        rx.text(experience, class_name="text-base font-bold text-on-surface"),
                    ),
                    rx.box(
                        rx.text("AI MATCH SCORE", class_name="text-[9px] font-bold tracking-widest text-on-surface-variant mb-0.5"),
                        rx.hstack(
                            rx.text(ai_score, class_name=f"text-base font-bold {ai_score_color}"),
                            rx.el.span("verified", class_name=f"material-symbols-outlined text-[16px] fill-icon {ai_score_color}"),
                            class_name="flex items-center gap-1",
                        ),
                    ),
                    rx.box(
                        rx.text("EST. REVENUE", class_name="text-[9px] font-bold tracking-widest text-on-surface-variant mb-0.5"),
                        rx.text(revenue, class_name="text-base font-bold text-on-surface"),
                        rx.text("THB/mo", class_name="text-[10px] text-on-surface-variant"),
                    ),
                    rx.box(
                        rx.text("FOOT TRAFFIC", class_name="text-[9px] font-bold tracking-widest text-on-surface-variant mb-0.5"),
                        rx.text(traffic, class_name="text-base font-bold text-backoffice-primary"),
                        rx.text("impact", class_name="text-[10px] text-on-surface-variant"),
                    ),
                    columns="4",
                    class_name="gap-6 mb-4",
                ),
                rx.grid(
                    rx.box(
                        _ai_badge(),
                        rx.text(ai_text, class_name="text-sm text-on-surface-variant leading-relaxed"),
                        class_name="bg-surface-container-low rounded-xl p-4",
                    ),
                    _financial_health(),
                    columns="2",
                    class_name="gap-4 mb-4",
                ),
                rx.hstack(
                    rx.el.button(
                        "DECLINE",
                        class_name=(
                            "text-sm font-bold tracking-wide text-on-surface-variant bg-transparent border-0 "
                            "cursor-pointer hover:text-error transition-colors px-4"
                        ),
                    ),
                    rx.el.button(
                        "APPROVE TENANT",
                        class_name="backoffice-btn-primary border-0 rounded-full px-6 py-2.5 text-sm font-bold cursor-pointer",
                    ),
                    class_name="flex items-center justify-end gap-2",
                ),
                class_name="flex-1 p-6 flex flex-col justify-between",
            ),
            class_name="flex",
        ),
        class_name="bg-white rounded-2xl shadow-sm overflow-hidden mb-5",
    )


def landlord_applications_page_content() -> rx.Component:
    return landlord_layout(
        "applications",
        rx.box(
            rx.hstack(
                rx.box(
                    rx.hstack(
                        rx.heading("Tenant ", as_="h1",
                                   class_name="text-3xl font-bold text-on-surface"),
                        rx.heading("Applications", as_="h1",
                                   class_name="text-3xl font-bold font-headline italic text-primary"),
                        class_name="flex items-baseline gap-0",
                    ),
                    rx.text("Reviewing 24 active candidates for Station Alpha-7",
                            class_name="text-sm text-on-surface-variant mt-1"),
                ),
                rx.hstack(
                    rx.text("FILTER BY", class_name="text-xs font-bold tracking-widest text-on-surface-variant"),
                    rx.hstack(
                        rx.text("Highest AI Match", class_name="text-sm text-on-surface"),
                        rx.el.span("expand_more", class_name="material-symbols-outlined text-[18px] text-on-surface-variant"),
                        class_name="flex items-center gap-1 bg-surface-container-low rounded-full px-4 py-2 cursor-pointer",
                    ),
                    class_name="flex items-center gap-3 bg-white rounded-full px-5 py-3 shadow-sm",
                ),
                class_name="flex items-start justify-between mb-8",
            ),
            _applicant_card(
                "Wanida Suthep", "ARTISAN CAFE",
                "12 Years", "89%", "text-backoffice-primary",
                "High potential for morning commuter synergy. Proximity to EV chargers aligns with customer dwell times of 20-30 minutes.",
                "14.2k", "+18%",
                "#4a5568",
            ),
            _applicant_card(
                "Tanaka Foods Co.", "PREMIUM RETAIL",
                "25 Years", "94%", "text-secondary",
                "Enterprise-grade tenant with stable long-term outlook. Ideal for high-density residential surroundings.",
                "32.8k", "+31%",
                "#744210",
            ),
            _applicant_card(
                "PharmaCare Ltd.", "PHARMACY",
                "8 Years", "76%", "text-on-surface-variant",
                "Service-oriented anchor. May require specialized ventilation and security infrastructure upgrades.",
                "21.5k", "+12%",
                "#1a4a5e",
            ),
        ),
    )
