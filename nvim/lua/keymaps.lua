local utils = require('utils')

local map = utils.map

map('n', '<C-l>', '<cmd>noh<CR>') -- Clear highlights
-- map('i', 'ii', '<Esc>')           -- ii to escape

-- Term maps
map('n', '<F9>', '<cmd>10sp term://zsh<CR>')
map('n', '<Leader>vt', '<cmd>vsplit term://zsh<CR>')

-- Auto complete Parenthesis and more
map('i', '(', '()<Esc>ha')
map('i', '{', '{}<Esc>ha')
map('i', '[', '[]<Esc>ha')

