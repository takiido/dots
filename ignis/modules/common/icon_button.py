"""Reusable icon button component."""

from typing import Callable, Optional

from gi.repository import Gtk
from ignis import widgets


class IconButton(widgets.Button):
    """A button that displays an icon font glyph.

    Supports left-click and optional right-click handlers.
    """

    def __init__(
        self,
        icon: str = "",
        on_click: Optional[Callable] = None,
        on_right_click: Optional[Callable] = None,
    ) -> None:
        """Initialize the icon button.

        Args:
            icon: Icon font glyph to display.
            on_click: Left-click callback.
            on_right_click: Right-click callback.
        """
        self.btn_label = widgets.Label(
            style="font-family: 'Phosphor';",
            label=icon,
        )

        super().__init__(
            css_classes=["bar__icon-btn"],
            child=self.btn_label,
            on_click=on_click,
        )

        if on_right_click:
            gesture = Gtk.GestureClick()
            gesture.set_button(3)
            gesture.connect("released", lambda g, n, x, y: on_right_click())
            self.add_controller(gesture)

    def update_icon(self, icon: str) -> None:
        """Update the displayed icon.

        Args:
            icon: New icon glyph to display.
        """
        self.btn_label.set_label(icon)
