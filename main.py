import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gui.main import MainWindow
from tts import TTS


def main():
    win = MainWindow(TTS())
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
