if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

###########################################################
# Oh My Zsh
###########################################################

# Load OMZ
export ZSH="$HOME/.oh-my-zsh"

# Themes selection
ZSH_THEME="powerlevel10k/powerlevel10k"

# Plugins
plugins=(
	archlinux
	git
	github
	python
	pip
	virtualenv
	man
	sudo
	themes
	asdf
	zsh-autosuggestions
	zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh


###########################################################
# Custom Settings
###########################################################
export EDITOR='nvim'
export TERM=alacritty
export TERMINAL=alacritty


unsetopt autopushd
setopt append_history           # allow multiple sessions to append to one history
setopt bang_hist                # treat ! special during command expansion
setopt extended_history         # Write history in :start:elasped;command format
setopt hist_expire_dups_first   # expire duplicates first when trimming history
setopt hist_find_no_dups        # When searching history, don't repeat
setopt hist_ignore_dups         # ignore duplicate entries of previous events
setopt hist_ignore_space        # prefix command with a space to skip it's recording
setopt hist_reduce_blanks       # Remove extra blanks from each command added to history

###########################################################
# Aliases
###########################################################
alias :q='exit'
alias c='clear'
alias qtc='cd ~/.config/qtile'
alias neo='clear && neofetch'
alias trashfolder='cd ~/.local/share/Trash/files'
alias trash='rm -rf ~/.local/share/Trash/files/* ~/.local/share/Trash/info/*'
alias arch='alacritty -e htop & alacritty -e ranger & clear'
alias pose='arch && neo'
alias token='bat ~/Documents/.token'
alias pwmenu='python3 ~/.dotfiles_test/qtile/extensions/wm_power_menu.py'
alias pacman='pacman --color always'
alias yay='yay --color always'
alias pleasec='clear && please'
alias work='cd ~/Workspace'
alias rcd='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
