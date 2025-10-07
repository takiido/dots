from ignis import widgets
from ignis.services.audio import AudioService


class Mixer(widgets.Box):
    def __init__(self):
        self.speakers = []
        self.apps = []
        self.mics = []
        self.recs = []

        self.audio_serv = AudioService.get_default()
        self.audio_serv.connect(
            "speaker-added", lambda _, speaker: self.on_stream_added(speaker, "speaker")
        )
        self.audio_serv.connect(
            "microphone-added", lambda _, mic: self.on_stream_added(mic, "mic")
        )
        self.audio_serv.connect(
            "app-added", lambda _, app: self.on_stream_added(app, "app")
        )
        self.audio_serv.connect(
            "recorder-added", lambda _, rec: self.on_stream_added(rec, "rec")
        )

        super().__init__()

    def on_stream_added(self, stream, type: str):
        match type:
            case "app":
                self.apps.append(stream)
                print(f"App added: {stream.name}")
            case "speaker":
                self.speakers.append(stream)
                print(f"Speaker added {stream.name}")
            case "mic":
                self.mics.append(stream)
                print(f"Mic added: {stream.name}")
            case "rec":
                self.recs.append(stream)
                print(f"Rec added: {stream.name}")
