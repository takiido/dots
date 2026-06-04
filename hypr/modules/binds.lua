local apps = require("modules/default_apps")

local mainMod = "SUPER"

hl.bind(
    mainMod .. " + M",
    hl.dsp.exec_cmd("command -v hyprshutdown >/dev/null 2>&1 && hyprshutdown || hyprctl dispatch 'hl.dsp.exit()'")
)

hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag())
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize())

hl.bind(mainMod .. " + Return", hl.dsp.exec_cmd(apps.terminal))

hl.bind(mainMod .. " + Q", hl.dsp.window.close())
hl.bind(mainMod .. " + F", hl.dsp.window.float({toggle}))
hl.bind(mainMod .. " + S", hl.dsp.workspace.toggle_special("magic"))
hl.bind(mainMod .. " + SHIFT + S", hl.dsp.window.move({ workspace = "special:magic" }))
for i = 0, 9 do
    hl.bind(mainMod .. " + " .. i, hl.dsp.focus({ workspace =  i}))
    hl.bind(mainMod .. " + SHIFT + " .. i, hl.dsp.window.move({ workspace =  i}))
end


hl.bind("Print", hl.dsp.exec_cmd('grim -g "$(slurp)"'))
hl.bind("SHIFT + Print", hl.dsp.exec_cmd('grim -g "$(slurp -d)" - | wl-copy'))
