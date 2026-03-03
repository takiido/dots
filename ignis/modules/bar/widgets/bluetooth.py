"""Bluetooth button widget."""

import subprocess
from typing import Any

from gi.repository import Gio, GLib

from ...common import IconButton


def _launch_bluetui() -> None:
    """Launch the bluetui application."""
    subprocess.Popen(["foot", "-T", "bluetui", "-e", "bluetui"])


class Bluetooth(IconButton):
    """Bluetooth status icon with toggle support.

    Left-click opens bluetui, right-click toggles Bluetooth power.
    Icon changes based on power state and connected devices.
    Uses BlueZ directly via DBus (no gnome-bluetooth required).
    """

    ICON_OFF = ""
    ICON_ON = ""
    ICON_CONNECTED = ""

    BLUEZ_SERVICE = "org.bluez"
    BLUEZ_ADAPTER_IFACE = "org.bluez.Adapter1"
    BLUEZ_DEVICE_IFACE = "org.bluez.Device1"
    DBUS_PROPS_IFACE = "org.freedesktop.DBus.Properties"
    OBJECT_MANAGER_IFACE = "org.freedesktop.DBus.ObjectManager"

    def __init__(self) -> None:
        """Initialize the Bluetooth widget."""
        self._adapter_path: str | None = None
        self._bus = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)

        super().__init__(
            icon=self.ICON_OFF,
            on_click=lambda _: _launch_bluetui(),
            on_right_click=self._toggle,
        )

        self._setup_bluez()

    def _setup_bluez(self) -> None:
        """Find the default adapter and subscribe to DBus signals."""
        try:
            result = self._bus.call_sync(
                self.BLUEZ_SERVICE,
                "/",
                self.OBJECT_MANAGER_IFACE,
                "GetManagedObjects",
                None, None,
                Gio.DBusCallFlags.NONE,
                -1, None,
            )
            objects = result.unpack()[0]

            for path, interfaces in objects.items():
                if self.BLUEZ_ADAPTER_IFACE in interfaces:
                    self._adapter_path = path
                    break

        except GLib.Error:
            self.set_tooltip_text("Bluetooth unavailable")
            return

        if not self._adapter_path:
            self.set_tooltip_text("No Bluetooth adapter found")
            return

        # Watch for property changes on any BlueZ object (adapter + devices)
        self._bus.signal_subscribe(
            self.BLUEZ_SERVICE,
            self.DBUS_PROPS_IFACE,
            "PropertiesChanged",
            None,  # any object path
            None, Gio.DBusSignalFlags.NONE,
            self._on_properties_changed,
            None,
        )

        # Watch for new/removed objects (device connect/disconnect events)
        self._bus.signal_subscribe(
            self.BLUEZ_SERVICE,
            self.OBJECT_MANAGER_IFACE,
            "InterfacesAdded",
            None,
            None, Gio.DBusSignalFlags.NONE,
            lambda *a: self._update_icon(),
            None,
        )
        self._bus.signal_subscribe(
            self.BLUEZ_SERVICE,
            self.OBJECT_MANAGER_IFACE,
            "InterfacesRemoved",
            None,
            None, Gio.DBusSignalFlags.NONE,
            lambda *a: self._update_icon(),
            None,
        )

        self._update_icon()

    def _on_properties_changed(
        self,
        connection: Any,
        sender: Any,
        path: Any,
        iface: Any,
        signal: Any,
        params: Any,
        user_data: Any,
    ) -> None:
        """Handle DBus PropertiesChanged signal."""
        changed_iface = params.unpack()[0]
        if changed_iface in (self.BLUEZ_ADAPTER_IFACE, self.BLUEZ_DEVICE_IFACE):
            self._update_icon()

    def _get_adapter_powered(self) -> bool:
        """Return whether the default adapter is powered."""
        try:
            result = self._bus.call_sync(
                self.BLUEZ_SERVICE,
                self._adapter_path,
                self.DBUS_PROPS_IFACE,
                "Get",
                GLib.Variant("(ss)", (self.BLUEZ_ADAPTER_IFACE, "Powered")),
                None,
                Gio.DBusCallFlags.NONE,
                -1, None,
            )
            return result.unpack()[0]
        except GLib.Error:
            return False

    def _get_connected_devices(self) -> list[dict]:
        """Return a list of dicts with name/battery info for connected devices."""
        try:
            result = self._bus.call_sync(
                self.BLUEZ_SERVICE,
                "/",
                self.OBJECT_MANAGER_IFACE,
                "GetManagedObjects",
                None, None,
                Gio.DBusCallFlags.NONE,
                -1, None,
            )
            objects = result.unpack()[0]
        except GLib.Error:
            return []

        devices = []
        for path, interfaces in objects.items():
            if self.BLUEZ_DEVICE_IFACE not in interfaces:
                continue
            props = interfaces[self.BLUEZ_DEVICE_IFACE]
            if not props.get("Connected", False):
                continue
            name = props.get("Alias") or props.get("Name") or "Unknown device"
            battery = None
            # Battery percentage via org.bluez.Battery1 if present
            if "org.bluez.Battery1" in interfaces:
                battery = interfaces["org.bluez.Battery1"].get("Percentage")
            devices.append({"name": name, "battery": battery})

        return devices

    def _toggle(self, *args: Any) -> None:
        """Toggle Bluetooth power state."""
        if not self._adapter_path:
            return
        try:
            powered = self._get_adapter_powered()
            self._bus.call_sync(
                self.BLUEZ_SERVICE,
                self._adapter_path,
                self.DBUS_PROPS_IFACE,
                "Set",
                GLib.Variant(
                    "(ssv)",
                    (self.BLUEZ_ADAPTER_IFACE, "Powered", GLib.Variant("b", not powered)),
                ),
                None,
                Gio.DBusCallFlags.NONE,
                -1, None,
            )
        except GLib.Error:
            pass

    def _update_icon(self, *args: Any) -> None:
        """Update icon and tooltip based on Bluetooth state."""
        if not self._adapter_path:
            self.set_tooltip_text("Bluetooth unavailable")
            return

        if not self._get_adapter_powered():
            self.update_icon(self.ICON_OFF)
            self.set_tooltip_text("Bluetooth disabled")
            return

        connected = self._get_connected_devices()
        if connected:
            self.update_icon(self.ICON_CONNECTED)
            lines = []
            for device in connected:
                line = device["name"]
                if device["battery"] is not None:
                    line += f" ({device['battery']}%)"
                lines.append(line)
            self.set_tooltip_text("\n".join(lines))
        else:
            self.update_icon(self.ICON_ON)
            self.set_tooltip_text("Bluetooth on, no devices")
