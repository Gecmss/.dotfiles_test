from libqtile import widget
from settings.theme import *

#################################################################
# CUSTOM FUNCTIONS
#################################################################

def separator(color):
    return widget.Sep(
        foreground=theme['foreground'],
        background=color,
        linewidth=0,
        padding=16,
    )

def left_triangle(ng_color, pg_color):
    return widget.TextBox(
        text="",
        fontsize=bar_theme['size'] + 1,
        font=fonts['powerline'],
        foreground=pg_color,
        background=ng_color,
        padding=-0.1,
    )

def right_triangle(ng_color, pg_color):
    return widget.TextBox(
        text="",
        fontsize=bar_theme['size'] + 1,
        font=fonts['powerline'],
        foreground=pg_color,
        background=ng_color,
        padding=-0.0,
    )

def set_icon(icon, group_color, mouse_callbacks={}):
    return widget.TextBox(
        text=icon,
        fontsize=icons['size'],
        foreground=theme['foreground'],
        background=group_color,
        mouse_callbacks=mouse_callbacks,
    )
