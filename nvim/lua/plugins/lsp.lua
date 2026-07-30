-- LSP capabilities (blink.cmp integration)
local capabilities = require("blink.cmp").get_lsp_capabilities()

vim.filetype.add({
  extension = {
    tsx = "typescriptreact",
    jsx = "javascriptreact",
  }
})

-- Bash
vim.lsp.config("bashls", {
  capabilities = capabilities,
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

  settings = {
    ["rust-analyzer"] = {
      checkOnSave = true,
      cargo = {
        allFeatures = true,
      },
      rustfmt = {
        extraArgs = {},
      },
    },
  },
})

-- SQL
vim.lsp.config("sqlls", {
  capabilities = capabilities,
})

-- C / C++
vim.lsp.config("clangd", {
  capabilities = capabilities,
  cmd = {
    "clangd",
    "--background-index",
    "--clang-tidy",
    "--header-insertion=iwyu",
    "--completion-style=detailed",
  },
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
  "clangd",
})
