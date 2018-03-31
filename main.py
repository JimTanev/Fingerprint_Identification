import fingerprint
import gui

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def main():
    # file_name = fmatcher.get_ID('fingerprints/one_more.tif')
    # print(file_name)

    win = gui.MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
