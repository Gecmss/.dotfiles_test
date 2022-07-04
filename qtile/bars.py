from libqtile import bar, widget
from libqtile.command import lazy

from theme import *
from utils import *
from common import *

main_bar = bar.Bar(
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
    )
