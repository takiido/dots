import datetime
from ignis import widgets
from ignis import utils


class Clock(widgets.Box):
    def update_label(self):
        text = datetime.datetime.now().strftime("%H:%M %p")
        self.clock_label.set_label(text)

    def __init__(self):
        self.clock_label = widgets.Label(label="clock")

        utils.Poll(60000, lambda x: self.update_label())
        super().__init__(child=[self.clock_label])
