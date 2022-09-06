local g = vim.g

g.neovide_transparency = 0.7
g.neovide_cursor_vfx_mode = 'pixiedust'
g.neovide_cursor_trail_lenght = 0.8
g.neovide_cursor_vfx_opacity = 200
g.neovide_cursor_vfx_particle_life = 1.7
g.neovide_cursor_vfx_particle_density = 9.0

vim.cmd [[
    if exists('g:neovide')
        syntax enable
        colorscheme spaceduck
        set background=dark
        set termguicolors
        let g:airline_theme='spaceduck'
        set guifont=UbuntuMono\ Nerd\ Font:h12
    endif
]]
