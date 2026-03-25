"""Shared button / CTA classes aligned with landing `nav_bar` actions."""

BTN_LANDING_GHOST = (
    "btn-lime-ghost inline-flex items-center justify-center bg-transparent text-slate-600 "
    "dark:text-slate-400 font-sans text-sm px-4 py-2.5 border-0 cursor-pointer rounded-md transition-colors"
)

BTN_LANDING_PRIMARY = (
    "inline-flex items-center justify-center primary-gradient text-white px-6 py-2.5 rounded-md text-sm font-bold "
    "shadow-sm border-0 cursor-pointer transition-all hover:shadow-lime-500/40 hover:ring-2 hover:ring-lime-300 "
    "hover:ring-offset-2 hover:ring-offset-white/80 active:scale-95"
)

# Primary CTA on dark / image backgrounds (Pro card)
BTN_LANDING_PRIMARY_ON_DARK = (
    "inline-flex items-center justify-center primary-gradient text-white w-full py-3 rounded-md text-sm font-bold "
    "shadow-sm border-0 cursor-pointer transition-all hover:shadow-lime-500/40 hover:ring-2 hover:ring-lime-300 "
    "hover:ring-offset-2 hover:ring-offset-black/90 active:scale-95"
)

# Full-width Apply on space cards (same motion as landing Get Started)
BTN_LANDING_PRIMARY_BLOCK = (
    "inline-flex items-center justify-center primary-gradient text-white w-full py-2 rounded-md text-sm font-bold "
    "shadow-sm border-0 cursor-pointer transition-all hover:shadow-lime-500/40 hover:ring-2 hover:ring-lime-300 "
    "hover:ring-offset-2 hover:ring-offset-white/80 active:scale-95"
)
