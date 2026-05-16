import reflex as rx
from component.landlord_backoffice.landlord_layout import landlord_layout


def _ai_badge() -> rx.Component:
    return rx.hstack(
        rx.el.span("auto_awesome", class_name="material-symbols-outlined text-[14px] text-primary fill-icon"),
        rx.text("AI RECOMMENDATION", class_name="text-[9px] font-bold tracking-widest text-primary"),
        class_name="flex items-center gap-1 mb-2",
    )


def _applicant_card(
    name: str,
    store_name: str,
    category: str,
    experience: str,
    ai_score: str,
    ai_score_color: str,
    ai_text: str,
    revenue: str,
    image_placeholder_color: str,
) -> rx.Component:
    return rx.box(
        rx.hstack(
            # Left: portrait image panel
            rx.box(
                rx.box(
                    rx.text(
                        category,
                        class_name="text-[10px] font-bold text-white bg-black/50 backdrop-blur-sm px-2.5 py-1 rounded-full",
                    ),
                    class_name="absolute top-4 left-4 z-10",
                ),
                rx.box(
                    rx.text(store_name, class_name="text-base font-bold text-white leading-tight"),
                    rx.hstack(
                        rx.el.span("person", class_name="material-symbols-outlined text-[13px] text-white/70"),
                        rx.text(name, class_name="text-xs text-white/80"),
                        class_name="flex items-center gap-1 mt-1",
                    ),
                    class_name=(
                        "absolute bottom-0 left-0 right-0 px-4 py-4 z-10 "
                        "bg-gradient-to-t from-black/70 to-transparent"
                    ),
                ),
                class_name="w-52 flex-shrink-0 rounded-l-2xl relative overflow-hidden self-stretch",
                style={"backgroundColor": image_placeholder_color},
            ),
            # Right: details
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.text(store_name, class_name="text-lg font-bold text-on-surface"),
                        rx.text(name, class_name="text-xs text-on-surface-variant mt-0.5"),
                    ),
                    rx.box(
                        rx.text(category, class_name="text-[10px] font-bold tracking-wide text-primary border border-primary/30 bg-primary/5 px-2.5 py-1 rounded-full"),
                    ),
                    class_name="flex items-start justify-between mb-5",
                ),
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
                    columns="3",
                    class_name="gap-6 mb-4",
                ),
                rx.box(
                    _ai_badge(),
                    rx.text(ai_text, class_name="text-sm text-on-surface-variant leading-relaxed"),
                    class_name="bg-surface-container-low rounded-xl p-4 mb-4",
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
            class_name="flex items-stretch",
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
                name="Wanida Suthep",
                store_name="The Artisan Brew",
                category="ARTISAN CAFE",
                experience="12 Years",
                ai_score="89%",
                ai_score_color="text-backoffice-primary",
                ai_text="High potential for morning commuter synergy. Proximity to EV chargers aligns with customer dwell times of 20-30 minutes.",
                revenue="14,200",
                image_placeholder_color="#4a5568",
            ),
            _applicant_card(
                name="Tanaka Foods Co.",
                store_name="Tanaka Premium Market",
                category="PREMIUM RETAIL",
                experience="25 Years",
                ai_score="94%",
                ai_score_color="text-secondary",
                ai_text="Enterprise-grade tenant with stable long-term outlook. Ideal for high-density residential surroundings.",
                revenue="32,800",
                image_placeholder_color="#744210",
            ),
            _applicant_card(
                name="PharmaCare Ltd.",
                store_name="PharmaPlus Express",
                category="PHARMACY",
                experience="8 Years",
                ai_score="76%",
                ai_score_color="text-on-surface-variant",
                ai_text="Service-oriented anchor. May require specialized ventilation and security infrastructure upgrades.",
                revenue="21,500",
                image_placeholder_color="#1a4a5e",
            ),
        ),
    )
