-- LSP capabilities (blink.cmp integration)
local capabilities = require("blink.cmp").get_lsp_capabilities()

vim.filetype.add({
  extension = {
    tsx = "typescriptreact",
    jsx = "javascriptreact",
  }
})

-- Lua
vim.lsp.config("lua_ls", {
  capabilities = capabilities,
})

-- Python
vim.lsp.config("pyright", {
  capabilities = capabilities,
})

-- TypeScript / JavaScript
vim.lsp.config("ts_ls", {
  capabilities = capabilities,
})

-- ESLint
vim.lsp.config("eslint", {
  capabilities = capabilities,
})

-- JSON
vim.lsp.config("jsonls", {
  capabilities = capabilities,
})

-- CSS / SCSS
vim.lsp.config("cssls", {
  capabilities = capabilities,
})

-- Rust
vim.lsp.config("rust_analyzer", {
  capabilities = capabilities,
})

-- SQL
vim.lsp.config("sqlls", {
  capabilities = capabilities,
})

-- Java
vim.lsp.config("jdtls", {
  capabilities = capabilities,
  root_dir = function()
    return vim.fs.dirname(
      vim.fs.find({ "pom.xml", "build.gradle", ".git" }, { upward = true })[1]
    )
  end,
})

vim.lsp.enable({
  "lua_ls",
  "pyright",
  "ts_ls",
  "eslint",
  "jsonls",
  "cssls",
  "rust_analyzer",
  "sqlls",
  "jdtls",
})
