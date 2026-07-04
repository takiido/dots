import QtQuick
import QtQuick.Controls
import Quickshell
import Quickshell.Services.UPower
import qs.services

Button {
  readonly property var bat: UPower.displayDevice ?? UPower.devices?.values?.find(d => d.type === UPowerDeviceType.Battery && d.isPresent)
  readonly property real rawPct: bat?.percentage ?? -1
  readonly property bool charging: bat?.state === UPowerDeviceState.Charging || bat?.state === UPowerDeviceState.FullyCharged
  readonly property bool present: bat?.isPresent ?? false
  readonly property int pct: rawPct > 1 ? Math.round(rawPct) : Math.round(rawPct * 100)
  readonly property real rate: bat?.changeRate ?? 0

  implicitHeight: ButtonStyle.height
  leftPadding: ButtonStyle.padding
  rightPadding: ButtonStyle.padding

  flat: ButtonStyle.flat

  onClicked: Quickshell.execDetached(
    {
      command: ["foot", "--title=battery", "jolt"]
    }
  )



  contentItem: Row {
    id: row
    spacing: 2

    Text {
      text: charging ? "\ue0ba" : pct >= 75 ? "\ue0c2" : pct >= 50 ? "\ue0c6" : pct >= 25 ? "\ue0c4" : "\ue0be"
      font.family: "Phosphor"
      font.pixelSize: 13
      color: ButtonStyle.textColor
      anchors.verticalCenter: parent.verticalCenter
    }

    Text {
      text: pct + "%"
      font.family: ButtonStyle.fontFamily
      font.pixelSize: ButtonStyle.fontSize
      color: ButtonStyle.textColor
      anchors.verticalCenter: parent.verticalCenter
    }

    Text {
      text: present && Math.abs(rate) > 0.1 ? (charging ? "\ue08e" : "\ue03e") : ""
      font.family: ButtonStyle.fontFamily
      font.pixelSize: 11
      color: charging ? "#44ff44" : "#ff4444"
      anchors.verticalCenter: parent.verticalCenter
    }

    Text {
      text: present && Math.abs(rate) > 0.1 ? rate.toFixed(1) + "W" : ""
      font.family: ButtonStyle.fontFamily
      font.pixelSize: ButtonStyle.fontSize
      color: ButtonStyle.mutedColor
      anchors.verticalCenter: parent.verticalCenter
    }
  }

  background: Rectangle {
    radius: ButtonStyle.borderRadius
    color: parent.hovered ? ButtonStyle.hoverColor : "transparent"
  }
}
