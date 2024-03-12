import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor
import link_bio.styles.constants as constants
from link_bio.styles.styles import Size as Size

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.flex(
            link_sponsor(
                "elgato.png",
                constants.ELGATO_URL,
                "Logotipo de Elgato",
            ),
            link_sponsor(
                "mvp.png",
                constants.MVP_URL,
                "Logotipo de Microsoft MVP",
            ),
            spacing = "9",
        ),
        width = "100%",
        align_items = "center",
    )