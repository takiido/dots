"""Workspaces display widget."""

from enum import Enum
from typing import Any, Optional

from ignis import utils
from ignis import widgets
from ignis.services.hyprland import HyprlandService

from .workspace_btn import WorkspaceBtn

class WorkspaceLetter(Enum):
    А = 1
    Б = 2
    В = 3
    Г = 4
    Д = 5
    Е = 6


class Workspaces(widgets.Box):
    """Displays the active window title.

    Subscribes to Hyprland to track window focus changes.
    """

    def __init__(self, monitor_id: int) -> None:
        """Initialize the window name widget."""
        self._hyprland = HyprlandService.get_default()

        self._monitor = utils.get_monitor(monitor_id).get_connector()

        self._hyprland.connect("notify::workspaces", lambda *_: self._on_workspaces_change())
        self._hyprland.connect("notify::active-workspace", lambda *_: self._on_active_change())

        self._workspaces = None

        super().__init__(child=[], css_classes=["workspaces"])

    def _on_workspaces_change(self, *_) -> None:
        self.child = []
        for i in self._hyprland.workspaces:
            if (i.monitor == self._monitor):
                btn = WorkspaceBtn(
                        label = WorkspaceLetter(i.id).name,
                        workspace = i
                        )
                self.child = self.child + [btn]

    def _on_active_change(self, *_) -> None:
        active_id = self._hyprland.active_workspace.id
        for btn in self.child:
           is_active = (btn.workspace.id == active_id)
           btn.update_active(is_active)
    
    def _remove_workspace(self, w) -> None:
        self.child = [btn for btn in self.child if btn.workspace != w]
