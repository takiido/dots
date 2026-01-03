"""System tray widget."""

from typing import Any, List

from ignis import widgets
from ignis.services.system_tray import SystemTrayItem, SystemTrayService

from ...common import IconButton


class Tray(widgets.Box):
    """Collapsible system tray with overflow support.

    Shows up to MAX_VISIBLE icons, with remaining icons
    accessible via a toggle button.
    """

    MAX_VISIBLE = 3

    ICON_EXPAND = ""
    ICON_COLLAPSE = ""

    def __init__(self) -> None:
        """Initialize the system tray widget."""
        self._items: List[SystemTrayItem] = []
        self._expanded = False

        self._visible_box = widgets.Box()
        self._overflow_box = widgets.Box()

        self._overflow_revealer = widgets.Revealer(
            child=self._overflow_box,
            transition_type="slide_left",
            transition_duration=280,
            reveal_child=False,
        )

        self._toggle_btn = IconButton(
            icon=self.ICON_EXPAND,
            on_click=lambda _: self._toggle_overflow(),
        )
        self._toggle_btn.set_visible(False)

        service = SystemTrayService.get_default()
        service.connect("added", lambda _, item: self._add_item(item))

        super().__init__(
            child=[self._overflow_revealer, self._visible_box, self._toggle_btn]
        )

    def _add_item(self, item: SystemTrayItem) -> None:
        """Add a new tray item."""
        self._items.append(item)
        item.connect("removed", self._remove_item)
        self._update()

    def _remove_item(self, item: SystemTrayItem) -> None:
        """Remove a tray item."""
        if item in self._items:
            self._items.remove(item)
            self._update()

    def _toggle_overflow(self) -> None:
        """Toggle overflow visibility."""
        self._expanded = not self._expanded
        self._overflow_revealer.set_reveal_child(self._expanded)
        self._toggle_btn.update_icon(
            self.ICON_COLLAPSE if self._expanded else self.ICON_EXPAND
        )

    def _update(self) -> None:
        """Rebuild tray display."""
        total = len(self._items)
        has_overflow = total > self.MAX_VISIBLE

        # Visible items (most recent)
        visible = [self._create_icon(i) for i in self._items[-self.MAX_VISIBLE:]]
        self._visible_box.set_child(visible)

        # Overflow items
        if has_overflow:
            overflow = [self._create_icon(i) for i in self._items[:-self.MAX_VISIBLE]]
            self._overflow_box.set_child(overflow)
        else:
            self._overflow_box.set_child([])
            if self._expanded:
                self._expanded = False
                self._overflow_revealer.set_reveal_child(False)

        self._toggle_btn.set_visible(has_overflow)
        if not has_overflow:
            self._toggle_btn.update_icon(self.ICON_EXPAND)

    def _create_icon(self, item: SystemTrayItem) -> widgets.Button:
        """Create a tray icon button."""
        icon = widgets.Icon(image=item.icon)
        btn = widgets.Button(
            child=icon,
            css_classes=["tray__icon"],
            on_click=lambda _, i=item: (
                i.activate(0, 0) if hasattr(i, "activate") else None
            ),
        )
        btn.set_tooltip_text(getattr(item, "title", "") or "")
        return btn
