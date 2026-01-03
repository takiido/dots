"""Volume control widget."""

from enum import Enum
from typing import Any, Optional

from ignis import widgets
from ignis.services.audio import AudioService

from ...common import IconButton, Slider


class SpeakerIcon(Enum):
    """Speaker icon states."""

    NONE = ""
    LOW = ""
    NORMAL = ""
    HIGH = ""
    MUTED = ""


class Volume(widgets.Box):
    """Volume control with slider reveal.

    Click to show/hide volume slider, mute button, and controls.
    """

    THRESHOLD_HIGH = 75
    THRESHOLD_LOW = 20

    def __init__(self) -> None:
        """Initialize the volume widget."""
        self._speakers: list = []
        self._default_speaker: Optional[Any] = None
        self._visible = False

        self._audio = AudioService.get_default()
        self._audio.connect("speaker-added", lambda _, s: self._on_speaker_added(s))

        self._toggle_btn = IconButton(on_click=lambda _: self._toggle_slider())

        self._mute_btn = IconButton(
            on_click=lambda _: self._toggle_mute(),
        )

        self._settings_btn = IconButton(
            icon="",
            on_click=lambda _: None,
        )

        self._slider = Slider(
            step=1,
            show_value=True,
            on_change=lambda val: self._set_volume(round(val)),
        )

        self._revealer = widgets.Revealer(
            child=widgets.Box(
                child=[self._mute_btn, self._slider, self._settings_btn]
            ),
            transition_type="slide_left",
            transition_duration=280,
            reveal_child=False,
        )

        super().__init__(child=[self._revealer, self._toggle_btn])

    def _toggle_slider(self) -> None:
        """Toggle slider visibility."""
        if self._default_speaker is None:
            return

        self._visible = not self._visible
        self._revealer.set_reveal_child(self._visible)

        if self._visible:
            self._toggle_btn.update_icon("")
        else:
            self._update_icon()

    def _on_speaker_added(self, speaker: Any) -> None:
        """Handle new speaker device."""
        if speaker in self._speakers:
            return

        self._speakers.append(speaker)
        speaker.connect("removed", self._on_speaker_removed)

        if speaker.is_default:
            self._slider.set_value(speaker.volume)
            self._default_speaker = speaker
            speaker.stream.connect("notify::is-muted", self._update_icon)
            speaker.stream.connect("notify::volume", self._update_icon)
            self._update_icon()

    def _on_speaker_removed(self, speaker: Any) -> None:
        """Handle speaker removal."""
        if speaker in self._speakers:
            self._speakers.remove(speaker)

    def _update_icon(self, *args: Any) -> None:
        """Update speaker icon based on state."""
        if self._default_speaker is None:
            icon = SpeakerIcon.NONE
        elif self._default_speaker.is_muted:
            icon = SpeakerIcon.MUTED
        else:
            vol = self._default_speaker.volume
            if vol > self.THRESHOLD_HIGH:
                icon = SpeakerIcon.HIGH
            elif vol > self.THRESHOLD_LOW:
                icon = SpeakerIcon.NORMAL
            else:
                icon = SpeakerIcon.LOW

        if not self._visible:
            self._toggle_btn.update_icon(icon.value)
        self._mute_btn.update_icon(icon.value)

    def _set_volume(self, value: int) -> None:
        """Set speaker volume."""
        if self._default_speaker:
            self._default_speaker.volume = value

    def _toggle_mute(self) -> None:
        """Toggle speaker mute state."""
        if self._default_speaker:
            self._default_speaker.is_muted = not self._default_speaker.is_muted
            self._update_icon()
