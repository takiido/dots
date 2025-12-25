$env.config.show_banner = false
try { fastfetch -c ~/.config/fastfetch/config-min.jsonc } catch { print "fastfetch not found" }
