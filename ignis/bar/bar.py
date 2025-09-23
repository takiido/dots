from ignis.widgets import Widget


def left() -> Widget.Box:
    return Widget.Box(
            css_classes = ["bar__left"],
            spacing = 10,
            child = [
                Widget.Label(
                    label = "left"
                    ),
                Widget.Label(
                    label = "widgets"
                    )
                ]
            )

def center() -> Widget.Box:
    return Widget.Box(
            css_classes = ["bar__center"],
            spacing = 10,
            child = [
                Widget.Label(
                    label = "center"
                    ),
                Widget.Label(
                    label = "widgets"
                    )
                ]
            )

def right() -> Widget.Box:
    return Widget.Box(
            css_classes = ["bar__right"],
            spacing = 10,
            child = [
                Widget.Label(
                    label = "right"
                    ),
                Widget.Label(
                    label = "widgets"
                    )
                ]
            )

class Bar(Widget.Window):
    __gtype_name__ = "TopBar"

    def __init__(self, monitor: int):
        print(monitor)

        super().__init__(
                exclusivity = "exclusive",
                namespace = f"TopBar-{monitor}",
                monitor = monitor,
                anchor = ["left", "top", "right"],
                child = Widget.CenterBox(
                    css_classes = ["bar"],
                    start_widget = left(),
                    center_widget = center(),
                    end_widget = right()
                    )
                )
