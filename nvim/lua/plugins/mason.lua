require("mason").setup()

require("mason-lspconfig").setup({
  ensure_installed = {
    -- JS / TS
    "ts_ls",
    "eslint",

    -- Web basics
    "cssls",
    "jsonls",

    -- Python
    "pyright",

    -- Rust
    "rust_analyzer",

    -- Java
    "jdtls",

    -- SQL
    "sqlls",

    -- Lua
    "lua_ls",
  }
})
