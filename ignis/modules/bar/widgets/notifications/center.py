"""Notification center bar widget."""

from typing import Any

from ignis import widgets
from ignis.services.notifications import NotificationService

from .popup import NotificationPopup
from .window import NotificationWindow


# Singleton instances
_window: NotificationWindow | None = None
_popup: NotificationPopup | None = None


def get_window() -> NotificationWindow:
    """Get the singleton notification window."""
    global _window
    if _window is None:
        _window = NotificationWindow()
    return _window


def get_popup() -> NotificationPopup:
    """Get the singleton notification popup."""
    global _popup
    if _popup is None:
        _popup = NotificationPopup()
    return _popup


class NotificationCenter(widgets.Box):
    """Bar button that opens the notification panel.

    Displays a clickable label and manages notification popups.
    """

    _service_connected = False

    def __init__(self) -> None:
        """Initialize the notification center widget."""
        self._window = get_window()
        self._popup = get_popup()
        self._service = NotificationService.get_default()

        if not NotificationCenter._service_connected:
            NotificationCenter._service_connected = True
            self._service.connect("notified", self._on_notification)

        trigger_btn = widgets.Button(
            child=widgets.Label(label="𝖓𝖎𝖍𝖎𝖑"),
            css_classes=["notification__trigger"],
            on_click=lambda _: self._toggle(),
        )

        super().__init__(child=[trigger_btn], css_classes=["notification"])

    def _on_notification(self, _: Any, notif: Any) -> None:
        """Handle new notification."""
        self._popup.show_notification(notif)
        if self._window.is_open:
            self._window.update()

    def _toggle(self) -> None:
        """Toggle notification panel visibility."""
        self._window.toggle()
