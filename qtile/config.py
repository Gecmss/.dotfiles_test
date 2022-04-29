# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This shit requires python-psutils, Ubuntu Mono Nerd Font and Powerline fonts
# requires scrot too

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()


############################### Custom Variables ###############################

net_device= "enp2s0"


# Fonts
default_font = "Ubuntu Mono Nerd Font"
powerline_font = "Source Code Pro for Powerline Bold"
default_font_size = 16

# Theme
fg_color = "#000000" #  "#FFFFFF"   "#000000"
bg_color = "#0A0E14"

# Bar
bar_size = 24
bar_color = "#020203"

# Group box
gborder_width = 1
icon_size = 18
hl_method = "text"
ua_method = "text"
gbg_color = "#0A0E14"
active_color = "#F1FA8C"
inactive_color = "#6272A4"
tcsb_color = "#E1AD01" # "#BD93F9"
tsb_color = "#BD93F9"
ocsb_color = "#44435A"
ub_color = "#FF5555"

# Windows Name
wtext_color = "#BD93F9"
wbg_color = "#0A0E14"


# Text groups
"""
group1_color = "#FF7F00" # Orange
group2_color = "#D600F7" # Dark Rose 
group3_color = "#007BFF" # Blue
group4_color = "#C60000" # Red
"""

group1_color = "#BD93F9"
group2_color = "#6272A4"  #F1FA8C #D600F7 #6272A4 #E1AD01 #BD93F9
group3_color = "#F1FA8C" 
group4_color = "#E1AD01" 

therm_ico = " "      # nf-fa-thermometer_2
ram_ico = "  "       # nf-fa-save
updates_ico= " "     # nf-mdi-autorenew
speed_ico=" 龍 "       # nf-mdi-speedometer
volume_ico=" "        # nf-fa-volume_up

updates_color="#BC0000" #Rojo


# Current Layout
clfg_color = "#000000"

# Functions
# Sep
def separator(color):
    return widget.Sep(
        foreground=fg_color,
        background=color,
        linewidth=0,
        padding=16,
    )


def fc_rectangle(type, color):
    if type == 0:       # nf-ple-left_half_circle_thick
        icon=""
    elif type == 1:     # nf-ple-right_half_circle_thick
        icon="" #"" ""
    else:
        icon = ""

    return widget.TextBox(
        text=icon,
        fontsize=bar_size,
        foreground=color,
        background=bg_color,
    )

def left_triangle(ng_color, pg_color):
    return widget.TextBox(
        text="",
        fontsize=bar_size+1,
        font=powerline_font,
        foreground=pg_color,
        background=ng_color,
        padding=-0.1,
    )

def right_triangle(ng_color, pg_color):
    return widget.TextBox(
        text="",
        fontsize=bar_size+1,
        font=powerline_font,
        foreground=pg_color,
        background=ng_color,
        padding=-0.1,
    )

def fc_icon(icon, group_color):
    return widget.TextBox(
        text=icon,
        fontsize=icon_size,
        foreground=fg_color,
        background=group_color,
    )
    
############################### End Custom Confs ################################

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    
    # Keys to lauch apps

    # Rofi menu
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Launch Rofi menu"),
    Key([mod, "shift"], "Tab", lazy.spawn("rofi -show"), desc="Launch Rofi window menu"),
    
    # Firefox
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    
    # Ranger
    Key([mod], "f", lazy.spawn("alacritty -e ranger"), desc="Launch Ranger file explorer"),

    # Telegram 
    Key([mod], "t", lazy.spawn("telegram-desktop"), desc="Launch Telegram"),

    # Spotify    
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch Spotify"),

    # Code    
    Key([mod], "c", lazy.spawn("code"), desc="Launch Code"),

    # Calibre    
    Key([mod, "control"], "c", lazy.spawn("calibre"), desc="Launch Calibre"),

    # Notion && Nitrogen
    Key([mod], "n", lazy.spawn("nitrogen ~/Images/Wallpapers"), desc="Launch Nitrogen"),
    Key([mod, "control"], "n", lazy.spawn("notion-app-enhanced"), desc="Launch Notion"),

    # Nvim    
    Key([mod], "v", lazy.spawn("alacritty -e nvim"), desc="Launch Nvim"),

    # QuteBrowser    
    Key([mod], "q", lazy.spawn("qutebrowser"), desc="Launch Qutebrowser"),



    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Controls
    Key([mod], "p", lazy.spawn("scrot -e 'mv ~/*.png ~/Images/Screenshots/%Y-%m-%d-%T-screenshot.png'"), desc="Screenshot"),
    Key([mod, "shift"], "p", lazy.spawn("scrot -s -e 'mv ~/*.png ~/Images/Screenshots/%Y-%m-%d-%T-screenshot.png'"), desc="Screenshot -select"),
    Key([mod, "control"], "p", lazy.spawn("gnome-screenshot -i"), desc="Gnome Screenshot"),
]


# Nerd font list
# 1. nf-linux-archlinux
# 2. nf-fa-firefox
# 3. nf-fa-terminal
# 4. nf-fa-code
# 5. nf-fa-folder_open
# 6. nf-dev-vim
# 7. nf-fae-python
# 8. nf-fae-telegram
# 9. nf-fa-spotify
# 10. nf-fa-dropbox 


groups = [Group(i) for i in [
    "  ",
    "  ",
    "  ",
    "  ",
    "  ",
    "  ",
    "  ",
    "  ",
    "  ",
    "  ", #Stuff
]]

