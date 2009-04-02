set nocompatible
filetype on
filetype indent on
filetype plugin on
let python_highlight_all=1
highlight BadWhitespace ctermbg=red guibg=red
syntax on
set bg=dark
colorscheme slate

" folds saves when leaving a file
au BufWinLeave * silent! mkview
au BufRead * silent loadview

set tabstop=4
set softtabstop=4
set shiftwidth=4
set smartindent
set backspace=indent,eol,start "backspace across lines
set incsearch
set ruler " line numbers
set wildmenu " TEST: auto complete?
set clipboard+=unnamed " TEST: windows clipboard?
match BadWhitespace /\s\+$/ " show extra stuff
set laststatus=2
set statusline=%-(%f%m%)%=\ %(0x%B\(%b\)\ %(%l:%c/%L\(%p%%\)%)\ %n%)%(%h%r%y%)
hi StatusLine ctermbg=7 ctermfg=0 gui=undercurl guisp=Yellow
hi ModeMsg ctermbg=1 ctermfg=3
