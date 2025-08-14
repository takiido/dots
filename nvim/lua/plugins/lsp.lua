vim.lsp.enable({
    "lua_ls",
    "prettier",
    "pyright",
})

local lspconfig = require("lspconfig")

lspconfig.lua_ls.setup({})
lspconfig.pyright.setup({})
