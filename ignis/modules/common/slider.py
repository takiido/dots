"""Custom ASCII-style slider component."""

from typing import Callable

from ignis import widgets


class Slider(widgets.Box):
    """A slider with ASCII visualization overlay.

    Displays a progress bar using block characters (░▓) with
    an optional percentage label.
    """

    ASCII_LEVELS = [
        "░░░░░░░░░░",
        "▓░░░░░░░░░",
        "▓▓░░░░░░░░",
        "▓▓▓░░░░░░░",
        "▓▓▓▓░░░░░░",
        "▓▓▓▓▓░░░░░",
        "▓▓▓▓▓▓░░░░",
        "▓▓▓▓▓▓▓░░░",
        "▓▓▓▓▓▓▓▓░░",
        "▓▓▓▓▓▓▓▓▓░",
        "▓▓▓▓▓▓▓▓▓▓",
    ]

    def __init__(
        self,
        on_change: Callable[[float], None],
        min_val: int = 0,
        max_val: int = 100,
        initial: int = 50,
        step: int = 10,
        show_value: bool = False,
    ) -> None:
        """Initialize the slider.

        Args:
            on_change: Callback when value changes.
            min_val: Minimum value.
            max_val: Maximum value.
            initial: Initial value.
            step: Step increment.
            show_value: Whether to show percentage label.
        """
        self._on_change = on_change

        self._ascii_label = widgets.Label(label="[░░░░░░░░░░]")
        self._value_label = widgets.Label(width_request=50, label=f"{initial}%")

        self._scale = widgets.Scale(
            min=min_val,
            max=max_val,
            step=step,
            value=initial,
            on_change=lambda x: self._on_scale_change(int(x.value)),
        )

        slider_wrapper = widgets.Overlay(
            child=self._ascii_label,
            overlays=[self._scale],
        )

        children = [slider_wrapper]
        if show_value:
            children.append(self._value_label)

        self._update_display(initial)

        super().__init__(child=children)

    def set_value(self, value: int) -> None:
        """Set the slider value programmatically.

        Args:
            value: New value to set.
        """
        self._scale.set_value(value)
        self._update_display(value)

    def _on_scale_change(self, value: int) -> None:
        """Handle scale value changes."""
        self._update_display(value)
        if self._on_change:
            self._on_change(value)

    def _update_display(self, value: int) -> None:
        """Update ASCII and percentage display."""
        level = min(10, max(0, int(value / 10)))
        self._ascii_label.set_label(f"[{self.ASCII_LEVELS[level]}]")
        self._value_label.set_label(f"{int(value)}%")
