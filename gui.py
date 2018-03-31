import fingerprint
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    __fingerprint = None

    def __init__(self):
        Gtk.Window.__init__(self, title="Demo")

        self.executing_selection_dialog()
        self.set_default_size(800, 500)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.link_button = Gtk.LinkButton("http://localhost:8080/finger/" + self.__fingerprint.get_id(), "Visit localhost", expand=True)
        vbox.add(self.link_button)

        button_edit = Gtk.Button("Edit fingerprint", expand=True)
        button_edit.connect("clicked", self.on_edit_clicked)
        vbox.add(button_edit)

        exit_button = Gtk.Button("Exit", hexpand=True)
        exit_button.connect("clicked", lambda widget: exit(0))
        vbox.add(exit_button)

    def executing_selection_dialog(self):
        dialog = FingerprintSelectionDialog(self)
        dialog.run()
        dialog.destroy()
        self.__fingerprint = dialog.get_fingerprint()
        if self.__fingerprint is None:
            exit(0)

    def on_edit_clicked(self, widget):
        edit_dialog = EditDialog(self, self.__fingerprint)
        edit_dialog.run()
        edit_dialog.destroy()
        self.__fingerprint = edit_dialog.get_fingerprint()
        self.link_button.set_uri("http://localhost:8080/finger/" + self.__fingerprint.get_id())


class FingerprintSelectionDialog(Gtk.Dialog):
    __fingerprint = None

    def get_fingerprint(self):
        return self.__fingerprint

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Fingerprint selection", parent, 0)

        self.set_default_size(600, 400)
        self.set_border_width(10)

        box = self.get_content_area()
        box.props.orientation = Gtk.Orientation.VERTICAL

        button_choose = Gtk.Button("Select Fingerprint", expand=True)
        button_choose.connect("clicked", self.on_select_clicked)
        box.add(button_choose)

        button_add = Gtk.Button("Add Fingerprint", expand=True)
        button_add.connect("clicked", self.on_add_clicked)
        box.add(button_add)

        exit_button = Gtk.Button("Exit", hexpand=True)
        exit_button.connect("clicked", lambda widget: exit(0))
        box.add(exit_button)

        self.show_all()

    def on_select_clicked(self, widget):
        file_dialog = Gtk.FileChooserDialog("Please select a tif file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(file_dialog)

        response = file_dialog.run()
        if response == Gtk.ResponseType.OK:
            self.__fingerprint = fingerprint.construct_fingerprint(file_dialog.get_filename())
            file_dialog.destroy()
            self.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            file_dialog.destroy()

    def on_add_clicked(self, widget):
        file_dialog = Gtk.FileChooserDialog("Please select a tif file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(file_dialog)

        response = file_dialog.run()
        if response == Gtk.ResponseType.OK:
            file_name = file_dialog.get_filename()
            if fingerprint.construct_fingerprint(file_name) is None:
                add_dialog = AddDialog(self, file_name)
                file_dialog.destroy()
                add_dialog.run()
                add_dialog.destroy()

                self.__fingerprint = add_dialog.get_fingerprint()
                self.destroy()
            else:
                file_dialog.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            file_dialog.destroy()

    @staticmethod
    def add_filters(dialog):
        filter_fingerprint = Gtk.FileFilter()
        filter_fingerprint.set_name("Fingerprints")
        filter_fingerprint.add_mime_type("image/tif")
        filter_fingerprint.add_pattern("*.tif")
        dialog.add_filter(filter_fingerprint)


class AddDialog(Gtk.Dialog):
    __fingerprint = None
    __file_name = None

    def get_fingerprint(self):
        return self.__fingerprint

    def __init__(self, parent, file_name):
        Gtk.Dialog.__init__(self, 'Add fingerprint', parent, 0)

        self.__file_name = file_name

        self.set_default_size(600, 400)

        box = self.get_content_area()
        box.props.orientation = Gtk.Orientation.VERTICAL

        self.__entry = Gtk.Entry()
        box.pack_start(self.__entry, False, True, 0)

        button_add = Gtk.Button("Add fingerprint", expand=True)
        button_add.connect("clicked", self.on_add_clicked)
        box.add(button_add)

        button_delete = Gtk.Button("Cancel fingerprint", expand=True)
        button_delete.connect("clicked", self.on_cancel_clicked)
        box.add(button_delete)

        self.show_all()

    def on_add_clicked(self, widget):
        fingerprint_file = 'DB1/' + self.__entry.get_text() + '.tif'
        os.rename(self.__file_name, fingerprint_file)
        self.__fingerprint = fingerprint.Fingerprint(fingerprint_file)
        self.destroy()

    def on_cancel_clicked(self, widget):
        self.destroy()


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

        button_delete = Gtk.Button("Cancel fingerprint", expand=True)
        button_delete.connect("clicked", self.on_cancel_clicked)
        box.add(button_delete)

        self.show_all()

    def on_update_clicked(self, widget):
        updated_relative_file_name = 'DB1/' + self.__entry.get_text() + '.tif'
        os.rename(self.__fingerprint.get_file_name(), updated_relative_file_name)
        self.__fingerprint.set_file_name(updated_relative_file_name)

    def on_delete_clicked(self, widget):
        os.remove(self.__fingerprint.get_file_name())
        exit(0)

    def on_cancel_clicked(self, widget):
        self.destroy()
