import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color as Color

def link_button(title: str, body: str, url: str, icon: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src = icon,
                    width = styles.Size.BIG.value,
                    height = "auto",
                    alt = title,
                    margin = styles.Size.MEDIUM.value,
                    padding_y = styles.Size.SMALL.value,
                    ),
                rx.vstack(
                    rx.text(title, style=styles.BUTTOM_TITLE_STYLE),
                    rx.text(body, style=styles.BUTTOM_BODY_STYLE),
                    spacing = "0",
                    align_items="start",
                    margin = styles.Size.SMALL.value,
                    ),
                    width = "100%",
                ),
            ),
        href = url,
        is_external = True,
        width = "100%",
    )

