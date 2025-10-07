from ignis import widgets

from .widgets.dash import Dash
from .widgets.clock import Clock
from .widgets.mode import Mode
from .widgets.tray import Tray


class Bar(widgets.Window):
    __gtype_name__ = "Bar"

    def __init__(self, monitor: int, control_centre):
        self.control_centre = control_centre

        lWidgets = widgets.Box(child=[Mode()])

        cWidgets = widgets.Box(child=[widgets.Label(label="𝖓𝖎𝖍𝖎𝖑")])

        rWidgets = widgets.Box(
            child=[
                Tray(),
                Dash(control_centre),
                Clock(),
            ]
        )

        barContainer = widgets.CenterBox(
            vertical=False,
            start_widget=lWidgets,
            center_widget=cWidgets,
            end_widget=rWidgets,
        )

        super().__init__(
            namespace=f"bar-{monitor}",
            monitor=monitor,
            exclusivity="exclusive",
            anchor=["left", "bottom", "right"],
            child=barContainer,
        )
