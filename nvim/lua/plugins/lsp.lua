vim.lsp.enable({
    "lua_ls",
    "pyright",
    "cssls",
})

local lspconfig = require("lspconfig")

lspconfig.lua_ls.setup({})
lspconfig.pyright.setup({})
lspconfig.cssls.setup({})
