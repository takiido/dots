from ignis import widgets
from .customIconBtn import CustomIconBtn
from .volume import Volume
from .backlight import Backlight


class Dash(widgets.Box):
    def __init__(self, control_centre):
        self.network_btn = CustomIconBtn(
            icon="", on_click=lambda _: control_centre.toggle()
        )

        super().__init__(
            child=[
                self.network_btn,
                Backlight(),
                Volume(),
            ],
        )
