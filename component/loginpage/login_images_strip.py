import reflex as rx


def login_images_strip() -> rx.Component:
    """Three-image strip shown below the sign-in card."""
    images = [
        ("/image/login-retail-store.jpg", "Retail store interior"),
        ("/image/login-analyst.jpg", "Business analyst with data"),
        ("/image/login-buildings.jpg", "Modern city buildings"),
    ]
    return rx.el.div(
        *[
            rx.image(
                src=src,
                alt=alt,
                class_name="w-full h-40 object-cover rounded-xl",
            )
            for src, alt in images
        ],
        class_name="grid grid-cols-3 gap-4 max-w-xl mx-auto w-full px-4",
    )
