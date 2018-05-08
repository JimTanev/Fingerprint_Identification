import os
import const
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class EditDialog(Gtk.Dialog):
    __fingerprint = None

    def get_fingerprint(self):
        return self.__fingerprint

    def __init__(self, parent, fingerprint, language_properties):
        self.__fingerprint = fingerprint

        Gtk.Dialog.__init__(self, 'Edit fingerprint', parent, 0)
        self.set_default_size(600, 400)
        self.set_border_width(10)
        self.tts = language_properties.tts
        self.messages = language_properties.messages

        box = self.get_content_area()
        box.props.orientation = Gtk.Orientation.VERTICAL

        self.__entry = Gtk.Entry(expand=True)
        self.tts.add_speak_hover(self.__entry, self.messages.edit.entry_tts)
        box.pack_start(self.__entry, False, True, 0)

        button_update = Gtk.Button(self.messages.edit.button_update_title, expand=True)
        button_update.connect('clicked', self.on_update_clicked)
        self.tts.add_speak_hover(button_update, self.messages.edit.button_update_title)
        box.add(button_update)

        button_delete = Gtk.Button(self.messages.edit.button_delete_title, expand=True)
        button_delete.connect('clicked', self.on_delete_clicked)
        self.tts.add_speak_hover(button_delete, self.messages.edit.button_delete_title)
        box.add(button_delete)

        button_cancel = Gtk.Button(self.messages.edit.button_cancel_title, expand=True)
        button_cancel.connect('clicked', lambda widget: self.destroy())
        self.tts.add_speak_hover(button_cancel, self.messages.edit.button_cancel_title)
        box.add(button_cancel)

        self.show_all()

    def on_update_clicked(self, widget):
        entry_text = self.__entry.get_text()
        updated_relative_file_name = const.DB_PATH + entry_text + const.FILE_EXTENSION
        os.rename(self.__fingerprint.get_file_name(), updated_relative_file_name)
        self.__fingerprint.set_file_name(updated_relative_file_name)
        self.tts.speak(self.messages.edit.tts_update_fingerprint)
        self.tts.spell(entry_text)

    def on_delete_clicked(self, widget):
        os.remove(self.__fingerprint.get_file_name())
        self.tts.speak(self.messages.edit.tts_delete_complete)
        exit(0)
