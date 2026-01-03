"""Bluetooth button widget."""

import subprocess
from typing import Any

try:
    from ignis.services.bluetooth import BluetoothService
    HAS_BLUETOOTH = True
except Exception:
    HAS_BLUETOOTH = False

from ...common import IconButton


def _launch_bluetui() -> None:
    """Launch the bluetui application."""
    subprocess.Popen(["foot", "-T", "bluetui", "-e", "bluetui"])


class Bluetooth(IconButton):
    """Bluetooth status icon with toggle support.

    Left-click opens bluetui, right-click toggles Bluetooth power.
    Icon changes based on power state and connected devices.
    """

    ICON_OFF = ""
    ICON_ON = ""
    ICON_CONNECTED = ""

    def __init__(self) -> None:
        """Initialize the Bluetooth widget."""
        self._bluetooth: Any = None

        if HAS_BLUETOOTH:
            self._bluetooth = BluetoothService.get_default()

        super().__init__(
            icon=self.ICON_OFF,
            on_click=lambda _: _launch_bluetui(),
            on_right_click=self._toggle,
        )

        if HAS_BLUETOOTH and self._bluetooth:
            self._bluetooth.connect("notify::powered", self._update_icon)
            self._bluetooth.connect("notify::connected-devices", self._update_icon)
            self._update_icon()

    def _toggle(self) -> None:
        """Toggle Bluetooth power state."""
        if HAS_BLUETOOTH and self._bluetooth:
            self._bluetooth.powered = not self._bluetooth.powered

    def _update_icon(self, *args: Any) -> None:
        """Update icon and tooltip based on Bluetooth state."""
        if not HAS_BLUETOOTH or not self._bluetooth:
            self.set_tooltip_text("Bluetooth unavailable")
            return

        if not self._bluetooth.powered:
            self.update_icon(self.ICON_OFF)
            self.set_tooltip_text("Bluetooth disabled")
            return

        connected = self._bluetooth.connected_devices
        if connected:
            self.update_icon(self.ICON_CONNECTED)
            lines = []
            for device in connected:
                line = device.alias or device.name or "Unknown device"
                if hasattr(device, "battery_percentage") and device.battery_percentage > 0:
                    line += f" ({int(device.battery_percentage)}%)"
                lines.append(line)
            self.set_tooltip_text("\n".join(lines))
        else:
            self.update_icon(self.ICON_ON)
            self.set_tooltip_text("Bluetooth on, no devices")
