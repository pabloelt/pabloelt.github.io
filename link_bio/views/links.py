import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.styles.constants as constants

def links() -> rx.Component:
    return rx.vstack(
        title("¿A qué me dedico?"),
        link_button(
            "Papers publicados",
            "Mis artículos científicos en el campo de la propulsión acuática",
            constants.RESEARCHGATE_URL,
            "icons/atom.svg",
                    ),
        link_button(
            "Twitch",
            "Transmisiones sobre programación de lunes a viernes",
            constants.TWITCH_URL,
            "icons/twitch.svg",
            ),
        link_button(
            "Discord",
            "El chat y los grupos de estudio de la comunidad",
            constants.DISCORD_URL,
            "icons/discord.svg",
                    ),
        link_button(
            "Youtube",
            "Tutoriales sobre software de desarrollo semanales",
            constants.YOUTUBE_URL,
            "icons/youtube.svg",
            ),
        link_button(
            "Youtube (canal secundario)",
            "Emisiones en directo destacadas",
            constants.YOUTUBE_SECONDARY_URL,
            "icons/youtube.svg",
            ),

        title("Recursos y más"),
        link_button(
            "Git y GitHub desde cero",
            "Aquí puedes comprar mi libro en formato físico y eBook",
            constants.BOOK_URL,
            "icons/book.svg",
            ),
        link_button(
            "Libros recomendados",
            "Mi listado de libros sobre programación, ciencia y tecnología",
            constants.BOOKS_URL,
            "icons/bookmark.svg",
            ),
        link_button(
            "Mi setup",
            "Listado con todos los elementos que uso en mi trabajo",
            "https://www.youtube.com/",
            "icons/gear.svg",
            ),
        link_button(
            "Mouredev",
            "Mi sitio web",
            "https://www.youtube.com/",
            "icons/github.svg",
            ),
        link_button(
            "Invítame a un café",
            "¿Quieres ayudarme a que siga creando contenido?",
            "https://www.youtube.com/",
            "icons/coffee.svg",
            ),

        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            constants.MYPUBLICINBOX_URL,
            "icons/inbox.svg",
            ),
        link_button(
            "Email",
            constants.EMAIL_URL,
            f"mailto:{constants.EMAIL_URL}",
            "icons/mail.svg",
            ),

        width = "100%",
    )