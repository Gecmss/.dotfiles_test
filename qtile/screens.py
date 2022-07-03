from libqtile.config import Screen

from bars import main_bar

main_screen = Screen(bottom=main_bar)

screens = [main_screen]
