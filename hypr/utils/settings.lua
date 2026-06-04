local json = require("external/dkjson")

local file = io.open(".config/hypr/consts/settings.json", "r")

local settings = {
  border_size = 0,
  gaps_in = 4,
  gaps_out = 16,

  colors = {
    active_border = "",
    inactive_border = "",
  }
}

if file then
  local content = file:read("*a")
  local table = json.decode(content)

  settings.border_size = table.border_size
  settings.gaps_in = table.gaps_in
  settings.gaps_out = table.gaps_out
  settings.colors.active_border = table.colors.active_border
  settings.colors.inactive_border = table.colors.inactive_border
end

return settings
