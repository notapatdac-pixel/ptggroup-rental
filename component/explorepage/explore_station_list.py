import reflex as rx


_STATIONS = [
    {
        "id": "latphrao71",
        "title": "PTG Station Lat Phrao 71",
        "province": "Bangkok",
        "traffic_level": "high",
        "location": "Bangkok · 2.4 km away",
        "match_badge": "98% Match",
        "traffic_badge": "High Traffic",
        "traffic_badge_class": "bg-on-secondary-container/10 text-on-secondary-container",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAogYrPXv2k3xHfrvbGuzO2u9H021UfnjMDMLdrEuLu2gcWwSPbve71JZORUMDDO8zIqCI0qJ1BsPvzeI2XvXsUIlY9K58cfYcjOMUAWR2_i49F1_jWhThLLarbsBYMgxgc4v0VRqRj9eIjeaYHEFJuJHKGOCdjYH-9rNAX2Nh5sR-96NsIkkQicdlwhVgxMatMoIjNU8gdA3_D_drXtDmqGuAEX8DPF9T8cRvga1fGTTE_a2KHsAQ5jWufQ47tXLdN87UwcjOhK4Q",
        "max_area": ("Max Area", "45 sqm"),
        "available": ("Available", "3 Spaces"),
        "spaces_count": 3,
    },
    {
        "id": "ramaix",
        "title": "PTG Station Rama IX",
        "province": "Bangkok",
        "traffic_level": "medium",
        "location": "Bangkok · 5.1 km away",
        "match_badge": "92% Match",
        "traffic_badge": "Medium Traffic",
        "traffic_badge_class": "bg-tertiary-container/20 text-on-tertiary-container",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuB1XxKMY6FJqo6lJ8jPB-SDQcmEdz1BGe1moAtnxPkXaE82_zwaznYWAnNMvLgUTjz3bkjFvZeSOD-qBHB6XnZmYHrz9yTFk8xIw2xJWi8aN23rFnPM54otIauhJHSX5S_Uhz9OcmG9tRBR2XpLp0qdbts3bwiDPzho2Es8p_WCV7x1v_1HQ0UVhh4AjPQcbJKfIrLX3yFBdzQxm9pSBNvFh_kw6Ge_u_v818HARIcLfsm_P3S4Ku7CyHiA0rGDHIOLCRR1VQ0yOsY",
        "max_area": ("Max Area", "120 sqm"),
        "available": ("Available", "5 Spaces"),
        "spaces_count": 5,
    },
    {
        "id": "bangna",
        "title": "PTG Station Bang Na",
        "province": "Samut Prakan",
        "traffic_level": "high",
        "location": "Samut Prakan · 12.8 km away",
        "match_badge": "85% Match",
        "traffic_badge": "High Traffic",
        "traffic_badge_class": "bg-secondary-container/30 text-on-secondary-container",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCA1MuAJaNhJiEsiDcqskadl4jthvCv3RRv8V3kePz311obEN72Bl5XlnODxBKTtH2HcQQ81ZgsvXMaj3PbOS_l8tndMBg_nuwhVyxl9SukBnO91yFKDU6kxOuu951CaFp80ln54VmlOKK9KZnl7L-imZ5qj675tbgYkJiDd0PImdorHHiJxO67x6IvhB9xtpEI0lpiYXeiuWA2iEn2BEvZytquIlJ2d7iJLov2gJt7eUgkRa65IEKjLmfzYoefpJ7EI-h7lCe-KKo",
        "max_area": ("Max Area", "32 sqm"),
        "available": ("Available", "1 Space"),
        "spaces_count": 1,
    },
]


