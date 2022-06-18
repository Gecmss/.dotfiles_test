let g:airline#extensions#ale#enabled = 1

highlight ALEError guibg=#434343 guisp=White
highlight ALEInfo guibg=#434343 guisp=White
highlight ALEWarning guibg=#434343 guisp=White
highlight ALEErrorLine guibg=#434343 gui=bold
highlight ALEInfoLine guibg=#434343 gui=bold
highlight ALEWarningLine guibg=#434343 gui=bold

" Use system flake8
"let g:ale_python_flake8_executable = '/usr/bin/flake8'
let g:ale_linters = {
\   'python': ['flake8'],
\   'sh': ['shellcheck'],
\}
