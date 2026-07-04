local s = require("utils.settings")

hl.on("hyprland.start", function ()
  for _, cmd in ipairs(s.autostart) do
    hl.exec_cmd(cmd)
  end
end)
