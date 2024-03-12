import reflex as rx
import datetime
import link_bio.styles.styles as styles
import link_bio.styles.constants as constants

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="Logo_bg_remove.png",
            width = styles.Size.HUGE.value,
            height="auto",
            alt = "Logotipo de Pabloelt",
            align="center",
            ),
        rx.link(
            f"©2014-{datetime.date.today().year} MoureDev by Brais Moure v3",
            font_size = styles.Size.MEDIUM.value,
            href = constants.LINKEDIN_URL,
            is_external = True,
            align = "center",
            color = styles.TextColor.FOOTER.value,
            ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD",
            align = "center",
            font_size = styles.Size.MEDIUM.value,
            color = styles.TextColor.FOOTER.value,
            ),
        align_items = "center",
        margin_bottom = styles.Size.BIG.value,
        padding_bottom = styles.Size.BIG.value,
        padding_x = styles.Size.BIG.value,
    )