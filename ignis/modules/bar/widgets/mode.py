from enum import Enum
from ignis import widgets


class Mode(widgets.Box):
    def __init__(self):
        modes = ["Normal", "Tablet", "Docked"]
        mode_label = widgets.Label(label=modes[0])

        super().__init__(child=[mode_label])
