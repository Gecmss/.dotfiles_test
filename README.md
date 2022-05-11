# .dotfiles_test

This is a test to save my dotfiles. 
Sorry if you watch this disaster.

## Dependencies

you can install dependencies running:

sudo pacman -S <dependencies> 

picom
alacritty
nerd-fonts-ubuntu-mono
scrot
python-psutils
gnome-screenshot
rofi
udiskie
nitrogen
alsamixer
pulseaudio
network-manager-applet
volumeico
nodejs
zsh
tmux
npm
noto-fonts
alsa-utils
pulseaudio-alsa


### Applications of shortcuts
firefox
ranger
spotify
notion-app-enhanced
neovim
telegram-desktop
xterm
code

## Extra necessary things (look for it in github)
- powerline-fonts 
- oh-my-zsh or oh-my-bash

## Recomendations
###sound 
if you have problems with the audio then you can put the next in your /etc/asound.conf

```
defaults.ctl.card <PCH>
defaults.pcm.card <PCH>

```
Where <PCH> is your pch sound card, you can find that out with the command

```
cat /proc/asound/cards
```




