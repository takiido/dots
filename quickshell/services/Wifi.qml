pragma Singleton
import QtQuick
import Quickshell
import Quickshell.Io

Singleton {
  property bool connected: false

  Process {
    command: ["sh", "-c", "c=$(cat /sys/class/net/wl*/carrier 2>/dev/null); echo ${c:-0}"]
    running: true
    stdout: SplitParser {
      onRead: data => connected = data.trim() === "1"
    }
  }

  Process {
    command: ["iw", "event"]
    running: true
    stdout: SplitParser {
      onRead: data => {
        if (data.includes("connected to"))
          connected = true
        else if (data.includes("disconnected from"))
          connected = false
      }
    }
  }
}
