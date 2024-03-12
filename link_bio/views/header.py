import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.components.dialog_icon import dialog_icon
import  link_bio.styles.constants as constants

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name = "Pablo Esteban",
                size = "7",
                src = "avatar.jpg",
                alt = "Avatar de @pabloelt",
                color = TextColor.BODY.value,
                bg = Color.CONTENT.value,
                radius = "medium",
                #padding = "2px",
                #border = "4px",
                #border_color = Color.PRIMARY.value,
                ),
            #rx.image(src="man_hat.jpg", width="150px", height="auto", align="center"),
            rx.vstack(
                rx.heading(
                    "PABLO ESTEBAN LÓPEZ-TELLO",
                    size = "4",
                    ),
                rx.text(
                    "@pabloelt",
                    size="4",
                    color = TextColor.HEADER.value,
                    ),
                rx.hstack(
                    #link_icon(constants.GITHUB_URL,"icons/github.svg", "GitHub"),
                    #link_icon(constants.TWITTER_X_URL,"icons/twitter.svg", "Twitter"),
                    link_icon(constants.INSTAGRAM_URL,"icons/instagram.svg", "Instagram"),
                    #link_icon(constants.TIKTOK_URL,"icons/tiktok.svg", "TikTok"),
                    #link_icon(constants.SPOTIFY_URL,"icons/spotify.svg", "Spotify"),
                    link_icon(constants.LINKEDIN_URL,"icons/linkedin.svg", "LinkedIn"),
                    #dialog_icon("666666666","phone"),
                    spacing = "5",
                    ),
                ),
                spacing = "5",
            ),
        rx.flex(
            info_text("13+ ", "años de experiencia"),
            rx.spacer(),
            info_text("100+ ", "aplicaciones creadas"),
            rx.spacer(),
            info_text("1M+ ", "seguidores"),
            width = "100%"
            ),
        rx.text(f"""
                Soy ingeniero industrial graduado en la Universidad de Málaga, 
                además recientemente he acabado mis estudios de doctorado en 
                la modalidad de ingeniería mecatrónica, donde trabajé durante 
                4 años con nuevos medios de propulsión acuática basados en la 
                tecnología de perfiles batientes.
                """,
                text_align = "justify",
                color = TextColor.BODY.value,
                font_size = Size.MEDIUM_2.value,
                ),
        align_items = "start",
        spacing = "5",
    )