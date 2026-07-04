pragma Singleton
import QtQuick
import Quickshell
import Quickshell.Io

Singleton {
  property string rootPct: ""
  property string homePct: ""

  Process {
    id: proc
    command: ["sh", "-c", "df -h --output=pcent,target / /home 2>/dev/null | tail -n +2"]
    running: true
    stdout: SplitParser {
      onRead: data => {
        var parts = data.trim().split(/\s+/)
        if (parts.length >= 2) {
          if (parts[1] === "/") rootPct = parts[0]
          else if (parts[1] === "/home") homePct = parts[0]
        }
      }
    }
  }

  Timer {
    interval: 30000
    running: true
    repeat: true
    onTriggered: {
      var c = proc.command
      proc.command = []
      proc.command = c
    }
  }
}
