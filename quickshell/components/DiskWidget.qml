import QtQuick
import QtQuick.Controls
import Quickshell
import qs.services

Button {
  readonly property bool hasHome: Disk.homePct !== ""

  implicitHeight: ButtonStyle.height
  leftPadding: ButtonStyle.padding
  rightPadding: ButtonStyle.padding

  flat: ButtonStyle.flat

  text: "/ " + Disk.rootPct
  palette {
    buttonText: ButtonStyle.textColor;
    text: ButtonStyle.textColor
  }
  font.family: ButtonStyle.fontFamily
  font.pixelSize: ButtonStyle.fontSize

  onClicked: Quickshell.execDetached(
    {
      command: ["foot", "--title=disk", "diskonaut"]
    }
  )

  background: Rectangle {
    radius: ButtonStyle.borderRadius
    color: parent.hovered ? ButtonStyle.hoverColor : "transparent"
  }
}
