import reflex as rx

from component.auth_state import AuthState


def _profile_menu() -> rx.Component:
    """Circle avatar with dropdown — shown when user is logged in on all pages."""
    dropdown = rx.cond(
        AuthState.nav_dropdown_open,
        rx.box(
            rx.box(
                rx.text(AuthState.user_name, class_name="text-xs font-bold text-on-surface"),
                rx.text(AuthState.user_email, class_name="text-[10px] text-on-surface-variant"),
                class_name="px-4 py-3 border-b border-outline-variant/20",
            ),
            rx.link(
                rx.hstack(
                    rx.el.span("grid_view", class_name="material-symbols-outlined text-base"),
                    rx.text("Dashboard", class_name="text-sm font-medium"),
                    class_name="flex items-center gap-2 px-4 py-2.5 hover:bg-surface-container-low rounded-lg transition-colors",
                ),
                href=rx.cond(
                    AuthState.user_type == "landlord",
                    "/landlorddashboard",
                    "/retailerdashboard",
                ),
                on_click=AuthState.close_nav_dropdown,
                class_name="no-underline text-on-surface w-full block",
            ),
            rx.cond(
                AuthState.user_type == "retailer",
                rx.link(
                    rx.hstack(
                        rx.el.span("manage_accounts", class_name="material-symbols-outlined text-base"),
                        rx.text("Edit Profile", class_name="text-sm font-medium"),
                        class_name="flex items-center gap-2 px-4 py-2.5 hover:bg-surface-container-low rounded-lg transition-colors",
                    ),
                    href="/retailerprofilesetup",
                    on_click=AuthState.close_nav_dropdown,
                    class_name="no-underline text-on-surface w-full block",
                ),
            ),
            rx.box(
                rx.hstack(
                    rx.el.span("logout", class_name="material-symbols-outlined text-base"),
                    rx.text("Logout", class_name="text-sm font-medium"),
                    class_name="flex items-center gap-2 px-4 py-2.5 hover:bg-surface-container-low rounded-lg transition-colors cursor-pointer",
                ),
                on_click=AuthState.logout,
                class_name="text-error w-full",
            ),
            class_name=(
                "absolute right-0 top-[52px] bg-white border border-outline-variant/20 "
                "rounded-2xl shadow-xl py-2 w-48 z-[60]"
            ),
        ),
        rx.fragment(),
    )
    return rx.box(
        rx.box(
            rx.text(AuthState.initials, class_name="text-sm font-bold text-white select-none"),
            on_click=AuthState.toggle_nav_dropdown,
            class_name=(
                "w-9 h-9 rounded-full primary-gradient flex items-center justify-center "
                "cursor-pointer hover:opacity-90 transition-opacity shadow-sm"
            ),
        ),
        dropdown,
        class_name="relative",
    )


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
        rx.cond(
            AuthState.logged_in,
            _profile_menu(),
            rx.hstack(
                rx.link(
                    "Sign In",
                    href="/loginpage",
                    class_name="btn-lime-ghost inline-flex items-center justify-center bg-transparent text-slate-600 dark:text-slate-400 font-sans text-sm px-4 py-2 border-0 cursor-pointer rounded-md transition-colors no-underline",
                ),
                rx.link(
                    "Get Started",
                    href="/createaccountpage",
                    class_name="inline-flex items-center justify-center primary-gradient text-white px-6 py-2.5 rounded-md text-sm font-bold shadow-sm border-0 cursor-pointer transition-all hover:shadow-lime-500/40 hover:ring-2 hover:ring-lime-300 hover:ring-offset-2 hover:ring-offset-white/80 active:scale-95 no-underline",
                ),
                class_name="flex items-center gap-4",
            ),
        ),
        class_name="flex items-center",
    )

    if not show_search:
        return rx.el.nav(
            rx.hstack(
                rx.hstack(logo, links, class_name="flex items-center gap-14"),
                right_actions,
                class_name="w-full flex justify-between items-center px-8 h-20",
            ),
            class_name="fixed top-0 w-full bg-white/80 dark:bg-slate-900/80 backdrop-blur-md z-50 overflow-visible",
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
        class_name="fixed top-0 w-full bg-white/80 dark:bg-slate-900/80 backdrop-blur-md z-50 border-b border-outline-variant/10 overflow-visible",
    )
