import Quickshell
import QtQuick
import QtQuick.Controls
import Quickshell.Io
import Quickshell.Services.UPower
import qs.components
import qs.services

PanelWindow {
  required property var modelData
  screen: modelData

  anchors { top: true; left: true; right: true }
  implicitHeight: 30
  color: "#000000"

  Row {
    anchors { left: parent.left; verticalCenter: parent.verticalCenter; leftMargin: 8 }
    spacing: 8
    Workspaces {}
  }

  Button {
    anchors.centerIn: parent
    implicitHeight: ButtonStyle.height
    leftPadding: ButtonStyle.padding
    rightPadding: ButtonStyle.padding
    
    text: "\u{1D593}\u{1D58E}\u{1D58D}\u{1D58E}\u{1D591}"
    font.pixelSize: ButtonStyle.fontSize
    palette {
      buttonText: ButtonStyle.textColor;
      text: ButtonStyle.textColor
    }

    onClicked: Quickshell.execDetached(
      {
        command: ["vicinae", "toggle"]
      }
    )


    background: Rectangle {
      radius: ButtonStyle.borderRadius
      color: parent.hovered ? ButtonStyle.hoverColor : "transparent"
    }
  }

  Row {
    anchors { right: parent.right; verticalCenter: parent.verticalCenter; rightMargin: 8 }
    spacing: 2
    BatteryWidget {}
    DiskWidget {}
    SystemTray {}
    WifiButton {}
    BluetoothButton {}
    TimeWidget {}
  }
}
