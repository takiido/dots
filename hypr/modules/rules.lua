hl.window_rule({
  name = "tui_settings",
  match = {
    title = "bluetooth||network||battery||disk"
  },
  float = true,
  center = true,
  pin = true,
  stay_focused = true,
  dim_around = true,
  size = {"(monitor_w*0.5)", "(monitor_h*0.7)"}
})
