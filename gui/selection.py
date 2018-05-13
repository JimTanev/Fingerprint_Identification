import fingerprint
import const
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .add import AddDialog


class SelectionDialog(Gtk.Dialog):
    __fingerprint = None

    def get_fingerprint(self):
        return self.__fingerprint

    def __init__(self, parent, language_properties):
        self.tts = language_properties.tts
        self.language_properties = language_properties

        Gtk.Dialog.__init__(self, 'Choose fingerprint', parent, 0)
        self.set_default_size(600, 400)
        self.set_border_width(10)
        self.messages = language_properties.messages

        self.content_area = self.get_content_area()
        self.box = self.__create_box()
        self.content_area.add(self.box)

        self.show_all()

    def __create_box(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.props.orientation = Gtk.Orientation.VERTICAL

        button_change_language = Gtk.Button(self.messages.selection.button_change_language_title, expand=True)
        button_change_language.connect('clicked', self.on_change_language_clicked)
        self.tts.add_speak_hover(button_change_language, self.messages.selection.button_change_language_title)
        box.add(button_change_language)

        button_select = Gtk.Button(self.messages.selection.button_select_title, expand=True)
        button_select.connect('clicked', self.on_select_clicked)
        self.tts.add_speak_hover(button_select, self.messages.selection.button_select_title)
        box.add(button_select)

        button_add = Gtk.Button(self.messages.selection.button_add_title, expand=True)
        button_add.connect('clicked', self.on_add_clicked)
        self.tts.add_speak_hover(button_add, self.messages.selection.button_add_title)
        box.add(button_add)

        button_exit = Gtk.Button(self.messages.selection.button_exit_title, hexpand=True)
        button_exit.connect('clicked', lambda widget: exit(0))
        self.tts.add_speak_hover(button_exit, self.messages.selection.button_exit_title)
        box.add(button_exit)

        return box

    def on_change_language_clicked(self, widget):
        self.content_area.remove(self.box)
        self.language_properties.change_language()
        self.tts = self.language_properties.tts
        self.messages = self.language_properties.messages
        self.box = self.__create_box()
        self.content_area.add(self.box)
        self.show_all()

    def on_select_clicked(self, widget):
        file_dialog = Gtk.FileChooserDialog(self.messages.selection.file_dialog_title, self,
                                            Gtk.FileChooserAction.OPEN,
                                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(file_dialog)

        response = file_dialog.run()
        if response == Gtk.ResponseType.OK:
            self.__fingerprint = self.__check_fingerprint_in_db(file_dialog.get_filename())
            if self.__fingerprint is None:
                self.tts.speak(self.messages.selection.tts_fingerprint_not_found)
            else:
                self.destroy()
        file_dialog.destroy()

    def on_add_clicked(self, widget):
        file_dialog = Gtk.FileChooserDialog(self.messages.selection.file_dialog_title, self,
                                            Gtk.FileChooserAction.OPEN,
                                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.add_filters(file_dialog)

        response = file_dialog.run()
        if response == Gtk.ResponseType.OK:
            file_name = file_dialog.get_filename()
            if self.__check_fingerprint_in_db(file_name) is None:
                add_dialog = AddDialog(self, file_name, self.language_properties)
                add_dialog.run()
                add_dialog.destroy()

                self.__fingerprint = add_dialog.get_fingerprint()
                self.destroy()
            else:
                self.tts.speak(self.messages.selection.tts_fingerprint_exist_in_database)
        file_dialog.destroy()

    def __check_fingerprint_in_db(self, file_name):
        result = fingerprint.construct_fingerprint(file_name)
        if result == const.MULTIPLE:
            self.tts.speak(self.messages.selection.tts_more_than_one_fingerprint)
            exit(0)
        else:
            return result

    @staticmethod
    def add_filters(dialog):
        filter_fingerprint = Gtk.FileFilter()
        filter_fingerprint.set_name('image/tif')
        filter_fingerprint.add_mime_type('image/tif')
        filter_fingerprint.add_pattern('*' + const.FILE_EXTENSION)
        dialog.add_filter(filter_fingerprint)