def _station_card(station: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=station["image"],
                alt=station["title"],
                class_name="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105",
            ),
            rx.el.div(
                rx.el.span(
                    rx.el.span("verified", class_name="material-symbols-outlined text-[12px] fill-icon"),
                    " PTG Verified",
                    class_name=(
                        "bg-white/90 backdrop-blur px-2.5 py-1 rounded-full text-[10px] font-bold text-primary "
                        "flex items-center gap-1 uppercase tracking-wider"
                    ),
                ),
                rx.el.span(
                    station["match_badge"],
                    class_name="bg-primary text-white px-2.5 py-1 rounded-full text-[10px] font-bold flex items-center gap-1 uppercase tracking-wider",
                ),
                class_name="absolute top-3 left-3 flex gap-2",
            ),
            rx.el.button(
                rx.el.span("favorite", class_name="material-symbols-outlined text-sm"),
                type="button",
                class_name="absolute top-3 right-3 w-8 h-8 rounded-full bg-white/20 backdrop-blur text-white flex items-center justify-center hover:bg-white hover:text-error transition-all cursor-pointer",
            ),
            class_name="relative h-40 overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(station["title"], class_name="font-serif text-lg font-bold text-on-surface"),
                    rx.el.p(station["location"], class_name="text-xs text-outline font-medium"),
                ),
                rx.el.span(
                    station["traffic_badge"],
                    class_name=f"{station['traffic_badge_class']} px-2 py-1 rounded-lg text-[10px] font-bold uppercase tracking-tighter",
                ),
                class_name="flex justify-between items-start mb-2",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span("aspect_ratio", class_name="material-symbols-outlined text-primary text-lg"),
                    rx.el.div(
                        rx.el.p(station["max_area"][0], class_name="text-[10px] text-outline uppercase font-bold tracking-widest"),
                        rx.el.p(station["max_area"][1], class_name="text-sm font-bold text-on-surface"),
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.el.span("storefront", class_name="material-symbols-outlined text-primary text-lg"),
                    rx.el.div(
                        rx.el.p(station["available"][0], class_name="text-[10px] text-outline uppercase font-bold tracking-widest"),
                        rx.el.p(station["available"][1], class_name="text-sm font-bold text-on-surface"),
                    ),
                    class_name="flex items-center gap-2",
                ),
                class_name="grid grid-cols-2 gap-4 my-4",
            ),
            rx.el.div(
                rx.el.button(
                    "View Details",
                    type="button",
                    class_name="flex-1 bg-gradient-to-tr from-primary to-primary-container text-white text-xs font-bold py-3 rounded-lg hover:brightness-110 transition-all active:scale-95",
                ),
                class_name="flex gap-2 pt-2",
            ),
            class_name="p-5",
        ),
        id=f"ptg-station-card-{station['id']}",
        custom_attrs={
            "data-station-id": station["id"],
            "data-province": station["province"],
            "data-traffic": station["traffic_level"],
            "data-spaces": str(station["spaces_count"]),
        },
        class_name="group bg-white rounded-xl border border-transparent hover:border-primary/20 hover:shadow-xl transition-all duration-300 overflow-hidden cursor-pointer",
    )


def explore_station_list() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "Browse Locations",
                            class_name="text-2xl font-serif font-bold text-on-surface tracking-tight",
                        ),
                        rx.el.p(
                            "Showing 1,247 locations across Thailand",
                            class_name="text-sm text-outline mt-1",
                        ),
                        class_name="",
                    ),
                    rx.el.button(
                        rx.el.span("tune", class_name="material-symbols-outlined text-on-surface-variant"),
                        type="button",
                        class_name="p-2 border border-outline-variant rounded-xl hover:bg-surface-container-low transition-colors",
                    ),
                    class_name="flex items-center justify-between mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.select(
                            rx.el.option("All Provinces", value="all"),
                            rx.el.option("Bangkok", value="Bangkok"),
                            rx.el.option("Nonthaburi", value="Nonthaburi"),
                            rx.el.option("Pathum Thani", value="Pathum Thani"),
                            rx.el.option("Samut Prakan", value="Samut Prakan"),
                            id="ptg-explore-filter-province",
                            class_name=(
                                "appearance-none bg-surface-container-low border-none rounded-full px-4 py-2 text-xs font-medium pr-8 "
                                "focus:ring-1 focus:ring-primary/30 cursor-pointer"
                            ),
                        ),
                        rx.el.span(
                            "expand_more",
                            class_name=(
                                "material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-[16px] "
                                "pointer-events-none text-outline cursor-pointer"
                            ),
                        ),
                        class_name="relative",
                    ),
                    rx.el.div(
                        rx.el.select(
                            rx.el.option("All Traffic", value="all"),
                            rx.el.option("High", value="high"),
                            rx.el.option("Medium", value="medium"),
                            rx.el.option("Low", value="low"),
                            id="ptg-explore-filter-traffic",
                            class_name=(
                                "appearance-none bg-surface-container-low border-none rounded-full px-4 py-2 text-xs font-medium pr-8 "
                                "focus:ring-1 focus:ring-primary/30 cursor-pointer"
                            ),
                        ),
                        rx.el.span(
                            "expand_more",
                            class_name=(
                                "material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-[16px] "
                                "pointer-events-none text-outline cursor-pointer"
                            ),
                        ),
                        class_name="relative",
                    ),
                    rx.el.div(
                        rx.el.select(
                            rx.el.option("All Spaces", value="all"),
                            rx.el.option("2+ Spaces", value="2"),
                            rx.el.option("5+ Spaces", value="5"),
                            rx.el.option("10+ Spaces", value="10"),
                            id="ptg-explore-filter-spaces",
                            class_name=(
                                "appearance-none bg-surface-container-low border-none rounded-full px-4 py-2 text-xs font-medium pr-8 "
                                "focus:ring-1 focus:ring-primary/30 cursor-pointer"
                            ),
                        ),
                        rx.el.span(
                            "expand_more",
                            class_name=(
                                "material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-[16px] "
                                "pointer-events-none text-outline cursor-pointer"
                            ),
                        ),
                        class_name="relative",
                    ),
                    class_name="flex flex-wrap gap-2",
                ),
                class_name="p-6 border-b border-surface-container",
            ),
            rx.el.div(
                *[_station_card(s) for s in _STATIONS],
                class_name="flex-1 overflow-y-auto p-6 space-y-6",
            ),
            class_name="w-[480px] h-full bg-white flex flex-col shadow-2xl z-10",
        ),
    )

