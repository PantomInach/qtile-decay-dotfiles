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

import os
import subprocess
from dataclasses import dataclass

from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

if qtile.core.name == "x11":
    term = "urxvt"
elif qtile.core.name == "wayland":
    term = "foot"

# try:
#     # Configure wayland imput devices
#     from libqtile.backend.wayland import INputConfig
#     wl_input_rules = {
#         "type:keyboard": InputConfig(kb_layout=de),
#         "*": InputConfig(pointer_accel=False, pointer_accel=-0.8)
#     }
# except Exception:
#     pass
#

##########
# Colors #
##########


@dataclass
class Color:
    # Decay color schema
    bright_black = "#384148"
    bright_blue = "#8cc1ff"
    bright_cyan = "#90daff"
    bright_green = "#94f7c5"
    bright_magenta = "#e2a6ff"
    bright_red = "#fc7b81"
    bright_white = "#fafdff"
    bright_yellow = "#ffeba6"
    cursor = "#f5f5f5"
    text = "CellForeground"
    black = "#1c252c"
    blue = "#70a5eb"
    cyan = "#74bee9"
    green = "#78dba9"
    magenta = "#c68aee"
    red = "#e05f65"
    white = "#dee1e6"
    yellow = "#f1cf8a"
    background = "#101419"
    foreground = "#b6beca"


def set_floating_false(window):
    windows.floating = False


mod = "mod4"
terminal = guess_terminal()

keys = [
    # Key([mod, "shift"], "q", lazy.shutdown()),
    Key(
        [mod, "control"],
        "r",
        lazy.reload_config(),
        lazy.spawn("~/.config/qtile/scripts/autostart.sh"),
    ),
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Change layout"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
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
    # Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle previous layout"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Key(
    #     [mod],
    #     "f",
    #     lazy.window.togroup(qtile.current_group),
    #     desc="Tile floating window",
    # ),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
]

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# group_names = ["Web", "Terminal", "3", "4", "5", "6", "7", "8", "9", "Discord"]
group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_layouts = [
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
]

for i in range(len(group_names)):
    groups.append(
        Group(name=group_names[i], layout=group_layouts[i], label=group_labels[i])
    )

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Layout settings
border_width = 3
margin = 0
border_focus = Color.red
border_normal = Color.blue

# See http://docs.qtile.org/en/latest/manual/ref/layouts.html
# Floating layout is defined down below.
layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.MonadTall(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
    ),
    layout.MonadWide(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
    ),
    layout.Max(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
    ),
    layout.Matrix(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
    ),
    layout.RatioTile(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        fancy=True,
    ),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=3,
    foreground=Color.foreground,
    background=Color.background,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/.config/wallpaper/background.png",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.GroupBox(
                    block_highlight_text_color=Color.blue,
                    highlight_color=["000000", Color.bright_red],
                    highlight_method="line",
                    inactive=Color.bright_blue,
                    other_current_screen_border=Color.blue,
                    other_screen_border=Color.blue,
                    this_current_screen_border=Color.red,
                    this_screen_border=Color.red,
                    urgent_border=Color.red,
                    urgent_text=Color.red,
                    use_mouse_whell=False,
                ),
                widget.TextBox("|"),
                widget.CurrentLayout(),
                widget.TextBox("|"),
                widget.WindowName(),
                #
                widget.Spacer(),
                widget.Clock(format="%d-%m-%Y | %a | %H:%M:%S"),
                widget.Spacer(),
                #
                widget.Systray(),
                widget.TextBox("|"),
                widget.CPU(format="CPU {load_percent}%"),
                widget.TextBox("|"),
                widget.Memory(
                    measure_mem="G", format="RAM {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}"
                ),
                widget.TextBox("|"),
                widget.KeyboardLayout(configured_keyboards=["de", "us"]),
                widget.TextBox("| VOL"),
                widget.PulseVolume(),
                widget.TextBox("|"),
                widget.QuickExit(),
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        wallpaper="~/.config/wallpaper/background.png",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.GroupBox(
                    block_highlight_text_color=Color.blue,
                    highlight_color=["000000", Color.bright_red],
                    highlight_method="line",
                    inactive=Color.bright_blue,
                    other_current_screen_border=Color.blue,
                    other_screen_border=Color.blue,
                    this_current_screen_border=Color.red,
                    this_screen_border=Color.red,
                    urgent_border=Color.red,
                    urgent_text=Color.red,
                    use_mouse_whell=False,
                ),
                widget.TextBox("|"),
                widget.CurrentLayout(),
                widget.TextBox("|"),
                widget.WindowName(),
                #
                widget.Spacer(),
                widget.Clock(format="%d-%m-%Y | %a | %I:%M:%S %p"),
                widget.Spacer(),
                #
                widget.CPU(format="CPU {load_percent}%"),
                widget.TextBox("|"),
                widget.Memory(
                    measure_mem="G", format="RAM {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}"
                ),
                widget.TextBox("|"),
                widget.KeyboardLayout(configured_keyboards=["de", "us"]),
                widget.TextBox("| VOL"),
                widget.PulseVolume(),
                widget.TextBox("|"),
                widget.QuickExit(),
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=border_focus,
    border_normal=border_normal,
    border_width=border_width,
    margin=margin,
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
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~")
    try:
        subprocess.Popen([home + "/.config/qtile/scripts/autostart.sh"])
        # pass

    except Exception as e:
        with open("/tmp/qtile_error.txt", "a") as f:
            f.write("ERROR: " + str(e))


@hook.subscribe.client_new
def assigne_apps_to_group(client):
    """
    To get the name of the application use xprop.
    Now insert one of the values of WM_CLASS(String).
    """
    d = {}
    d[group_names[0]] = ["firefox", "Firefox", "Mozilla Firefox", "browser"]
    d[group_names[1]] = ["Alacritty"]
    d[group_names[2]] = ["textstudio"]
    d[group_names[3]] = []
    d[group_names[4]] = ["ipe"]
    d[group_names[5]] = ["Signal", "kdeconnect-app", "kdeconnect.app"]
    d[group_names[6]] = ["Mail", "thunderbird"]
    d[group_names[7]] = []
    d[group_names[8]] = ["Steam"]
    d[group_names[9]] = ["discord"]

    wm_class = client.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            # client.group.cmd_toscreen(toggle=False)


floating_types = ["notification", "toolbar", "splash", "dialog"]


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
