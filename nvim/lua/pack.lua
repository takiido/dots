vim.pack.add({
  -- Theme
  { src = "https://github.com/bluz71/vim-moonfly-colors", name = "moonfly" },

  -- Syntax highlighting
  { src = "https://github.com/nvim-treesitter/nvim-treesitter" },

  -- File explorer & icons
  { src = "https://github.com/nvim-tree/nvim-tree.lua" },
  { src = "https://github.com/nvim-tree/nvim-web-devicons" },

  -- UI Components
  { src = "https://github.com/romgrk/barbar.nvim" },

  -- LSP
  { src = "https://github.com/neovim/nvim-lspconfig" },
  { src = "https://github.com/mason-org/mason.nvim" },
  { src = "https://github.com/mason-org/mason-lspconfig.nvim" },

  -- Completion
  { src = "https://github.com/Saghen/blink.cmp" },

  -- Diagnostics / formatting
  { src = "https://github.com/nvimtools/none-ls.nvim" },
  { src = "https://github.com/nvim-lua/plenary.nvim" },

  -- University (Java)
  {
    src = 'https://github.com/JavaHello/spring-boot.nvim',
    version = '218c0c26c14d99feca778e4d13f5ec3e8b1b60f0',
  },
  'https://github.com/MunifTanjim/nui.nvim',
  'https://github.com/mfussenegger/nvim-dap',

  'https://github.com/nvim-java/nvim-java',
})
