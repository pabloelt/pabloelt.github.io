import reflex as rx
import link_bio.styles.styles as styles

def dialog_icon(text: str, icon: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.icon(
                tag = icon,
                size = 25,
                color = styles.Color.SECONDARY.value,
                ),
            ),
        rx.flex(
            rx.dialog.content(
                rx.dialog.description(
                    rx.text(
                        text,
                        size = "3",
                        ),
                    ),
                rx.dialog.close(
                    rx.button(
                        rx.text(
                            "Close",
                            size = "2",
                            align = "center",
                            ),
                        width = "13%",
                        align = "start",
                        margin_y = styles.Size.SMALL.value,
                        ),
                    ),
                ),
        ),
    )