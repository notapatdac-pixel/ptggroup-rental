import reflex as rx


def _footer_column(title: str, links: list[str]) -> rx.Component:
    return rx.box(
        rx.heading(title, as_="h4", class_name="font-headline text-lg mb-8"),
        rx.el.ul(
            *[
                rx.el.li(
                    rx.link(
                        item,
                        href="#",
                        class_name="text-slate-400 hover:text-lime-400 text-sm transition-colors underline-offset-4 hover:underline",
                    )
                )
                for item in links
            ],
            class_name="space-y-4",
        ),
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.box(
            rx.grid(
                rx.box(
                    rx.hstack(
                        rx.text("PTG", class_name="text-4xl font-serif font-bold text-lime-500"),
                        rx.text("Retail Platform", class_name="font-headline text-lg tracking-tight"),
                        class_name="flex items-center gap-2 mb-8",
                    ),
                    rx.text(
                        "Thailand's leading intelligent marketplace connecting businesses with high-potential energy station retail hubs.",
                        class_name="text-slate-400 text-sm leading-relaxed max-w-xs",
                    ),
                ),
                _footer_column("Platform", ["Explore", "Pricing", "AI Advisor", "Market Analytics"]),
                _footer_column("Company", ["About Us", "Careers", "Newsroom", "Investor Relations"]),
                _footer_column("Legal", ["Terms", "Privacy", "Cookie Policy", "Whistleblowing"]),
                class_name="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-28",
            ),
            rx.hstack(
                rx.text("© 2024 PTG Energy Public Company Limited. All rights reserved.", class_name="text-slate-500 text-xs"),
                rx.hstack(
                    rx.link(rx.el.span("language", class_name="material-symbols-outlined text-xl"), href="#", class_name="text-slate-500 hover:text-lime-400 transition-colors"),
                    rx.link(rx.el.span("contact_support", class_name="material-symbols-outlined text-xl"), href="#", class_name="text-slate-500 hover:text-lime-400 transition-colors"),
                    class_name="flex gap-6",
                ),
                class_name="max-w-7xl mx-auto pt-12 mt-12 border-t border-slate-800 flex flex-col md:flex-row justify-between items-center gap-8",
            ),
        ),
        class_name="bg-slate-950 text-white py-12 px-6",
    )
