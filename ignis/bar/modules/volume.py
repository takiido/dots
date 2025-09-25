from ignis.widgets import Widget

from .custom.custom_btn_icon import CustomIconBtn
from .custom.custom_slider import CustomSlider


class Volume(Widget.Box):
    def __init__(self):
        self.is_open = False
        
        btn = CustomIconBtn("", self.open_volume, [])

        self.revealer = Widget.Revealer(
                child = CustomSlider(50.0),
                transition_type = 'slide_right',
                transition_duration = 140,
                reveal_child = self.is_open,
                )

        super().__init__(
                css_classes = ["bar__volume"],
                child = [btn, self.revealer]
                )

    def open_volume(self, *args):
        self.is_open = not self.is_open
        self.revealer.set_reveal_child(self.is_open)
