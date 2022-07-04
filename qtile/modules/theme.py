# Special Colors
background=     '#0f111b'
foreground=     '#ecf0c1'
visualSel=     '#1b1c36'
cursorLine=     '#16172d'

# Base Colors
red=            '#e33400'
orange=         '#e39400'
green=          '#5ccc96'
green2=         '#67bf95'
yellow=         '#f2ce00'
purple=         '#b3a1e6'
purple2=        '#7a5ccc'
darkPurp=       '#30365F'
darkPurp2=      '#686f9a'
cyan=           '#00a3cc'
magenta=        '#ce6f8f'


# Coloration
pureWhite=      '#ffffff'
pureBlack=      '#000000'
grey=           '#818596'
grey2=          '#c1c3cc'

#####################################################################
# Theme
#####################################################################

fonts = {
    'default': 'Ubuntu Mono Nerd Font',
    'powerline': 'Source Code Pro',
    'size': 16
}

bar_theme = {
    'color': background, #020203 #060814 
    'size': 24,
    'margin': 6,
    'border_width': 0,
}

theme = {
    'foreground': pureBlack,
    'background': background,
    'active': green,
    'inactive': purple2,
    'icon_size': 18,
}

group_box = {
    'foreground': foreground,
    'background': pureBlack,
    'disable_grab': True,
    'highlight': 'text',
    'urgent': 'text',
    'urgent_color': red,
    'this_current_screen_border': orange,
    'this_screen_border': magenta,
    'other_current_screen_border': magenta,
    'other_screen_border': green,
    'border_width': 1,
}

window_name = {
    'text_color': green, #BD93F9
    'background': background, #090300
    'max_chars': 32,
}

group_colors = {
    1: magenta, #7D78DE
    2: darkPurp2,
    3: darkPurp, #82930F
    4: orange,
}

float_window = {
    'focus': green,
    'normal': background,
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
    'foreground': green,
    'background': background,
    'active': orange,
    'inactive': purple2,
}
