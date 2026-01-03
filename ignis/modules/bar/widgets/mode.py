"""Mode indicator widget."""

from ignis import widgets


class Mode(widgets.Box):
    """Displays the current device mode (Normal/Tablet/Docked)."""

    MODES = ["Normal", "Tablet", "Docked"]

    def __init__(self) -> None:
        """Initialize the mode widget."""
        label = widgets.Label(label=self.MODES[0])
        super().__init__(child=[label])
