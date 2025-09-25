from typing import Callable, List
from ignis.widgets import Widget


class CustomIconBtn(Widget.Button):
    __gtype_name__ = "IconButton"

    def __init__(self, icon: str, onclick: Callable, css_classes: List[str]):
        css_classes.append("bar__btn-icon")
        print(icon)

        super().__init__(
                css_classes = css_classes,
                on_click = onclick,
                child = Widget.Label(
                    label = icon
                    )
                )
