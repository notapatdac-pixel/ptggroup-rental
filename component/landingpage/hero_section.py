import reflex as rx

from component.landingpage.stats_bar import hero_stats_strip

# AI-generated hero art (PTG-inspired). Files: assets/image/hero-ptg-style-*.png → URLs /image/...
HERO_CAROUSEL_IMAGES: list[tuple[str, str]] = [
    ("/image/hero-ptg-style-1.png", "Modern green and white petrol retail station at sunset"),
    ("/image/hero-ptg-style-2.png", "Night scene with green-lit canopy and convenience store"),
    ("/image/hero-ptg-style-3.png", "Aerial view of fuel and retail hub, lime green accents"),
    ("/image/hero-ptg-style-4.png", "Dusk forecourt with emerald canopy and glass retail"),
]


def hero_section() -> rx.Component:
    slides = []
    for i, (url, alt) in enumerate(HERO_CAROUSEL_IMAGES):
        slides.append(
            rx.el.img(
                src=url,
                alt=alt,
                loading="eager" if i == 0 else "lazy",
                decoding="async",
                class_name=f"hero-carousel-bg-slide hero-carousel-bg-slide--{i}",
            )
        )

    return rx.el.section(
        rx.box(
            rx.box(*slides, class_name="hero-carousel-bg"),
            rx.box(
                class_name=(
                    "absolute inset-0 z-[1] bg-gradient-to-r "
                    "from-black/15 via-black/10 to-black/25 pointer-events-none"
                )
            ),
            rx.box(
                rx.grid(
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.box(class_name="w-2 h-2 rounded-full bg-secondary"),
                                rx.text(
                                    "Thailand's Premier Retail Marketplace",
                                    class_name="text-xs font-bold tracking-widest uppercase text-on-secondary-container",
                                ),
                                class_name="inline-flex items-center gap-2 px-3 py-1 bg-on-secondary-container/10 rounded-full mb-8",
                            ),
                            rx.heading(
                                rx.fragment(
                                    "Find Your Next Store at ",
                                    rx.el.span("PTG Gas Stations", class_name="text-primary italic"),
                                ),
                                as_="h1",
                                class_name="text-6xl lg:text-7xl text-on-surface leading-[1.1] mb-8 drop-shadow-sm",
                            ),
                            rx.text(
                                "Discover high-traffic retail locations, analyze success potential with AI, and grow your business where customers already are.",
                                class_name="text-xl text-on-surface leading-relaxed mb-10 max-w-xl",
                            ),
                            rx.hstack(
                                rx.link(
                                    rx.hstack(
                                        rx.text("Explore Locations"),
                                        rx.el.span(
                                            "arrow_forward",
                                            class_name="material-symbols-outlined text-lime-200 group-hover:text-lime-50 group-hover:translate-x-4 transition-all",
                                        ),
                                        class_name="flex items-center gap-2",
                                    ),
                                    href="/explorepage",
                                    class_name=(
                                        "group inline-flex items-center justify-center primary-gradient text-white "
                                        "px-26 py-4 rounded-md text-base font-bold border-0 cursor-pointer "
                                        "transition-all hover:shadow-lg hover:shadow-lime-600/40 no-underline"
                                    ),
                                ),
                                rx.link(
                                    "Get Started",
                                    href="/createaccountpage",
                                    class_name="btn-lime-outline inline-flex items-center justify-center bg-white/90 px-8 py-4 rounded-md text-base font-bold border border-outline-variant transition-colors text-on-surface cursor-pointer backdrop-blur-sm no-underline",
                                ),
                                class_name="flex flex-wrap gap-4",
                            ),
                            class_name="hero-content-glass p-8 lg:p-10 max-w-4xl",
                        ),
                        class_name="z-10",
                    ),
                ),
                class_name="relative z-10 max-w-7xl mx-auto pt-44 pb-44 md:pb-56 px-8",
            ),
            hero_stats_strip(),
            class_name="relative overflow-hidden min-h-[90vh] lg:min-h-[40rem]",
        ),
    )
