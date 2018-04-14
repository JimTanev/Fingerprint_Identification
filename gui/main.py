import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gui.selection import SelectionDialog
from gui.edit import EditDialog


class MainWindow(Gtk.Window):
    __fingerprint = None

    def __init__(self, tts):
        Gtk.Window.__init__(self, title="Главно меню")

        self.tts = tts
        self.executing_selection_dialog()
        self.set_default_size(800, 500)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.link_button = Gtk.LinkButton("http://localhost:8000/" + self.__fingerprint.get_id(),
                                          "Посетете localhost", expand=True)
        self.tts.add_speak_hover(self.link_button, "Посетете localhost")
        vbox.add(self.link_button)

        button_edit = Gtk.Button("Променете пръстовият отпечатък", expand=True)
        button_edit.connect("clicked", self.on_edit_clicked)
        self.tts.add_speak_hover(button_edit, "Променете пръстовият отпечатък")
        vbox.add(button_edit)

        button_exit = Gtk.Button("Изход", hexpand=True)
        button_exit.connect("clicked", lambda widget: exit(0))
        self.tts.add_speak_hover(button_exit, "Изход")
        vbox.add(button_exit)

    def executing_selection_dialog(self):
        dialog = SelectionDialog(self, self.tts)
        dialog.run()
        dialog.destroy()
        self.__fingerprint = dialog.get_fingerprint()
        if self.__fingerprint is not None:
            self.tts.speak(self.__fingerprint.get_id())
        else:
            self.tts.speak("Затваряне на програмата")
            exit(0)

    def on_edit_clicked(self, widget):
        edit_dialog = EditDialog(self, self.__fingerprint, self.tts)
        edit_dialog.run()
        edit_dialog.destroy()
        self.__fingerprint = edit_dialog.get_fingerprint()
        self.link_button.set_uri("http://localhost:8000/" + self.__fingerprint.get_id())
