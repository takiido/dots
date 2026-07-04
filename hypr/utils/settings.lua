local json = require("external/dkjson")

local function merge(defaults, data)
  if type(data) ~= "table" then return defaults end
  for k, v in pairs(data) do
    if k == "autostart" then
      defaults[k] = v
    elseif type(v) == "table" and type(defaults[k]) == "table" then
      merge(defaults[k], v)
    else
      defaults[k] = v
    end
  end
  return defaults
end

local settings = {
  border_size = 0,
  gaps_in = 0,
  gaps_out = 0,
  colors = {
    active_border = "",
    inactive_border = "",
  },
  default_apps = {
    terminal = "",
    launcher = ""
  },
  autostart = {},
  decoration = {
    rounding = 0,
    rounding_power = 0
  },
}

local file = io.open(os.getenv("HOME") .. "/.config/hypr/settings.json", "r")
if file then
  local content = file:read("*a")
  file:close()

  local data, _, err = json.decode(content)
  if data then
    merge(settings, data)
  else
    io.stderr:write("settings.json parse error: " .. tostring(err) .. "\n")
  end
end

return settings
