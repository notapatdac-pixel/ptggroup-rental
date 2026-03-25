import reflex as rx


def nav_bar(show_search: bool = False) -> rx.Component:
    logo = rx.link(
        rx.hstack(
            rx.text("PTG", class_name="text-4xl font-serif font-bold text-lime-500"),
            rx.text("Retail Platform", class_name="font-headline text-lg tracking-tight text-on-surface"),
            class_name="flex items-center gap-2",
        ),
        href="/",
        class_name="no-underline",
    )

    links = rx.hstack(
        rx.link("Explore Locations", href="/explorepage", class_name="nav-link-lime font-sans"),
        rx.link("Pricing", href="/pricingpage", class_name="nav-link-lime font-sans"),
        class_name="hidden md:flex gap-10 items-center",
    )

    right_actions = rx.hstack(
        rx.el.button(
            "Sign In",
            type="button",
            class_name="btn-lime-ghost inline-flex items-center justify-center bg-transparent text-slate-600 dark:text-slate-400 font-sans text-sm px-4 py-2 border-0 cursor-pointer rounded-md transition-colors",
        ),
        rx.el.button(
            "Get Started",
            type="button",
            class_name="inline-flex items-center justify-center primary-gradient text-white px-6 py-2.5 rounded-md text-sm font-bold shadow-sm border-0 cursor-pointer transition-all hover:shadow-lime-500/40 hover:ring-2 hover:ring-lime-300 hover:ring-offset-2 hover:ring-offset-white/80 active:scale-95",
        ),
        class_name="flex items-center gap-4",
    )

    if not show_search:
        return rx.el.nav(
            rx.hstack(
                rx.hstack(logo, links, class_name="flex items-center gap-14"),
                right_actions,
                class_name="w-full flex justify-between items-center px-8 h-20",
            ),
            class_name="fixed top-0 w-full bg-white/80 dark:bg-slate-900/80 backdrop-blur-md z-50",
        )

    search = rx.el.div(
        rx.el.span(
            "search",
            class_name=(
                "material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 "
                "text-outline group-focus-within:text-primary"
            ),
        ),
        rx.el.input(
            id="ptg-explore-search-input",
            placeholder="Search by province, station name, or district...",
            type="text",
            class_name=(
                "w-full bg-surface-container-low border-none rounded-full py-2.5 pl-12 pr-4 text-sm "
                "focus:ring-2 focus:ring-primary/20 transition-all outline-none"
            ),
        ),
        class_name=(
            "pointer-events-auto relative group w-full max-w-2xl mx-auto transition-all "
            "duration-300 group-focus-within:max-w-5xl"
        ),
    )

    # Match landing’s button positioning exactly (same wrapper layout).
    # Search is an overlay in the center so it does not affect justify-between geometry.
    return rx.el.nav(
        rx.el.div(
            rx.hstack(
                rx.hstack(logo, links, class_name="flex items-center gap-14"),
                right_actions,
                class_name="w-full flex justify-between items-center px-8 h-20 relative z-10",
            ),
            rx.el.div(
                search,
                class_name=(
                    "pointer-events-none absolute inset-0 z-20 flex items-center justify-center"
                ),
            ),
            class_name="relative w-full",
        ),
        class_name="fixed top-0 w-full bg-white/80 dark:bg-slate-900/80 backdrop-blur-md z-50 border-b border-outline-variant/10",
    )
