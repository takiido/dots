"""Main status bar window."""

from ignis import widgets

from .widgets import (
    Bluetooth,
    Clock,
    Dash,
    Mode,
    Network,
    NotificationCenter,
    Tray,
    WindowName,
)


class Bar(widgets.Window):
    """Top status bar for the desktop.

    Contains left, center, and right widget groups.
    """

    __gtype_name__ = "Bar"

    def __init__(self, monitor: int) -> None:
        """Initialize the bar for a specific monitor.

        Args:
            monitor: Monitor index to display on.
        """
        left = widgets.Box(child=[Mode(), WindowName()])
        center = widgets.Box(child=[NotificationCenter()])
        right = widgets.Box(
            child=[
                Tray(),
                Bluetooth(),
                Network(),
                Dash(),
                Clock(),
            ]
        )

        container = widgets.CenterBox(
            vertical=False,
            start_widget=left,
            center_widget=center,
            end_widget=right,
        )

        super().__init__(
            namespace=f"bar-{monitor}",
            monitor=monitor,
            css_classes=["bar"],
            exclusivity="exclusive",
            anchor=["left", "top", "right"],
            child=container,
        )
