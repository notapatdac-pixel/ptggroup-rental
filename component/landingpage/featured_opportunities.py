import reflex as rx


def _opportunity_card(
    title: str,
    spaces: str,
    location: str,
    max_area: str,
    footfall: str,
    image_src: str,
    badge: str,
) -> rx.Component:
    return rx.box(
        rx.box(
            rx.image(src=image_src, class_name="w-full h-full object-cover"),
            rx.hstack(
                rx.text("PTG Verified", class_name="px-2 py-1 bg-primary text-white text-[10px] font-bold uppercase rounded tracking-wider"),
                rx.text(badge, class_name="px-2 py-1 bg-on-secondary-container text-white text-[10px] font-bold uppercase rounded tracking-wider"),
                class_name="absolute top-4 left-4 flex gap-2",
            ),
            class_name="relative aspect-video",
        ),
        rx.box(
            rx.hstack(
                rx.heading(title, as_="h4", class_name="font-headline text-xl text-on-surface"),
                rx.text(spaces, class_name="text-primary font-headline text-lg"),
                class_name="flex justify-between items-start mb-2",
            ),
            rx.hstack(
                rx.el.span("location_on", class_name="material-symbols-outlined text-sm"),
                rx.text(location),
                class_name="text-on-surface-variant text-sm flex items-center gap-1 mb-4",
            ),
            rx.hstack(
                rx.box(
                    rx.text("Max Area", class_name="text-[10px] uppercase text-on-surface-variant font-bold"),
                    rx.text(max_area, class_name="text-sm font-bold text-on-surface"),
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
        class_name="bg-surface-container-lowest rounded-xl overflow-hidden shadow-sm hover:shadow-xl hover:shadow-lime-500/20 transition-all hover:-translate-y-1 border border-outline-variant/10 hover:border-lime-400/50",
    )


def featured_opportunities() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.heading("Featured Opportunities", as_="h2", class_name="text-5xl text-on-surface mb-4"),
                    rx.text("High-potential locations available for lease this week.", class_name="text-on-surface-variant text-lg"),
                ),
                rx.el.button(
                    rx.hstack(
                        rx.text("View All Locations"),
                        rx.el.span("chevron_right", class_name="material-symbols-outlined"),
                        class_name="flex items-center gap-2",
                    ),
                    type="button",
                    class_name="btn-lime-text-link inline-flex items-center justify-center bg-transparent text-primary font-bold hover:gap-3 transition-all border-0 cursor-pointer rounded-md",
                ),
                class_name="flex justify-between items-end mb-16",
            ),
            rx.grid(
                _opportunity_card(
                    "PTG Station Lat Phrao 71",
                    "3 spaces",
                    "Bangkok, TH",
                    "45 sqm",
                    "2,400+",
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuDG9t56Z7xEVfMxBVCJb_mqaW-OCFg8uVeMRk1-fH0Dwo_qQ0UCFgTvRvjuKQNIiP35rqpjpe7v2SSzgCfBkf_y7oL8jaThS27lIEec0j1UNLsnTqv6CQsdSBg-CueDDn5bQW8Bw2CMjeiOXHyTFjRXsxnihc0o4o5c5DibTGTKw99dx1u0hpIOaZKSGc01ZXZlFdCrzMuGLHWKL0NsXAwGjQOCBZIlkDzAH4KhPOvd_vXjJXMBhHZKCGlYjz6Ay7c1fxKtKxEvTtc",
                    "High Traffic",
                ),
                _opportunity_card(
                    "PTG Station Sukhumvit 62",
                    "2 spaces",
                    "Bangkok, TH",
                    "120 sqm",
                    "5,800+",
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuCGDBmOXvUphYydWPfXlaCPouf1PgTV86XlkkCkc2qR6wCBI68DvYA-CoXPMQ6opMvVRZiF4ff-nIhvRVoeNWGsHVp3dCIew_BEr9_GSZaoD7LH3BNUw9XM3_f6Thww5-yoxKKiMb3y0b1BoSzDRN-xG0oAnrHOIN3CvKIIn9RleNSCUw8LoEe3A7J0z2D1xCJdNvkWwZZWZ6RTBMYD6SPQsO9-ISO9cf6DguObVlgQsSf95SP7awF1NemyRD51cKJPakNSLNdYdFY",
                    "High Traffic",
                ),
                _opportunity_card(
                    "PTG Station Nimman Rd",
                    "2 spaces",
                    "Chiang Mai, TH",
                    "32 sqm",
                    "1,900+",
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuDVhZQ92D84OU7JIXBK9I_7bSvaWz5fjpcntFGYu0hyvmwSz6L3kaXV8TaLIDcIXOO7-FRocDB1DAz6ANjB5CEBpPzYPni8tNz0v8tRDixwqWlzgpVd3Gshywn7TfLPU_5c1gFMOpLXiNrerECPWL_74jtnGaiubuVdhB3sbXeE7PETLsiay440SLO0JDbYD1vRO68bHOAKlXux4hcIeVO8U7S7bJrXuK4xcqdQCMYPRHJPpVlN4Dz483iU8yeOzupmiQFn-yDyQOg",
                    "Prime Location",
                ),
                class_name="grid md:grid-cols-3 gap-8 cursor-pointer",
            ),
            class_name="max-w-7xl mx-auto relative z-10",
        ),
        class_name="featured-opportunities-section relative overflow-hidden py-40 px-8",
    )
