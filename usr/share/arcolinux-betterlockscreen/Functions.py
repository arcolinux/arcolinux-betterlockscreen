# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import os
import subprocess
from gi.repository import GLib
from os.path import expanduser

home = expanduser("~")
base_dir = os.path.dirname(os.path.realpath(__file__))
config = home + "/.config/arcolinux-betterlockscreen/"
settings = "settings.conf"
# ================================================
#                   GLOBALS
# ================================================

# ================================================
#               NOTIFICATIONS
# ================================================


def _get_position(lists, string):
    nlist = [x for x in lists if string in x]
    position = lists.index(nlist[0])
    return position


def get_saved_path():
    with open(config + settings, "r") as f:
        lines = f.readlines()
        f.close()
    pos = _get_position(lines, "path=")

    return lines[pos].split("=")[1].strip()


def show_in_app_notification(self, message):
    if self.timeout_id is not None:
        GLib.source_remove(self.timeout_id)
        self.timeout_id = None

    self.notification_label.set_markup("<span foreground=\"white\">" +
                                       message + "</span>")
    self.notification_revealer.set_reveal_child(True)
    self.timeout_id = GLib.timeout_add(3000, timeOut, self)


def timeOut(self):
    close_in_app_notification(self)


def close_in_app_notification(self):
    self.notification_revealer.set_reveal_child(False)
    GLib.source_remove(self.timeout_id)
    self.timeout_id = None