for i, group in enumerate(groups):
    screen_number = str((i + 1)%10)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                screen_number,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                screen_number,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=1,
        margin=8,
        margin_on_single=16,
        border_focus=active_color,
        border_normal=bg_color,
        insert_position=1,
    ),
    layout.Max(),
    layout.MonadTall(
        border_focus=active_color,
        border_normal=bg_color,
        min_secondary_size=300,
        border_width=0,
    ),
    layout.Tile(
        border_focus=active_color,
        border_normal=bg_color,
        add_on_top=False,
        border_width=2,
        margin=8,
    ),
    layout.RatioTile(
        border_focus=active_color,
        border_normal=bg_color,
        border_width=1,
        fancy=True,
        margin=16,
    ),
    layout.TreeTab(
        active_bg=active_color,
        active_fg=fg_color,
        inactive_bg=inactive_color,
        inactive_fg=fg_color,
        bg_color=bg_color,
        section_fg=bg_color,
        border_width=1,
        font=powerline_font,
        panel_width=160,
        vspace=1,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=default_font,
    fontsize=default_font_size,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=active_color,
                    inactive=inactive_color,
                    borderwidth=gborder_width,
                    disable_drag=True,
                    fontsize=icon_size,
                    foreground=fg_color,
                    background=gbg_color,
                    highlight_method=hl_method,
                    margin_x=0,
                    margin_y=5,
                    padding_x=0,
                    padding_y=10,
                    this_current_screen_border=tcsb_color,
                    this_screen_border=tsb_color,
                    other_current_screen_border=ocsb_color,
                    other_screen_border=ocsb_color,
                    urgent_alert_method=ua_method,
                    urgent_border=ub_color,
                ),
                right_triangle(bar_color,gbg_color),
                separator(bar_color),
                widget.Prompt(),
                widget.WindowName(
                    foreground=wtext_color,
                    background=bar_color,
                    max_chars=32
                ),
                
                
                

                # Group one
                left_triangle(bar_color, group1_color),
                fc_icon(therm_ico, group1_color),
                widget.ThermalSensor(
                    foreground=fg_color,
                    background=group1_color,
                    threshold=50,
                    #tag_sensor="Core 0",
                    fmt= '{}'            #₁->u2081
                ),
                fc_icon(ram_ico, group1_color),
                widget.Memory(
                    foreground=fg_color,
                    background=group1_color,
                    fmt = '{}',
                    #measure_mem = "G",
                    #format = '{MemUsed:.1f}{mm}/{MemTotal:.0f}{mm}',
                    mouse_callbacks = {'Button1': lazy.spawn('alacritty -e htop')},
                ),
                widget.TextBox(
                    text="  ", # nf-oct-terminal
                    fontsize=icon_size,
                    foreground=fg_color,
                    background=group1_color,
                    mouse_callbacks={
                        "Button1": lazy.spawn("alacritty"),
                        "Button2": lazy.spawn("alacritty -e tmux"),
                        "Button3": lazy.spawn("xterm"),
                    }
                ),
                fc_icon(" ", group1_color),
                # End Group one
                
                
                # Group two
                left_triangle(group1_color, group2_color),
                widget.Clock(
                    foreground=fg_color,
                    background=group2_color,
                    format=" %d/%m/%Y %a  %I:%M %p", # nf-mdi-calendar_today nf-fa-clock_o
                ),
                #fc_icon(volume_ico, group2_color),
                #widget.PulseVolume(
                #    foreground=fg_color,
                #    background=group2_color,
                #    limit_max_volume=True,
                #    fontsize=default_font_size,
                #),
                #fc_icon(" ", group2_color),
                # End Group two


                # Group three
                #left_triangle(group2_color, group3_color),
                #fc_icon(updates_ico, group3_color),
                #widget.CheckUpdates(
                #    background=group3_color,
                #    color_have_updates=updates_color,
                #    color_no_updates=fg_color,
                #    foreground=fg_color,
                #    fontsize=default_font_size,
                #    no_update_string="0",
                #    display_format="{updates}",
                #    update_interval=3600,
                #    distro="Arch_checkupdates"
                #),
                #fc_icon(speed_ico, group3_color),
                #widget.Net(
                #    foreground=fg_color,
                #    background=group3_color,
                #    format=" {down}  {up}", #nf-fa-chevron_down  nf-fa-chevron_up
                #    interface=net_device,
                #    use_bits="true"
                #),
                #fc_icon(" ", group3_color),
                # End Group three
               

                # Group four
                left_triangle(group2_color, group4_color),
                widget.Systray(
                    icon_size=icon_size,
                    background=group4_color,
                ),
                fc_icon(" ", group4_color),
                #widget.CurrentLayoutIcon(
                #    foreground=clfg_color,
                #    background=group4_color,
                #    scale=0.75
                #),
                fc_icon(" ", group4_color), # nf-fa-window_maximize
                widget.CurrentLayout(
                    foreground=fg_color,
                    background=group4_color
                ),
                # End Group four


                # widget.Systray(icon_size=icon_size,background=bg_color,),
                # widget.Clock(format="%Y-%m-%d %A %I:%M %p"),
                # widget.QuickExit(),
                # widget.CurrentLayout(),
            ],
            bar_size,
            background=bar_color,
            #opacity=0.9,
            #border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
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
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=tcsb_color,
    border_normal=bg_color,
    border_width=2,
    margin=6,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


