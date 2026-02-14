"""Workspaces button component"""

from ignis import widgets
from ignis.services.hyprland import HyprlandWorkspace

class WorkspaceBtn(widgets.Button):
    service = None;

    def __init__(self, id, label, service) -> None:
        self.id = id;
        self._label = widgets.Label(label=label)
        self._active = False
        self.service = service

        super().__init__(
                child=self._label,
                css_classes=["workspace_btn"],
                on_click=lambda _: self.switch_to_workspace(id)
                )

    def toggle_active(self):
        self._active = not self._active
        self.css_classes = ["workspace_btn--active"] if self._active else ["workspace_btn"]

    def switch_to_workspace(self, id):
        workspace = self.service.workspaces[id]
        HyprlandWorkspace.switch_to(workspace)
