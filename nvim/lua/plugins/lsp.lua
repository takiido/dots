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


vim.lsp.config("java_language_server", {
    cmd = { "/path/to/lang_server_linux.sh" },
    root_dir = vim.fs.dirname(vim.fs.find({ 'pom.xml', 'build.gradle', '.git' }, { upward = true })[1]),
})


vim.lsp.enable({
    "lua_ls",
    "pyright",
    "cssls",
    "java_language_server",
})
