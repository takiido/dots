import os
import sys
from enum import Enum
from ignis import widgets
from ignis.services.backlight import BacklightService
from .customIconBtn import CustomIconBtn
from ...common.customSlider import CustomSlider


class BacklightState(Enum):
    NONE = ""
    LOW = ""
    NORMAL = ""


class Backlight(widgets.Box):
    BACKLIGHT_LOW_THRESHOLD = 40

    def __init__(self):
        self.is_backlight_visible = False

        self.backlight_serv = BacklightService.get_default()
        self.max_brightness = self.backlight_serv.max_brightness

        self.backlight_serv.connect("notify::brightness", self.on_backlight_change)

        self.slider_toggle_btn = CustomIconBtn(
            on_click=lambda _: self.open_backlight_slider()
        )

        self.backlight_control_btn = CustomIconBtn(
            icon="", on_click=lambda _: print("OPEN DASH BACKLIGHT CONTROL PANEL")
        )

        self.backlight_slider = CustomSlider(
            step=1,
            init_val=self.__convert_brightness(),
            draw_value=True,
            on_change=lambda val: self.set_brightness(
                round(self.max_brightness / 100 * val)
            ),
        )

        self.backlight_revealer = widgets.Revealer(
            child=widgets.Box(
                child=[self.backlight_slider, self.backlight_control_btn]
            ),
            transition_type="slide_left",
            transition_duration=280,
            reveal_child=self.is_backlight_visible,
        )

        super().__init__(child=[self.backlight_revealer, self.slider_toggle_btn])

    def open_backlight_slider(self):
        if self.backlight_serv.available is not None:
            self.is_backlight_visible = not self.is_backlight_visible
            self.backlight_revealer.set_reveal_child(self.is_backlight_visible)

            if self.is_backlight_visible:
                self.slider_toggle_btn.update_icon("")
            else:
                self.on_backlight_change()

    def on_backlight_change(self, service=None, _=None):
        if self.backlight_serv.available:
            brightness = self.__convert_brightness()
            if brightness < self.BACKLIGHT_LOW_THRESHOLD:
                self.update_backlight_icon(BacklightState.LOW)
            else:
                self.update_backlight_icon(BacklightState.NORMAL)
        else:
            self.update_backlight_icon(BacklightState.NONE)

    def update_backlight_icon(self, state: BacklightState):
        if not self.is_backlight_visible:
            self.slider_toggle_btn.update_icon(state.value)

    def set_brightness(self, value):
        if self.backlight_serv.available:
            self.backlight_serv.brightness = value

    def __convert_brightness(self) -> int:
        return self.backlight_serv.brightness / self.max_brightness * 100
