pragma Singleton
import QtQuick
import Quickshell

Singleton {
  property int width: 30
  property int padding: 15
  property int height: 30
  property bool flat: true
  property int fontSize: 12
  property string fontFamily: "monospace"
  property color textColor: "#ffffff"
  property color dimColor: "#666666"
  property color mutedColor: "#888888"
  property color borderColor: "red"
  property int borderRadius: 6
  property color hoverColor: "#333333"
}
