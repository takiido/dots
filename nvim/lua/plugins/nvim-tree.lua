require("nvim-tree").setup({
    view = {
        width = 30,
    },
    renderer = {
        root_folder_label = function(path)
            return " " .. vim.fn.fnamemodify(path, ":t")
        end,
        indent_markers = {
            enable = true,
            inline_arrows = true,
            icons = {
                item = "├",
                bottom = "",
            },
        },
        highlight_git = "name",
        indent_width = 3,
        icons = {
            glyphs = {
                folder = {
                    arrow_closed = "",
                    arrow_open = "",
                    default = "",
                    open = "",
                    empty = "",
                    empty_open = "",
                    symlink = "",
                    symlink_open = "",
                }
            }
        }
    }
})
