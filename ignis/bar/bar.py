from ignis.widgets import Widget

from .modules.clock import clock
from .modules.volume import Volume

darkMode = True

def test(args):
    print("test")

def left() -> Widget.Box:
    return Widget.Box(
            css_classes = ["bar__left"],
            spacing = 10,
            child = [
                Volume(),
                ]
            )

def center() -> Widget.Box:
    return Widget.Box(
            css_classes = ["bar__center"],
            spacing = 10,
            child = [
                Widget.Label(
                    css_classes = ["bar__logo"],
                    label = "𝖓𝖎𝖍𝖎𝖑"
                    ),
                ]
            )

def right() -> Widget.Box:
    return Widget.Box(
            css_classes = ["bar__right"],
            spacing = 10,
            child = [
                clock,
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
                    css_classes = ["bar", "bar--dark" if darkMode else ""],
                    start_widget = left(),
                    center_widget = center(),
                    end_widget = right()
                    )
                )
