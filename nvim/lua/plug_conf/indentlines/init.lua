local g = vim.g

g.indentLine_enabled = 1

vim.cmd [[
    :noremap <F5> :IndentLinesToggle<CR>
]]
