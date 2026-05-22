local null_ls = require("null-ls")

null_ls.setup({
  sources = {
    -- Python
    null_ls.builtins.formatting.black,

    -- JS / TS / JSON / CSS / HTML / SCSS
    null_ls.builtins.formatting.prettier,

    -- Rust
    null_ls.builtins.formatting.rustfmt,

    -- Java
    null_ls.builtins.formatting.google_java_format,

    -- SQL
    null_ls.builtins.formatting.sqlfluff,
  },
})
