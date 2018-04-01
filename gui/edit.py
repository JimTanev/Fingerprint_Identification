import os

import gi

import const

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class EditDialog(Gtk.Dialog):
    __fingerprint = None

    def get_fingerprint(self):
        return self.__fingerprint

    def __init__(self, parent, fingerprint):
        Gtk.Dialog.__init__(self, 'Update Fingerprint', parent, 0)

        self.__fingerprint = fingerprint

        self.set_default_size(600, 400)

        box = self.get_content_area()
        box.props.orientation = Gtk.Orientation.VERTICAL

        self.__entry = Gtk.Entry()
        box.pack_start(self.__entry, False, True, 0)

        button_update = Gtk.Button("Update fingerprint", expand=True)
        button_update.connect("clicked", self.on_update_clicked)
        box.add(button_update)

        button_delete = Gtk.Button("Delete fingerprint", expand=True)
        button_delete.connect("clicked", self.on_delete_clicked)
        box.add(button_delete)

        button_cancel = Gtk.Button("Cancel fingerprint", expand=True)
        button_cancel.connect("clicked", lambda widget: self.destroy())
        box.add(button_cancel)

        self.show_all()

    def on_update_clicked(self, widget):
        updated_relative_file_name = const.DB_PATH + self.__entry.get_text() + '.tif'
        os.rename(self.__fingerprint.get_file_name(), updated_relative_file_name)
        self.__fingerprint.set_file_name(updated_relative_file_name)

    def on_delete_clicked(self, widget):
        os.remove(self.__fingerprint.get_file_name())
        exit(0)
