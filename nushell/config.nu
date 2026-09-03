$env.config.show_banner = false

try {
    fastfetch -c ~/.config/fastfetch/config-min.jsonc
} catch {
    print "fastfetch not found"
}

$env.PATH = ($env.PATH | append '/home/takiido/.cargo/bin')

source ~/.config/mise/activate.nu
