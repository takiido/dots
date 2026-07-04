import QtQuick
import QtQuick.Controls
import Quickshell
import Quickshell.Io
import qs.services

Button {
  implicitHeight: ButtonStyle.height
  leftPadding: ButtonStyle.padding
  rightPadding: ButtonStyle.padding

  flat: ButtonStyle.flat

  text: BluetoothStatus.connected ? "\ue0dc" 
          : BluetoothStatus.powered ? "\ue0da" 
          : "\ue0de"
  palette {
    buttonText: ButtonStyle.textColor;
    text: ButtonStyle.textColor
  }
  font.pixelSize: ButtonStyle.fontSize
  font.family: "Phosphor"

  onClicked: Quickshell.execDetached(
    {
      command: ["foot", "--title=bluetooth", "bluetui"]
    }
  )

  background: Rectangle {
    radius: ButtonStyle.borderRadius
    color: parent.hovered ? ButtonStyle.hoverColor : "transparent"
  }
}
