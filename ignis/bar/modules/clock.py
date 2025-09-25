import datetime

from ignis.widgets import Widget
from ignis.utils import Utils


def update_clock(clock_label: Widget.Label):
    text = datetime.datetime.now().strftime("%I:%M %p")
    clock_label.set_label(text)


clock_lbl = Widget.Label()

Utils.Poll(60000, lambda x: update_clock(clock_lbl))

clock = Widget.Box(
        css_classes = ["bar__clock"],
        child = [
            clock_lbl
            ]
        )
