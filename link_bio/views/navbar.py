import reflex as rx
import link_bio.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.chakra.span("pabloelt", color = styles.Color.PRIMARY.value),
            rx.chakra.span("dev", color = styles.Color.SECONDARY.value),
            style = styles.NAVBAR_TITLE_STYLE,
        ),
    position = "sticky",
    bg = styles.Color.CONTENT.value,
    padding_x = styles.Size.BIG.value,
    padding_y = styles.Size.DEFAULT.value,
    z_index = "999", # Para asegurarnos que siempre va a estar en la parte superior
    top = 0,
    )