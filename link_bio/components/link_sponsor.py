import reflex as rx
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size

def link_sponsor(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = image,
            height = Size.VERY_BIG.value,
            width = "auto",
            alt = alt,
        ),
        href = url,
        is_external = True,
    )