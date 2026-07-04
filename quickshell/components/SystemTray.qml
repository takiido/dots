import QtQuick
import Quickshell
import Quickshell.Widgets
import Quickshell.Services.SystemTray
import qs.services

Row {
  spacing: 4

  Repeater {
    model: SystemTray.items

    delegate: Item {
      required property var modelData
      readonly property var trayItem: modelData

      implicitWidth: 20
      implicitHeight: ButtonStyle.height

      IconImage {
        anchors.centerIn: parent
        source: trayItem.icon
        width: 16
        height: 16
      }

      MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.LeftButton | Qt.RightButton
        onClicked: mouse => {
          if (mouse.button === Qt.RightButton && trayItem.hasMenu)
            trayItem.display(Window.window, mouse.x, mouse.y)
          else
            trayItem.activate()
        }
      }
    }
  }
}
