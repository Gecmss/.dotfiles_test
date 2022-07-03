import os
import subprocess
from libqtile import layout, hook
from libqtile.config import Click, Drag, DropDown, Key, Match, ScratchPad
from libqtile.lazy import lazy

# This shit requires python-psutils, Ubuntu Mono Nerd Font and Powerline fonts
# requires scrot too

from keys import keys
from groups import groups
from common import *
from layouts import layouts
from screens import screens
from theme import float_window

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
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

#################################################################
# HOOKS
#################################################################

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
