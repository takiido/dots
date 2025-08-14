require("nvim-treesitter.configs").setup({
    ensure_installed = {
        "css",
        "dockerfile",
        "html",
        "javascript",
        "lua",
        "markdown",
        "python",
        "rust",
        "scss",
        "sql",
        "tsx",
        "typescript",
    },
    highlight = {
        enabled = true,
        additional_vim_regex_highlighting = false,
    },
    indent = {
        enabled = true,
    },
    rainbow = {
        enabled = true,
        extended_mode = true,
        max_file_lines = nil,
    },
})
