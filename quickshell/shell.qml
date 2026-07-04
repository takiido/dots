//@ pragma ShellId nihil
import Quickshell
import qs.modules.bar

ShellRoot {
  Variants {
    model: Quickshell.screens
    Bar { screen: modelData }
  }
}
