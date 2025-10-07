from typing import Optional, Callable
from ignis import widgets


class CustomIconBtn(widgets.Button):
    def update_icon(self, icon: str):
        self.btn_label.set_label(icon)

    def __init__(self, icon: str = "", on_click: Optional[Callable] = None):
        self.btn_label = widgets.Label(style="font-family: 'Phosphor';", label=icon)

        super().__init__(
            css_classes=["bar_icon-btn"],
            child=self.btn_label,
            on_click=on_click,
        )
