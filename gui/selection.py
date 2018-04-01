import fingerprint
import const
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gui.add import AddDialog


class SelectionDialog(Gtk.Dialog):
    __fingerprint = None

    def get_fingerprint(self):
        return self.__fingerprint

    def __init__(self, parent, tts):
        Gtk.Dialog.__init__(self, "Избор на пръстов отпечатък", parent, 0)

        self.tts = tts

        self.set_default_size(600, 400)
        self.set_border_width(10)

        box = self.get_content_area()
        box.props.orientation = Gtk.Orientation.VERTICAL

        button_select = Gtk.Button("Изберете пръстов отпечатък", expand=True)
        button_select.connect("clicked", self.on_select_clicked)
        self.tts.add_speak_hover(button_select, "Изберете пръстов отпечатък")
        box.add(button_select)

        button_add = Gtk.Button("Добавете пръстов отпечатък", expand=True)
        button_add.connect("clicked", self.on_add_clicked)
        self.tts.add_speak_hover(button_add, "Добавете пръстов отпечатък")
        box.add(button_add)

        button_exit = Gtk.Button("Изход", hexpand=True)
        button_exit.connect("clicked", lambda widget: exit(0))
        self.tts.add_speak_hover(button_exit, "Изход")
        box.add(button_exit)

        self.show_all()

    def on_select_clicked(self, widget):
        file_dialog = Gtk.FileChooserDialog("Моля изберете tif файл", self,
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
        file_dialog = Gtk.FileChooserDialog("Моля изберете tif файл", self,
                                            Gtk.FileChooserAction.OPEN,
                                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.add_filters(file_dialog)

        response = file_dialog.run()
        if response == Gtk.ResponseType.OK:
            file_name = file_dialog.get_filename()
            if fingerprint.construct_fingerprint(file_name) is None:
                add_dialog = AddDialog(self, file_name, self.tts)
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
        filter_fingerprint.set_name("image/tif")
        filter_fingerprint.add_mime_type("image/tif")
        filter_fingerprint.add_pattern("*" + const.FILE_EXTENSION)
        dialog.add_filter(filter_fingerprint)
