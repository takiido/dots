local null_ls = require("null-ls")

null_ls.setup({
  sources = {
    -- Python
    null_ls.builtins.formatting.black,

    -- JS / TS / JSON / CSS / HTML / SCSS
    null_ls.builtins.formatting.prettier,

    -- SQL
    null_ls.builtins.formatting.sqlfluff,

    -- Lua
    null_ls.builtins.formatting.stylua,
  },
})
