"""Workspaces button component"""

from ignis import widgets

class WorkspaceBtn(widgets.Button):
    service = None;

    def __init__(self, label, workspace) -> None:
        self._label = widgets.Label(label=label, css_classes=["workspace_btn_label"])
        self.workspace = workspace

        super().__init__(
                child=self._label,
                css_classes=["workspace_btn"],
                on_click=lambda _: self._switch_to_workspace()
            )

    def _switch_to_workspace(self):
        self.workspace.switch_to()


    def update_active(self, is_active: bool):
        if is_active:
            self.css_classes = ["workspace_btn", "workspace_btn--active"]
        else: ["workspace_btn"]
