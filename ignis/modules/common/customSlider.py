from ignis import widgets


class CustomSlider(widgets.Box):
    def set_value(self, value: int):
        self.scale.set_value(value)
        self.update_ascii(value, subfunc=None)

    def update_ascii(self, value: int, subfunc):
        new_ascii = f"[{self.ascii_text[int(value / 10)]}]"
        self.ascii_label.set_label(new_ascii)
        self.value_label.set_label(f"{int(value)}%")
        if callable(subfunc):
            subfunc(value)

    def __init__(
        self,
        on_change,
        min: int = 0,
        max: int = 100,
        init_val: int = 50,
        draw_value=False,
        step: int = 10,
    ):
        self.ascii_text = [
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
            "▓▓▓▓▓▓▓▓▓▓",
        ]

        self.ascii_label = widgets.Label(label="[░░░░░░░░░░]")
        self.scale = widgets.Scale(
            min=min,
            max=max,
            step=step,
            value=init_val,
            on_change=lambda x: self.update_ascii(
                value=int(x.value), subfunc=on_change
            ),
        )
        self.slider_wrapper = widgets.Overlay(
            child=self.ascii_label, overlays=[self.scale]
        )
        self.value_label = widgets.Label(width_request=50, label=f"{init_val}%")

        self.update_ascii(init_val, subfunc=on_change)
        super().__init__(
            child=[self.slider_wrapper, self.value_label if draw_value else None]
        )
