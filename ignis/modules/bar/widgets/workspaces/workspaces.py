"""Workspaces display widget."""

from enum import Enum
from typing import Any, Optional

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

    def __init__(self, workspaces: Any) -> None:
        """Initialize the window name widget."""
        self._hyprland = HyprlandService.get_default()
        self._active_workspace = None
        self._hyprland.connect("notify::active-workspace", self._on_active_change)


        super().__init__(child=[])

        self._populate(workspaces)
    
    def _populate(self, w) -> None:
        """Add buttons based on workspaces"""
        for i in w:
            btn = WorkspaceBtn(
                    id = i,
                    label = WorkspaceLetter(i).name,
                    service=self._hyprland
                    )
            self.child = self.child + [btn]

    def _on_active_change(self, *args: Any) -> None:
        """Handle active workspace change"""
        for i in self.child:
            if i.id == self._hyprland.active_workspace:
                self._active_workspace = i
        
        for i in self.child:
            if i.id == self._active_workspace.id:
                i.toggle_active();

