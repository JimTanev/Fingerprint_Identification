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

    def __init__(self, parent, file_name, language_properties):
        self.__file_name = file_name

        Gtk.Dialog.__init__(self, 'Add new fingerprint', parent, 0)
        self.set_default_size(600, 400)
        self.set_border_width(10)
        self.tts = self.language_properties.tts
        self.messages = language_properties.messages

        box = self.get_content_area()
        box.props.orientation = Gtk.Orientation.VERTICAL

        self.__entry = Gtk.Entry(expand=True)
        self.tts.add_speak_hover(self.__entry, self.messages.add.entry_tts)
        box.pack_start(self.__entry, False, True, 0)

        button_add = Gtk.Button(self.messages.add.button_add_title, expand=True)
        button_add.connect('clicked', self.on_add_clicked)
        self.tts.add_speak_hover(button_add, self.messages.add.button_add_title)
        box.add(button_add)

        button_cancel = Gtk.Button(self.messages.add.button_cancel_title, expand=True)
        button_cancel.connect('clicked', lambda widget: self.destroy())
        self.tts.add_speak_hover(button_cancel, self.messages.add.button_cancel_title)
        box.add(button_cancel)

        self.show_all()

    def on_add_clicked(self, widget):
        entry_text = self.__entry.get_text()
        fingerprint_file = const.DB_PATH + entry_text + const.FILE_EXTENSION
        shutil.copy2(self.__file_name, fingerprint_file)
        self.__fingerprint = fingerprint.Fingerprint(fingerprint_file)
        self.tts.speak(self.messages.add.tts_add_new_fingerprint)
        self.tts.spell(entry_text)
        self.destroy()
