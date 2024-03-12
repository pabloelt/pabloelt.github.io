import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight


# Constants:
MAX_WIDTH = "600px"


# Sizes:
class Size(Enum):
    ZERO = "0px"
    SMALL = "0.5em" # em toma como referencia el tamaño de fuente de la aplicación. Así si aumenta el tamaño de fuente, aumenta la relación de espacio
    MEDIUM = "0.8em"
    MEDIUM_2 = "0.9em"
    DEFAULT = "1em"
    DEFAULT_2 = "1.2em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    HUGE = "6em"


# Styles:
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "size": "4",
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        #"display": "block",
        "white_space": "normal",
        "text_align": "start",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
        "background_color": Color.CONTENT.value,
        "color": TextColor.HEADER.value,
        "_hover": { # Para modificar el aspecto del botón cuando el ratón pasa por encima
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.link: {
        "text_decoration": "None",
        "_hover": {},
    }
}


NAVBAR_TITLE_STYLE = dict(
    font_family = Font.LOGO.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.LARGE.value,
)

TITLE_STYLE = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
)

BUTTOM_TITLE_STYLE = dict(
    font_size = Size.DEFAULT_2.value,
    font_weight = FontWeight.MEDIUM.value,
    color = TextColor.HEADER.value,
    font_family = Font.TITLE.value,
)
BUTTOM_BODY_STYLE = dict(
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value,
    font_family = Font.DEFAULT.value,
    font_weight = FontWeight.LIGHT.value,
)


# FONTS

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]
