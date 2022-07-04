from libqtile import layout 
from modules.theme import *


layouts = [
    layout.Columns(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=1,
        margin=8,
        margin_on_single=16,
        border_focus=theme['active'],
        border_normal=theme['background'],
        insert_position=1,
    ),
    layout.Max(),
    layout.Columns(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=0,
        margin=0,
        margin_on_single=0,
        border_focus=theme['active'],
        border_normal=theme['background'],
        insert_position=1,
    ),
    layout.Tile(
        border_focus=theme['active'],
        border_normal=theme['background'],
        border_on_single=False,
        add_on_top=False,
        border_width=0,
        margin=8,
    ),
    layout.RatioTile(
        border_focus=theme['active'],
        border_normal=theme['background'],
        border_on_single=False,
        border_width=0,
        fancy=True,
        margin=16,
    ),
    layout.TreeTab(
        active_bg=theme['active'],
        active_fg=theme['foreground'],
        inactive_bg=theme['inactive'],
        inactive_fg=theme['foreground'],
        bg_color=theme['background'],
        section_fg=theme['background'],
        border_width=1,
        font=fonts['powerline'],
        panel_width=160,
        vspace=1,
    ),
]
