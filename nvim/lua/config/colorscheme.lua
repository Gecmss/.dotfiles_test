local utils = require('utils')

local cmd = vim.cmd
local g = vim.g

utils.opt('o', 'termguicolors', true)
utils.opt('o', 'background', 'dark')

g.tokyonight_style = 'night'

-- cmd 'colorscheme gruvbox-material'
cmd 'hi normal guibg=NONE ctermbg=NONE'
