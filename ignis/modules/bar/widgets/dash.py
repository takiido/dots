"""Dashboard widget grouping backlight and volume controls."""

from ignis import widgets

from .backlight import Backlight
from .volume import Volume


class Dash(widgets.Box):
    """Container for system control widgets (backlight, volume)."""

    def __init__(self) -> None:
        """Initialize the dashboard widget."""
        super().__init__(child=[Backlight(), Volume()])
