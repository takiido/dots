"""Notification history window component."""

from datetime import datetime
from typing import Any

from ignis import widgets
from ignis.services.notifications import NotificationService


class NotificationWindow(widgets.Window):
    """Popup window displaying notification history.

    Shows a scrollable list of past notifications with dismiss controls.
    """

    __gtype_name__ = "NotificationWindow"

    def __init__(self) -> None:
        """Initialize the notification history window."""
        self.is_open = False
        self._service = NotificationService.get_default()

        self._list_box = widgets.Box(
            vertical=True,
            hexpand=True,
            spacing=12,
            css_classes=["notification-panel__list"],
        )

        header = widgets.Box(
            hexpand=True,
            child=[
                widgets.Label(
                    label="Notifications",
                    css_classes=["notification-panel__title"],
                ),
            ],
            css_classes=["notification-panel__header"],
        )

        self._empty_label = widgets.Label(
            label="No notifications",
            css_classes=["notification-panel__empty"],
        )

        scroll = widgets.Scroll(
            child=self._list_box,
            height_request=400,
            width_request=380,
        )

        panel = widgets.Box(
            vertical=True,
            child=[header, scroll],
            css_classes=["notification-panel"],
        )

        super().__init__(
            css_classes=["notification-panel"],
            namespace="notification",
            anchor=["top"],
            visible=False,
            popup=True,
            layer="top",
            child=panel,
        )

        self._update()

    def toggle(self) -> None:
        """Toggle window visibility."""
        self.is_open = not self.is_open
        self.set_visible(self.is_open)
        if self.is_open:
            self._update()

    def clear_all(self) -> None:
        """Clear all notifications."""
        self._service.clear_all()
        self._update()

    def update(self) -> None:
        """Public method to refresh the notification list."""
        self._update()

    def _update(self) -> None:
        """Refresh the notification list."""
        notifications = self._service.notifications

        if not notifications:
            self._list_box.set_child([self._empty_label])
            return

        items = [self._create_item(n) for n in reversed(notifications)]
        self._list_box.set_child(items)

    def _create_item(self, notif: Any) -> widgets.Box:
        """Create a notification list item widget."""
        app_name = notif.app_name or "Unknown"
        summary = self._truncate(notif.summary or "", 40)
        body = self._truncate(notif.body or "", 60)
        time_str = self._format_time(notif.time)

        header = widgets.Box(
            hexpand=True,
            child=[
                widgets.Label(label=app_name, css_classes=["notification-item__app"]),
                widgets.Box(hexpand=True),
                widgets.Label(label=time_str, css_classes=["notification-item__time"]),
            ],
            css_classes=["notification-item__header"],
        )

        summary_label = widgets.Label(
            label=summary,
            css_classes=["notification-item__title"],
            xalign=0,
            ellipsize="end",
        )

        body_label = widgets.Label(
            label=body,
            css_classes=["notification-item__body"],
            xalign=0,
            ellipsize="end",
        )

        close_btn = widgets.Button(
            child=widgets.Label(label=""),
            css_classes=["notification-item__close"],
            on_click=lambda _, n=notif: self._close_notification(n),
        )

        content = widgets.Box(
            hexpand=True,
            vertical=True,
            child=[summary_label, body_label],
            spacing=8,
            css_classes=["notification-item__content"],
        )

        wrapper = widgets.Box(
            hexpand=True,
            child=[content, close_btn],
            css_classes=["notification-item__wrapper"],
        )

        return widgets.Box(
            vertical=True,
            child=[header, wrapper],
            css_classes=["notification-item"],
        )

    def _close_notification(self, notif: Any) -> None:
        """Close a single notification."""
        notif.close()
        self._update()

    def _truncate(self, text: str, max_len: int) -> str:
        """Truncate text to single line with ellipsis."""
        text = text.replace("\n", " ").replace("\r", " ").strip()
        return text[:max_len - 3] + "..." if len(text) > max_len else text

    def _format_time(self, timestamp: float) -> str:
        """Format timestamp for display."""
        dt = datetime.fromtimestamp(timestamp)
        now = datetime.now()

        if dt.date() == now.date():
            return dt.strftime("%H:%M")
        elif (now - dt).days == 1:
            return "Yesterday " + dt.strftime("%H:%M")
        return dt.strftime("%m/%d %H:%M")
