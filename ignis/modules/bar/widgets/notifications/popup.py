"""Notification popup toast component."""

from datetime import datetime
from typing import Any, Dict, List

from gi.repository import GLib
from ignis import widgets


class NotificationPopup(widgets.Window):
    """Floating popup window for toast notifications.

    Supports stacking multiple notifications with auto-dismiss.
    """

    __gtype_name__ = "NotificationPopup"

    TIMEOUT_MS = 30000

    def __init__(self) -> None:
        """Initialize the notification popup window."""
        self._active_popups: List[Dict[str, Any]] = []

        self._popup_box = widgets.Box(
            vertical=True,
            css_classes=["notification-popup__container"],
        )

        super().__init__(
            css_classes=["notification-popup"],
            namespace="notification-popup",
            anchor=["top", "right"],
            visible=False,
            popup=True,
            layer="overlay",
            child=self._popup_box,
        )

    def show_notification(self, notif: Any) -> None:
        """Display a notification toast.

        Args:
            notif: Notification object from NotificationService.
        """
        app_name = notif.app_name or "Unknown"
        summary = self._truncate(notif.summary or "", 50)
        body = self._truncate((notif.body or "").replace("\n", " ").strip(), 80)
        time_str = datetime.fromtimestamp(notif.time).strftime("%H:%M")

        popup_id = id(notif)

        header = widgets.Box(
            hexpand=True,
            child=[
                widgets.Label(label=app_name, css_classes=["notification-popup__app"]),
                widgets.Label(label=time_str, css_classes=["notification-popup__time"]),
            ],
            css_classes=["notification-popup__header"],
        )

        summary_label = widgets.Label(
            label=summary,
            css_classes=["notification-popup__title"],
            xalign=0,
            ellipsize="end",
        )

        content_children = [header, summary_label]

        if body:
            body_label = widgets.Label(
                label=body,
                css_classes=["notification-popup__body"],
                xalign=0,
                ellipsize="end",
            )
            content_children.append(body_label)

        content = widgets.Box(
            vertical=True,
            child=content_children,
            css_classes=["notification-popup__content"],
        )

        timeout_id = GLib.timeout_add(
            self.TIMEOUT_MS,
            lambda pid=popup_id: self._auto_close(pid),
        )

        self._active_popups.append({
            "id": popup_id,
            "notif": notif,
            "widget": content,
            "timeout_id": timeout_id,
        })

        self._update_display()
        self.set_visible(True)

    def _truncate(self, text: str, max_len: int) -> str:
        """Truncate text with ellipsis."""
        return text[:max_len - 3] + "..." if len(text) > max_len else text

    def _update_display(self) -> None:
        """Rebuild popup display with all active notifications."""
        self._popup_box.set_child([p["widget"] for p in self._active_popups])

    def _remove_popup(self, popup_id: int, dismiss: bool = False) -> None:
        """Remove a popup by ID."""
        for i, popup in enumerate(self._active_popups):
            if popup["id"] == popup_id:
                if popup["timeout_id"]:
                    GLib.source_remove(popup["timeout_id"])
                if dismiss and popup["notif"]:
                    popup["notif"].dismiss()
                self._active_popups.pop(i)
                break

        if self._active_popups:
            self._update_display()
        else:
            self.set_visible(False)

    def _auto_close(self, popup_id: int) -> bool:
        """Auto-close handler for timeout."""
        self._remove_popup(popup_id, dismiss=False)
        return False
