import Quickshell
import QtQuick
import qs.services

Item {
  implicitHeight: ButtonStyle.height
  implicitWidth: 60

  SystemClock {
    id: clock
    precision: SystemClock.Minutes
  }

  Text {
    anchors.centerIn: parent
    text: Qt.formatDateTime(clock.date, "hh:mm")
    color: ButtonStyle.textColor
    font.pixelSize: ButtonStyle.fontSize
    font.family: ButtonStyle.fontFamily
  }
}
