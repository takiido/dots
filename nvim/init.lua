vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

vim.o.number = true
vim.o.relativenumber = true
vim.o.tabstop = 4
vim.o.shiftwidth = 4
vim.o.expandtab = true
vim.o.swapfile = false

vim.g.mapleader = " "

vim.keymap.set('n', '<leader>o', ':update<CR> :source<CR>')
vim.keymap.set('n', '<leader>w', ':write<CR>')
vim.keymap.set('n', '<leader>q', ':quit<CR>')
vim.keymap.set('n', '<leader>e', ':NvimTreeToggle<CR>')
vim.keymap.set('n', '<leader>lf', vim.lsp.buf.format)
vim.keymap.set('n', '<leader>f', ':Pick files<CR>')

vim.pack.add({
	{ src = "https://github.com/loctvl842/monokai-pro.nvim" },
	{ src = "https://github.com/neovim/nvim-lspconfig" },
	{ src = "https://github.com/nvim-tree/nvim-tree.lua" },
	{ src = "https://github.com/echasnovski/mini.pick" },
	{ src = "https://github.com/MunifTanjim/nui.nvim" },
	{ src = "https://github.com/Saghen/blink.cmp" },
})

vim.lsp.enable({
	"lua_ls",
	"prettier",
})

require("nvim-tree").setup({
	view = {
		width = 30,
	},
})

require("mini.pick").setup()

require("blink.cmp").setup({
	fuzzy = {
		implementation = "lua"
	},
})

require("monokai-pro").setup({
	vim.cmd("colorscheme monokai-pro"),
})

vim.cmd("MonokaiPro ristretto")
