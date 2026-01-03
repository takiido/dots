"""Window name display widget."""

from typing import Any, Optional

from ignis import widgets
from ignis.services.hyprland import HyprlandService


class WindowName(widgets.Box):
    """Displays the active window title.

    Subscribes to Hyprland to track window focus changes.
    """

    MAX_CHARS = 60

    def __init__(self) -> None:
        """Initialize the window name widget."""
        self._label = widgets.Label(
            label="-",
            ellipsize="end",
            max_width_chars=self.MAX_CHARS,
        )

        super().__init__(child=[self._label], style="margin-left: 10px;")

        self._hyprland = HyprlandService.get_default()
        self._hyprland.connect("notify::active-window", self._on_focus_change)

        self._current_window: Optional[Any] = None
        self._handler_id: Optional[int] = None

        self._on_focus_change()

    def _on_focus_change(self, *args: Any) -> None:
        """Handle window focus changes."""
        if self._current_window and self._handler_id:
            try:
                self._current_window.disconnect(self._handler_id)
            except Exception:
                pass

        self._current_window = self._hyprland.active_window
        self._handler_id = None

        if self._current_window:
            self._update_label()
            self._handler_id = self._current_window.connect(
                "notify::title",
                self._update_label,
            )
        else:
            self._label.set_label("Desktop")

    def _update_label(self, *args: Any) -> None:
        """Update the displayed window title."""
        if self._current_window:
            title = self._current_window.title
            if not title:
                title = self._current_window.class_name or "..."
            self._label.set_label(title)
