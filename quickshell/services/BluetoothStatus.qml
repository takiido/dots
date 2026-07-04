pragma Singleton
import QtQuick
import Quickshell
import Quickshell.Io

Singleton {
  property bool powered: false
  property bool connected: false

  Process {
    command: ["sh", "-c", "bluetoothctl show 2>/dev/null | grep -q 'Powered: yes' && echo yes || echo no"]
    running: true
    stdout: SplitParser {
      onRead: data => powered = data.trim() === "yes"
    }
  }

  Process {
    command: ["sh", "-c", "bluetoothctl devices Connected 2>/dev/null | wc -l"]
    running: true
    stdout: SplitParser {
      onRead: data => connected = parseInt(data.trim()) > 0
    }
  }

  Process {
    command: ["bluetoothctl", "monitor"]
    running: true
    stdout: SplitParser {
      onRead: data => {
        if (data.includes("Powered: yes")) powered = true
        else if (data.includes("Powered: no")) powered = false
        if (data.includes("Connected: yes")) connected = true
        else if (data.includes("Connected: no")) connected = false
      }
    }
  }
}
