"""Backlight control widget."""

from enum import Enum
from typing import Any

from ignis import widgets
from ignis.services.backlight import BacklightService

from ...common import IconButton, Slider


class BacklightIcon(Enum):
    """Backlight icon states."""

    NONE = ""
    LOW = ""
    NORMAL = ""


class Backlight(widgets.Box):
    """Backlight control with slider reveal.

    Click to show/hide brightness slider.
    """

    THRESHOLD_LOW = 40

    def __init__(self) -> None:
        """Initialize the backlight widget."""
        self._visible = False

        self._service = BacklightService.get_default()
        self._max_brightness = self._service.max_brightness

        self._service.connect("notify::brightness", self._on_change)

        self._toggle_btn = IconButton(on_click=lambda _: self._toggle())

        self._settings_btn = IconButton(
            icon="",
            on_click=lambda _: None,
        )

        self._slider = Slider(
            step=1,
            initial=self._get_percent(),
            show_value=True,
            on_change=lambda val: self._set_brightness(val),
        )

        self._revealer = widgets.Revealer(
            child=widgets.Box(child=[self._slider, self._settings_btn]),
            transition_type="slide_left",
            transition_duration=280,
            reveal_child=False,
        )

        super().__init__(child=[self._revealer, self._toggle_btn])

    def _toggle(self) -> None:
        """Toggle slider visibility."""
        if not self._service.available:
            return

        self._visible = not self._visible
        self._revealer.set_reveal_child(self._visible)

        if self._visible:
            self._toggle_btn.update_icon("")
        else:
            self._on_change()

    def _on_change(self, *args: Any) -> None:
        """Handle brightness changes."""
        if not self._service.available:
            icon = BacklightIcon.NONE
        elif self._get_percent() < self.THRESHOLD_LOW:
            icon = BacklightIcon.LOW
        else:
            icon = BacklightIcon.NORMAL

        if not self._visible:
            self._toggle_btn.update_icon(icon.value)

    def _set_brightness(self, percent: float) -> None:
        """Set brightness from percentage."""
        if self._service.available:
            value = round(self._max_brightness / 100 * percent)
            self._service.brightness = value

    def _get_percent(self) -> int:
        """Get current brightness as percentage."""
        return int(self._service.brightness / self._max_brightness * 100)
