from ignis import widgets
from ignis.services.system_tray import SystemTrayService
from ignis.services.system_tray import SystemTrayItem


class Tray(widgets.Box):
    def add_to_tray(self, item: SystemTrayItem):
        self.tray_items.append(item)
        self.update_tray()

    def remove_from_tray(self, item):
        self.tray_items.remove(item)

    def update_tray(self):
        front_items = []
        back_items = []
        tray_len = len(self.tray_items)

        for i in range(tray_len):
            if i < 3:
                front_items.append(widgets.Icon(image=self.tray_items[i].icon))
                self.front_tray.set_child(front_items)
            back_items.append(widgets.Icon(image=self.tray_items[i].icon))

    def __init__(self):
        sys_tray = SystemTrayService.get_default()
        self.tray_items = []

        self.front_tray = widgets.Box()

        sys_tray.connect("added", lambda x, item: self.add_to_tray(item))

        super().__init__(child=[self.front_tray])
