from libqtile.config import Key
from libqtile.command import lazy

from modules.groups import groups
from modules.common import *

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

    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split(), desc='Toggle between split and unsplit sides of stack'),
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
    Key([], 'Print', lazy.spawn("scrot -e 'mv ~/*.png ~/Images/Screenshots/%Y-%m-%d-%T-screenshot.png'"), desc='Screenshot'),
    Key(['shift'], 'Print', lazy.spawn("scrot -s -e 'mv ~/*.png ~/Images/Screenshots/%Y-%m-%d-%T-screenshot.png'"), desc='Screenshot -select'),
    Key(['control'], 'Print', lazy.spawn('gnome-screenshot -i'), desc='Gnome Screenshot'),

    # Spotify Control
    Key([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause'), desc='Play or Pause Player'),
    Key([], 'XF86AudioNext', lazy.spawn('playerctl next'), desc='Skip to next'),
    Key([], 'XF86AudioPrev', lazy.spawn('playerctl previous'), desc='Skip to previous'),

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
