import math

from ignis.widgets import Widget


class CustomSlider(Widget.Box):
    def __init__(self, init_value: float):
        self.value = init_value
        self.ascii = [
                "░░░░░░░░░░",
                "▓░░░░░░░░░",
                "▓▓░░░░░░░░",
                "▓▓▓░░░░░░░",
                "▓▓▓▓░░░░░░",
                "▓▓▓▓▓░░░░░",
                "▓▓▓▓▓▓░░░░",
                "▓▓▓▓▓▓▓░░░",
                "▓▓▓▓▓▓▓▓░░",
                "▓▓▓▓▓▓▓▓▓░",
                "▓▓▓▓▓▓▓▓▓▓"
                ]

        self.label = Widget.Label(
                css_classes = ["custom-slider-ascii"],
                label = self.ascii[math.ceil(self.value/10)]
                )
        
        self.value_label = Widget.Label(
                label = str(int(self.value)) + "%"
                )

        slider = Widget.Scale(
                min = 0,
                max = 100,
                step = 1,
                value = self.value,
                on_change = lambda x: self.update_ascii(value = x.value),
                draw_value = False
                )

        overlay = Widget.Overlay(
                width_request = 200,
                child = self.label,
                overlays = [slider]
                )
                     

        super().__init__(
                css_classes = ["custom-slider"],
                child = [overlay, self.value_label]
                )

    def update_ascii(self, value):
        self.label.set_label(self.ascii[math.ceil(value/10)])
        self.value_label.set_label(str(int(value)) + "%")
        print(value)

