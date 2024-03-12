# http://localhost:3000

import reflex as rx
from link_bio.views.navbar import navbar
from link_bio.views.header import header
from link_bio.views.links import links
from link_bio.views.footer import footer
import link_bio.styles.styles as styles
from link_bio.views.sponsors import sponsors

#class State(rx.State):
#    pass



def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width= styles.MAX_WIDTH,
                width= "100%",
                margin_y= styles.Size.BIG.value,
                padding = styles.Size.BIG.value,
            ),
        ),
        rx.center(
            footer(),
            ),
    )
    



app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets = styles.STYLESHEETS
)
app.add_page(
    index,
    title = "Mouredev | Te enseño programación y desarrollo de software",
    description = "Hola, mi nombre es Pablo Esteban. Soy ingeniero de software, desarrollador freelance full-stack y divulgador.",
    image = "avatar.jpg"
    )
#app.compile()