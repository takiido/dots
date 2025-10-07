from ignis import widgets
from .sections import Mixer


class ControlCentre(widgets.RevealerWindow):
    __gtype_name__ = "ControlCentre"

    def __init__(self, monitor: int):
        self.is_open = False

        self.control_centre_container = widgets.Box(child=[Mixer()])

        revealer = widgets.Revealer(
            transition_type="slide_up",
            transition_duration=70,
            child=self.control_centre_container,
            reveal_child=True,
        )

        box = widgets.Box(width_request=400, child=[revealer])

        super().__init__(
            anchor=["right", "bottom"],
            namespace=f"control_centre-{monitor}",
            visible=self.is_open,
            popup=True,
            layer="top",
            revealer=revealer,
            child=box,
        )

    def toggle(self, section: str = ""):
        self.is_open = not self.is_open
        self.set_visible(self.is_open)
