vim.lsp.config(
    "lua_ls",
    {}
)

vim.lsp.config(
    "pyright",
    {
        capabilities = vim.lsp.protocol.make_client_capabilities(),
    }
)

vim.lsp.config(
    "cssls",
    {
        cmd = { "css-languageserver", "--stdio" },
        capabilities = vim.lsp.protocol.make_client_capabilities(),
    }
)

vim.lsp.config(
    "jdlts",
    {}
)

vim.lsp.enable({
    "lua_ls",
    "pyright",
    "cssls",
    "jdtls",
})
