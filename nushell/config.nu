$env.config = ($env.config | upsert show_banner false)

try { fastfetch } catch { print "fastfetch not found" }
