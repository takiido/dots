from enum import Enum
from ignis import widgets
from ignis.services.audio import AudioService
from .customIconBtn import CustomIconBtn
from ...common.customSlider import CustomSlider


class SpeakerState(Enum):
    NONE = ""
    LOW = ""
    NORMAL = ""
    HIGH = ""
    MUTED = ""
    HEADPHONES = ""
    BT = "󰥰"


class Volume(widgets.Box):
    VOLUME_HIGH_THRESHOLD = 75
    VOLUME_LOW_THRESHOLD = 20

    def __init__(self):
        self.speakers = []
        self.default_speaker = None
        self.is_volume_visible = False

        self.audio_serv = AudioService.get_default()
        self.audio_serv.connect(
            "speaker-added", lambda _, speaker: self.on_speaker_added(speaker)
        )

        self.slider_toggle_btn = CustomIconBtn(
            on_click=lambda _: self.open_volume_slider()
        )

        self.mute_btn = CustomIconBtn(
            on_click=lambda _: self.toggle_mute(self.default_speaker)
        )

        self.volume_control_btn = CustomIconBtn(
            icon="",
            on_click=lambda _: print("OPEN DASH VOLUME CONTROL PANEL"),
        )
        self.vol_slider = CustomSlider(
            step=1,
            draw_value=True,
            on_change=lambda val: self.set_volume(round(val)),
        )

        self.vol_revealer = widgets.Revealer(
            child=widgets.Box(
                child=[
                    self.mute_btn,
                    self.vol_slider,
                    self.volume_control_btn,
                ]
            ),
            transition_type="slide_left",
            transition_duration=280,
            reveal_child=self.is_volume_visible,
        )

        super().__init__(child=[self.vol_revealer, self.slider_toggle_btn])

    def open_volume_slider(self):
        if self.default_speaker is not None:
            self.is_volume_visible = not self.is_volume_visible
            self.vol_revealer.set_reveal_child(self.is_volume_visible)

            if self.is_volume_visible:
                self.slider_toggle_btn.update_icon("")
            else:
                self.on_speaker_change()

    def on_speaker_added(self, speaker):
        if speaker not in self.speakers:
            self.speakers.append(speaker)
            speaker.connect("removed", self.on_speaker_removed)

            if speaker.is_default:
                self.vol_slider.set_value(speaker.volume)
                self.default_speaker = speaker

                speaker.stream.connect("notify::is-muted", self.on_speaker_change)
                speaker.stream.connect("notify::volume", self.on_speaker_change)

                self.on_speaker_change()

    def on_speaker_removed(self, speaker):
        if speaker in self.speakers:
            self.speakers.remove(speaker)

    def on_speaker_change(self, stream=None, _=None):
        if self.default_speaker is not None:
            if self.default_speaker.is_muted:
                self.update_speaker_icon(SpeakerState.MUTED)
            else:
                vol = self.default_speaker.volume
                if vol > self.VOLUME_HIGH_THRESHOLD:
                    self.update_speaker_icon(SpeakerState.HIGH)
                elif vol > self.VOLUME_LOW_THRESHOLD:
                    self.update_speaker_icon(SpeakerState.NORMAL)
                else:
                    self.update_speaker_icon(SpeakerState.LOW)
        else:
            self.update_speaker_icon(SpeakerState.NONE)

    def update_speaker_icon(self, state: SpeakerState):
        if not self.is_volume_visible:
            self.slider_toggle_btn.update_icon(state.value)
        self.mute_btn.update_icon(state.value)

    def set_volume(self, value):
        if self.default_speaker is not None:
            self.default_speaker.volume = value

    def toggle_mute(self, speaker):
        if speaker is not None:
            speaker.is_muted = not speaker.is_muted
            self.on_speaker_change()
