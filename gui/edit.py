import os
import const
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class EditDialog(Gtk.Dialog):
    __fingerprint = None

    def get_fingerprint(self):
        return self.__fingerprint

    def __init__(self, parent, fingerprint, tts):
        Gtk.Dialog.__init__(self, "Промяна на пръстовия отпечатък", parent, 0)

        self.__fingerprint = fingerprint
        self.tts = tts

        self.set_default_size(600, 400)

        box = self.get_content_area()
        box.props.orientation = Gtk.Orientation.VERTICAL

        self.__entry = Gtk.Entry()
        self.tts.add_speak_hover(self.__entry, "Въведете нов идентификационен номер")
        box.pack_start(self.__entry, False, True, 0)

        button_update = Gtk.Button("Промяна на идентификационния номер", expand=True)
        button_update.connect("clicked", self.on_update_clicked)
        self.tts.add_speak_hover(button_update, "Промяна на идентификационния номер")
        box.add(button_update)

        button_delete = Gtk.Button("Изтриване на пръстовия отпечатък", expand=True)
        button_delete.connect("clicked", self.on_delete_clicked)
        self.tts.add_speak_hover(button_delete, "Изтриване на пръстовия отпечатък")
        box.add(button_delete)

        button_cancel = Gtk.Button("Затваряне", expand=True)
        button_cancel.connect("clicked", lambda widget: self.destroy())
        self.tts.add_speak_hover(button_cancel, "Затваряне")
        box.add(button_cancel)

        self.show_all()

    def on_update_clicked(self, widget):
        entry_text = self.__entry.get_text()
        updated_relative_file_name = const.DB_PATH + entry_text + const.FILE_EXTENSION
        os.rename(self.__fingerprint.get_file_name(), updated_relative_file_name)
        self.__fingerprint.set_file_name(updated_relative_file_name)
        self.tts.speak("Идентификационния номер е променен на " + entry_text)

    def on_delete_clicked(self, widget):
        os.remove(self.__fingerprint.get_file_name())
        self.tts.speak("Изтриването завършено")
        exit(0)
