import reflex as rx
import link_bio.styles.styles as styles

def info_text(title: str, body: str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(
            title,
            font_weight = "bold",
            color = styles.Color.SECONDARY.value,
            ),
        body,
        font_size = styles.Size.MEDIUM.value,
        color = styles.TextColor.BODY.value,
    )