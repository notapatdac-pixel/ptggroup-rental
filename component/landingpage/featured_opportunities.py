import reflex as rx

from component.explorepage.stations_catalog import STATIONS


def _opportunity_card(station: dict) -> rx.Component:
    """Same image, title, location line, and badges as explore list; links to station detail."""
    d = station["detail"]
    spaces_lower = station["available"][1].lower()
    try:
        n = int(str(d["daily_customers"]).replace(",", ""))
        footfall = f"{n:,}+"
    except ValueError:
        footfall = f"{d['daily_customers']}+"

    inner = rx.box(
        rx.box(
            rx.image(src=station["image"], alt=station["title"], class_name="w-full h-full object-cover"),
            rx.hstack(
                rx.text(
                    "PTG Verified",
                    class_name="px-2 py-1 bg-primary text-white text-[10px] font-bold uppercase rounded tracking-wider",
                ),
                rx.text(
                    station["match_badge"],
                    class_name="px-2 py-1 bg-on-secondary-container text-white text-[10px] font-bold uppercase rounded tracking-wider",
                ),
                class_name="absolute top-4 left-4 flex gap-2",
            ),
            class_name="relative aspect-video",
        ),
        rx.box(
            rx.hstack(
                rx.heading(station["title"], as_="h4", class_name="font-headline text-xl text-on-surface"),
                rx.text(spaces_lower, class_name="text-primary font-headline text-lg"),
                class_name="flex justify-between items-start mb-2",
            ),
            rx.hstack(
                rx.el.span("location_on", class_name="material-symbols-outlined text-sm"),
                rx.text(station["location"]),
                class_name="text-on-surface-variant text-sm flex items-center gap-1 mb-4",
            ),
            rx.hstack(
                rx.box(
                    rx.text("Max Area", class_name="text-[10px] uppercase text-on-surface-variant font-bold"),
                    rx.text(station["max_area"][1], class_name="text-sm font-bold text-on-surface"),
                    class_name="flex flex-col",
                ),
                rx.box(
                    rx.text("Daily Footfall", class_name="text-[10px] uppercase text-on-surface-variant font-bold"),
                    rx.text(footfall, class_name="text-sm font-bold text-on-surface"),
                    class_name="flex flex-col",
                ),
                class_name="flex items-center gap-4 pt-4 border-t border-outline-variant/10",
            ),
            class_name="p-6",
        ),
        class_name=(
            "bg-surface-container-lowest rounded-xl overflow-hidden shadow-sm hover:shadow-xl "
            "hover:shadow-lime-500/20 transition-all hover:-translate-y-1 border border-outline-variant/10 "
            "hover:border-lime-400/50"
        ),
    )
    return rx.link(
        inner,
        href=f"/stationdetailpage/{station['id']}",
        class_name="no-underline block text-inherit",
    )


def featured_opportunities() -> rx.Component:
    featured = STATIONS[:3]
    return rx.el.section(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.heading("Featured Opportunities", as_="h2", class_name="text-5xl text-on-surface mb-4"),
                    rx.text(
                        "High-potential locations available for lease this week.",
                        class_name="text-on-surface-variant text-lg",
                    ),
                ),
                rx.link(
                    rx.hstack(
                        rx.text("View All Locations"),
                        rx.el.span("chevron_right", class_name="material-symbols-outlined"),
                        class_name="flex items-center gap-2",
                    ),
                    href="/explorepage",
                    class_name=(
                        "btn-lime-text-link inline-flex items-center justify-center bg-transparent text-primary "
                        "font-bold hover:gap-3 transition-all border-0 cursor-pointer rounded-md no-underline"
                    ),
                ),
                class_name="flex justify-between items-end mb-16 flex-wrap gap-6",
            ),
            rx.grid(
                *[_opportunity_card(s) for s in featured],
                class_name="grid md:grid-cols-3 gap-8",
            ),
            class_name="max-w-7xl mx-auto relative z-10",
        ),
        class_name="featured-opportunities-section relative overflow-hidden py-40 px-8",
    )
