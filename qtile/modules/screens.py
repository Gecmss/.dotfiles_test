from libqtile.config import Screen

from modules.bars import main_bar

main_screen = Screen(bottom=main_bar)

screens = [main_screen]
