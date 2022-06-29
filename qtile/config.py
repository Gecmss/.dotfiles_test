import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = 'mod4'
net_device= 'enp2s0'
terminal = 'alacritty'

# This shit requires python-psutils, Ubuntu Mono Nerd Font and Powerline fonts
# requires scrot too



#################################################################
# CUSTOM COLORS, ICONS AND THEMES
#################################################################

# COLORS ########################################################    
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

#################################################################

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


#################################################################
# KEYBINDINGS
#################################################################

keys = [
    # Focus
    Key([mod], 'h', lazy.layout.left(), desc='Move focus to left'),
    Key([mod], 'l', lazy.layout.right(), desc='Move focus to right'),
    Key([mod], 'j', lazy.layout.down(), desc='Move focus down'),
    Key([mod], 'k', lazy.layout.up(), desc='Move focus up'),

    Key([mod], 'space', lazy.layout.next(), desc='Move window focus to other window'),
    # Move

    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left(), desc='Move window to the left'),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right(), desc='Move window to the right'),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down(), desc='Move window down'),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(), desc='Move window up'),

    # Grow
    Key([mod, 'control'], 'h', lazy.layout.grow_left(), desc='Grow window to the left'),
    Key([mod, 'control'], 'l', lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod, 'control'], 'j', lazy.layout.grow_down(), desc='Grow window down'),
    Key([mod, 'control'], 'k', lazy.layout.grow_up(), desc='Grow window up'),
    Key([mod], 'n', lazy.layout.normalize(), desc='Reset all window sizes'),

    Key(
        [mod, 'shift'],
        'Return',
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack',
    ),
    Key([mod], 'Return', lazy.spawn(terminal), desc='Launch terminal'),

    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod, 'control'], 'Tab', lazy.prev_layout(), desc='Toggle between layouts'),
    Key(['mod1'], 'f', lazy.window.toggle_floating(), desc='Toggle between layouts'),

    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),
    Key([mod, 'control'], 'r', lazy.reload_config(), desc='Reload the config'),
    Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),
    Key([mod], 'r', lazy.spawncmd(), desc='Spawn a command using a prompt widget'),
    


    # Controls
    Key([mod], 'p', lazy.spawn("scrot -e 'mv ~/*.png ~/Images/Screenshots/%Y-%m-%d-%T-screenshot.png'"), desc='Screenshot'),
    Key([mod, 'shift'], 'p', lazy.spawn("scrot -s -e 'mv ~/*.png ~/Images/Screenshots/%Y-%m-%d-%T-screenshot.png'"), desc='Screenshot -select'),
    Key([mod, 'control'], 'p', lazy.spawn('gnome-screenshot -i'), desc='Gnome Screenshot'),

    # Spotify Control
    Key([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause'), desc='Play or Pause Player'),
    Key([], 'XF86AudioNext', lazy.spawn('playerctl next'), desc='Skip to next'),
    Key([], 'XF86AudioPrev', lazy.spawn('playerctl previous'), desc='Skip to previous'),

    #Power Menu
    # Key([mod], 'z', lazy.spawn("python3 ~/.dotfiles_test/qtile/extensions/wm_power_menu.py"), desc='Lauch Power Menu'),
    

    # Keys to lauch apps

    # Rofi menu
    Key([mod], 'm', lazy.spawn('rofi -show drun'), desc='Launch Rofi menu'),
    Key(['mod1'], 'Tab', lazy.spawn('rofi -show'), desc='Launch Rofi window menu'),
    
    # Firefox
    Key([mod], 'b', lazy.spawn('firefox'), desc='Launch firefox'),
    
    # Ranger
    Key([mod], 'f', lazy.spawn(terminal + ' --title Ranger -e ranger'), desc='Launch Ranger file explorer'),

    # Telegram 
    Key([mod], 't', lazy.spawn('telegram-desktop'), desc='Launch Telegram'),

    # Email
    Key([mod], 'e', lazy.spawn('thunderbird'), desc='Launch Thunderbird'),

    # Spotify    
    Key([mod], 's', lazy.spawn('spotify'), desc='Launch Spotify'),

    # Steam    
    Key([mod, 'control'], 's', lazy.spawn('flatpak run com.valvesoftware.Steam'), desc='Launch Steam'),

    # Code    
    Key([mod], 'c', lazy.spawn('code'), desc='Launch Code'),

    # Calibre    
    Key([mod, 'control'], 'c', lazy.spawn('calibre'), desc='Launch Calibre'),

    # Notion
    Key([mod, 'control'], "n", lazy.spawn('notion-app-enhanced'), desc='Launch Notion'),

    # NeoVide
    Key([mod], 'v', lazy.spawn('neovide'), desc='Launch Neovide'),
    
    # Nvim    
    Key([mod, 'control'], 'v', lazy.spawn(terminal + ' --title Nvim -e nvim'), desc='Launch Nvim'),

    # QuteBrowser    
    Key([mod], 'q', lazy.spawn('qutebrowser'), desc='Launch Qutebrowser'),
]


#################################################################
# GROUPS
#################################################################

# Nerd font list 
# 1. nf-linux-archlinux 
# 2. nf-fa-firefox 
# 3. nf-fa-terminal 
# 4. nf-fa-code 
# 5. nf-fa-folder_open 
# 6. nf-dev-vim 
# 7. nf-fae-python    nf-fa-steam_square 
# 8. nf-fae-telegram 
# 9. nf-fa-spotify 
# 10. nf-fa-dropbox 

groups = [
    Group('  '),
    Group('  '),
    Group('  '),
    Group('  '),
    Group('  '),
    Group('  '),
    Group('  '),
    Group('  '),
    Group('  ', matches=[Match(wm_class='spotify')]),
    Group('  '),
]

for i, group in enumerate(groups):
    screen_number = str((i + 1)%10)
    keys.extend(
        [
            Key(
                [mod],
                screen_number,
                lazy.group[group.name].toscreen(),
                desc='Switch to group {}'.format(group.name),
            ),

            Key(
                [mod, 'shift'],
                screen_number,
                lazy.window.togroup(group.name, switch_group=True),
                desc='Switch to & move focused window to group {}'.format(group.name),
            ),

            Key(
                [mod, 'control'],
                screen_number,
                lazy.window.togroup(group.name),
                desc='move focused window to group {}'.format(group.name)
            ),
        ]
    )

#################################################################
# DropDowns
#################################################################

groups.extend([
    ScratchPad('scratch',
               [
                   DropDown(
                       'term',
                       'alacritty',
                       opacity=1,
                       height=0.5,
                       width=0.5,
                       x=0.25,
                       y=0,

                   ),
                   DropDown(
                       'spot',
                       'spotify',
                       opacity=1,
                       height=0.75,
                       width=0.5,
                       x=0.25,
                       y=0,

                   ),
               ]
    )
])

keys.extend(
    [
        Key([], 'F2', lazy.group['scratch'].dropdown_toggle('term')),
        Key([], 'F10', lazy.group['scratch'].dropdown_toggle('spot')),
    ]
)

#################################################################
# LAYOUTS
#################################################################

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

#################################################################
# SCREENS
#################################################################

widget_defaults = dict(
    font=fonts['default'],
    fontsize=fonts['size'],
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    active=theme['active'],
                    inactive=theme['inactive'],
                    borderwidth=group_box['border_width'],
                    disable_drag=group_box['disable_grab'],
                    fontsize=theme['icon_size'],
                    foreground=group_box['foreground'],
                    background=group_box['background'],
                    highlight_method=group_box['highlight'],
                    margin_x=0,
                    margin_y=3,
                    padding_x=0,
                    padding_y=10,
                    this_current_screen_border=group_box['this_current_screen_border'],
                    this_screen_border=group_box['this_screen_border'],
                    other_current_screen_border=group_box['other_current_screen_border'],
                    other_screen_border=group_box['other_screen_border'],
                    urgent_alert_method=group_box['urgent'],
                    urgent_border=group_box['urgent_color'],
                ),
                right_triangle(bar_theme['color'], group_box['background']),
                separator(bar_theme['color']),
                widget.Prompt(
                    foreground=layout_theme['foreground']
                ),
                widget.WindowName(
                    foreground=window_name['text_color'],
                    background=window_name['background'],
                    max_chars=window_name['max_chars']
                ),

                widget.Systray(
                    icon_size=icons['size'],
                    background=bar_theme['color'],
                ),
                separator(bar_theme['color']),

                # Group one
                left_triangle(bar_theme['color'], group_colors[1]),
                set_icon(icons['therm'], group_colors[1]),
                widget.ThermalSensor(
                    foreground=theme['foreground'],
                    background=group_colors[1],
                    threshold=50,
                    fmt= '{}'
                ),
                set_icon(icons['ram'],
                         group_colors[1],
                         mouse_callbacks = {
                             'Button1': lazy.spawn(terminal + ' --title System -e htop'),
                             'Button3': lazy.spawn(terminal + ' --title System -e btop')
                         },
                         ),
                widget.Memory(
                    foreground=theme['foreground'],
                    background=group_colors[1],
                    fmt = '{}',
                    measure_mem = 'M', #'G', 'M'
                    #format = '{MemUsed:.1f}{mm}/{MemTotal:.0f}{mm}',
                    mouse_callbacks = {
                        'Button1': lazy.spawn(terminal + ' --title System -e htop'),
                        'Button3': lazy.spawn(terminal + ' --title System -e btop')
                },
                ),
                widget.TextBox(
                    text='  ', # nf-oct-terminal
                    fontsize=icons['size'],
                    foreground=theme['foreground'],
                    background=group_colors[1],
                    mouse_callbacks={
                        'Button1': lazy.spawn(terminal),
                        'Button2': lazy.spawn(terminal + ' -e tmux'),
                        'Button3': lazy.spawn('xterm'),
                    }
                ),
                set_icon(' ', group_colors[1]),
                # End Group one

                # Group two
                left_triangle(group_colors[1], group_colors[2]),
                set_icon(" ", group_colors[2]),
                widget.Pomodoro(
                    background=group_colors[2],
                    color_inactive=theme['foreground'],
                    color_break=group_box['this_current_screen_border'],
                    color_active=theme['active'],
                    fontsize=theme['icon_size'],
                    prefix_inactive=' ',
                    prefix_active=' ',
                    prefix_paused=' P',
                    prefix_break=' ',
                    prefix_long_break=' ',
                ),
                set_icon(" ", group_colors[2]),
                widget.Clock(
                    foreground=theme['foreground'],
                    background=group_colors[2],
                    format=' %d/%m/%Y %a  %H:%M %p', # nf-mdi-calendar_today nf-fa-clock_o  ... %H is for 24 format %I is 12 hour format 
                    mouse_callbacks={
                        'Button1': lazy.spawn('gsimplecal'),
                        'Button3': lazy.spawn(terminal + ' --title Calendar -e khal interactive'),
                    },
                ),
                #set_icon(icons['volume'], group_colors[2]),
                #widget.PulseVolume(
                #    foreground=theme['foreground'],
                #    background=group_colors[2],
                #    limit_max_volume=True,
                #    fontsize=fonts['size'],
                #),
                set_icon(" ", group_colors[2]),
                # End Group two


                # Group three
                left_triangle(group_colors[2], group_colors[3]),
                set_icon(' ', group_colors[3]),
                set_icon(' ', group_colors[3]), # nf-fa-window_maximize
                widget.CurrentLayout(
                    foreground=theme['foreground'],
                    background=group_colors[3]
                ),
                set_icon(' ', group_colors[3]),
                # End Group three
            ],
            bar_theme['size'],
            background=bar_theme['color'],
            #margin=bar_theme['margin'],
            border_width=bar_theme['border_width'],
            border_color=bar_theme['color'],
        ),
    ),
]


#################################################################
# FLOATING LAYOUT
#################################################################

mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],
    border_focus=float_window['focus'],
    border_normal=float_window['normal'],
    border_width=float_window['border_width'],
    margin=float_window['margin'],
)
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"

#################################################################
# HOOKS
#################################################################

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.client_new
def client_new(client):
    if client.name == 'Spotify':
        client.togroup(9)#('  ')
