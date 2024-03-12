import reflex as rx
import link_bio.styles.styles as styles

def link_icon(url: str, icon: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = icon,
            width = styles.Size.DEFAULT_2.value,
            height = "auto",
            alt = alt,
        ),
        href = url,
        is_external= True,
        #color = styles.Color.SECONDARY.value,
    )