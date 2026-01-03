"""Network status widget."""

import os
import subprocess
from typing import Optional, Tuple

from gi.repository import GLib

from ...common import IconButton


def _launch_impala() -> None:
    """Launch the impala network manager."""
    subprocess.Popen(["foot", "-T", "impala", "-e", "impala"])


class Network(IconButton):
    """Network status icon with WiFi/Ethernet support.

    Left-click opens impala, right-click toggles WiFi.
    Icon shows connection type and signal strength.
    """

    WIFI_INTERFACE = "wlan0"
    POLL_INTERVAL_S = 5

    ICON_OFF = ""
    ICON_ETHERNET = ""
    ICON_DISCONNECTED = ""
    ICON_LOW = ""
    ICON_MEDIUM = ""
    ICON_HIGH = ""

    def __init__(self) -> None:
        """Initialize the network widget."""
        super().__init__(
            icon=self.ICON_OFF,
            on_click=lambda _: _launch_impala(),
            on_right_click=self._toggle_wifi,
        )

        GLib.timeout_add_seconds(self.POLL_INTERVAL_S, self._poll)
        GLib.idle_add(self._update_icon)

    def _toggle_wifi(self) -> None:
        """Toggle WiFi enabled state via rfkill."""
        try:
            result = subprocess.run(
                ["rfkill", "list", "wifi"],
                capture_output=True,
                text=True,
            )
            if "Soft blocked: yes" in result.stdout:
                subprocess.run(["rfkill", "unblock", "wifi"])
            else:
                subprocess.run(["rfkill", "block", "wifi"])
            GLib.timeout_add(500, self._update_icon)
        except Exception:
            pass

    def _poll(self) -> bool:
        """Polling callback for periodic updates."""
        self._update_icon()
        return True

    def _update_icon(self) -> bool:
        """Update icon and tooltip based on network state."""
        if self._is_ethernet_connected():
            self.update_icon(self.ICON_ETHERNET)
            self.set_tooltip_text("Ethernet connected")
        elif self._is_wifi_enabled():
            if self._is_wifi_connected():
                state, rssi, name = self._get_iwctl_info()
                strength = self._rssi_to_percent(rssi) if rssi else 0

                if strength > 75:
                    icon = self.ICON_HIGH
                elif strength > 50:
                    icon = self.ICON_MEDIUM
                else:
                    icon = self.ICON_LOW

                self.update_icon(icon)
                self.set_tooltip_text(f"{name or 'Unknown'}\n{strength}% ({rssi} dBm)")
            else:
                self.update_icon(self.ICON_DISCONNECTED)
                self.set_tooltip_text("WiFi enabled, not connected")
        else:
            self.update_icon(self.ICON_OFF)
            self.set_tooltip_text("WiFi disabled")

        return False

    def _is_wifi_enabled(self) -> bool:
        """Check if WiFi is enabled via rfkill."""
        try:
            result = subprocess.run(
                ["rfkill", "list", "wifi"],
                capture_output=True,
                text=True,
            )
            return "Soft blocked: yes" not in result.stdout
        except Exception:
            return False

    def _is_wifi_connected(self) -> bool:
        """Check if WiFi is connected."""
        state, _, _ = self._get_iwctl_info()
        return state == "connected"

    def _is_ethernet_connected(self) -> bool:
        """Check if any ethernet interface is up."""
        try:
            for iface in os.listdir("/sys/class/net"):
                if iface.startswith(("eth", "enp")):
                    path = f"/sys/class/net/{iface}/operstate"
                    if os.path.exists(path):
                        with open(path, "r") as f:
                            if f.read().strip() == "up":
                                return True
        except Exception:
            pass
        return False

    def _get_iwctl_info(self) -> Tuple[Optional[str], Optional[int], Optional[str]]:
        """Get WiFi state, RSSI, and network name from iwctl."""
        try:
            result = subprocess.run(
                ["iwctl", "station", self.WIFI_INTERFACE, "show"],
                capture_output=True,
                text=True,
            )

            state = rssi = name = None

            for line in result.stdout.splitlines():
                if "State" in line:
                    state = line.split()[-1].strip()
                elif "Connected network" in line:
                    parts = line.split("Connected network")
                    if len(parts) > 1:
                        name = parts[1].strip()
                elif "RSSI" in line and "Average" not in line:
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if "dBm" in part and i > 0:
                            rssi = int(parts[i - 1])
                            break

            return state, rssi, name
        except Exception:
            return None, None, None

    def _rssi_to_percent(self, rssi: int) -> int:
        """Convert RSSI (dBm) to percentage."""
        return max(0, min(100, 2 * (rssi + 100)))
