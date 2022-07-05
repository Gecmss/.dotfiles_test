from settings.colorscheme import palette

#####################################################################
# THEMES
#####################################################################

fonts = {
    'default': 'Ubuntu Mono Nerd Font',
    'powerline': 'Source Code Pro',
    'size': 16
}

bar_theme = {
    'color': palette["background"],
    'size': 24,
    'margin': 6,
    'border_width': 0,
}

theme = {
    'foreground': palette["black"],
    'background': palette["background"],
    'active': palette[4],
    'inactive': palette[1],
    'icon_size': 18,
}

group_box = {
    'foreground': palette["foreground"],
    'background': palette["black"],
    'disable_grab': True,
    'highlight': 'text',
    'urgent': 'text',
    'urgent_color': palette[10],
    'this_current_screen_border': palette[9],
    'this_screen_border': palette[7],
    'other_current_screen_border': palette[7],
    'other_screen_border': palette[4],
    'border_width': 2,
}

window_name = {
    'text_color': palette[4], #BD93F9
    'background': palette["background"], #090300
    'max_chars': 32,
}

group_colors = {
    1: palette[7], #7D78DE
    2: palette[3],
    3: palette[2], #82930F
    4: palette[9],
}

float_window = {
    'focus': palette[9],
    'normal': palette["background"],
    'border_width': 2,
    'margin': 6
}

icons = {
    'size': 18,
    'therm': ' ',
    'ram': '  ',
    'updates': ' ',
    'speed': ' 龍 ',
    'volume': ' ',
}

layout_theme = {
    'foreground': palette["foreground"],
    'background': palette["background"],
    'active': palette[9],
    'inactive': palette[1],
}
