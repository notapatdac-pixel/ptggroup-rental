import reflex as rx

config = rx.Config(
    app_name="ptggroup_rental",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)