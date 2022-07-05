from libqtile.config import Screen

from settings.bars import main_bar

#################################################################
# SCREENS
#################################################################

main_screen = Screen(bottom=main_bar)

screens = [main_screen]
