import QtQuick
import QtQuick.Controls
import Quickshell
import Quickshell.Hyprland
import qs.services

Row {
  spacing: 2

  Repeater {
    model: Hyprland.workspaces

    delegate: Button {
      required property var modelData
      visible: !modelData.name.startsWith("special:")

      implicitHeight: ButtonStyle.height
      leftPadding: ButtonStyle.padding
      rightPadding: ButtonStyle.padding

      flat: ButtonStyle.flat
      checkable: true
      checked: modelData.focused

      text: modelData.name
      palette {
        buttonText: checked ? ButtonStyle.textColor : ButtonStyle.dimColor;
        text: checked ? ButtonStyle.textColor : ButtonStyle.dimColor
      }
      font.pixelSize: ButtonStyle.fontSize
      font.family: ButtonStyle.fontFamily
      
      onClicked: modelData.activate()

      background: Rectangle {
        radius: ButtonStyle.borderRadius
        color: parent.hovered || parent.checked ? ButtonStyle.hoverColor : "transparent"
      }
    }
  }
}
