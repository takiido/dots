require("blink.cmp").setup({
  sources = {
    default = { "lsp", "path", "buffer" },
  },
  fuzzy = {
    implementation = "lua"
  },
  completion = {
    menu = {
      draw = {
        padding = { 1, 1 },
        columns = {
          {
            "kind_icon",
            "label",
            gap = 1
          },
          {
            "label_description",
            gap = 3
          },
          { "kind" }
        },
        treesitter = { "lsp" }
      }
    },
    ghost_text = {
      enabled = true
    },
  }
})
