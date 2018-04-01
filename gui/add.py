import const
import fingerprint
import shutil
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AddDialog(Gtk.Dialog):
    __fingerprint = None
    __file_name = None

    def get_fingerprint(self):
        return self.__fingerprint

    def __init__(self, parent, file_name, tts):
        Gtk.Dialog.__init__(self, "Добавяне на пръстов отпечатък", parent, 0)

        self.__file_name = file_name
        self.tts = tts

        self.set_default_size(600, 400)

        box = self.get_content_area()
        box.props.orientation = Gtk.Orientation.VERTICAL

        self.__entry = Gtk.Entry()
        box.pack_start(self.__entry, False, True, 0)

        button_add = Gtk.Button("Добавяне", expand=True)
        button_add.connect("clicked", self.on_add_clicked)
        self.tts.add_speak_hover(button_add, "Добавяне")
        box.add(button_add)

        button_cancel = Gtk.Button("Затваряне и изход", expand=True)
        button_cancel.connect("clicked", lambda widget: self.destroy())
        self.tts.add_speak_hover(button_cancel, "Затваряне и изход")
        box.add(button_cancel)

        self.show_all()

    def on_add_clicked(self, widget):
        entry_text = self.__entry.get_text()
        fingerprint_file = const.DB_PATH + entry_text + const.FILE_EXTENSION
        shutil.copy2(self.__file_name, fingerprint_file)
        self.__fingerprint = fingerprint.Fingerprint(fingerprint_file)
        self.tts.speak("Добавен нов пръстов отпечатък с индентификационен номер " + entry_text)
        self.destroy()
