local utils = require('utils')

local cmd = vim.cmd
utils.opt('o', 'termguicolors', true)
utils.opt('o', 'background', 'dark')

vim.api.nvim_command([[
    augroup ChangeBackgroudColour
        autocmd colorscheme * :hi normal guibg=#0a0a0a cterm=NONE
    augroup END
]])


-- cmd 'colorscheme gruvbox-material'
cmd 'hi normal guibg=NONE ctermbg=NONE'
