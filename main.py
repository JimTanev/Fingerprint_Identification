import gui

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def main():

    win = gui.MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
