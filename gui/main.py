import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .selection import SelectionDialog
from .edit import EditDialog


class MainWindow(Gtk.Window):
    __fingerprint = None

    def __init__(self, language_properties):
        self.language_properties = language_properties

        Gtk.Window.__init__(self, title='Main menu')
        self.set_default_size(800, 500)
        self.set_border_width(10)

        self.executing_selection_dialog()
        self.tts = self.language_properties.tts
        self.messages = self.language_properties.messages

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.link_button_uri = 'http://localhost:8000/' + self.__fingerprint.get_id()

        self.link_button = Gtk.LinkButton(self.link_button_uri, self.messages.main.link_button_title, expand=True)
        self.tts.add_speak_hover(self.link_button, self.messages.main.link_button_title)
        vbox.add(self.link_button)

        button_edit = Gtk.Button(self.messages.main.button_edit_title, expand=True)
        button_edit.connect('clicked', self.on_edit_clicked)
        self.tts.add_speak_hover(button_edit, self.messages.main.button_edit_title)
        vbox.add(button_edit)

        button_exit = Gtk.Button(self.messages.main.button_exit_title, hexpand=True)
        button_exit.connect('clicked', lambda widget: exit(0))
        self.tts.add_speak_hover(button_exit, self.messages.main.button_exit_title)
        vbox.add(button_exit)

    def executing_selection_dialog(self):
        dialog = SelectionDialog(self, self.language_properties)
        dialog.run()
        dialog.destroy()
        self.__fingerprint = dialog.get_fingerprint()
        if self.__fingerprint is not None:
            self.language_properties.tts.spell(self.__fingerprint.get_id())
        else:
            self.language_properties.tts.speak(self.messages.main.tts_close_program)
            exit(0)

    def on_edit_clicked(self, widget):
        edit_dialog = EditDialog(self, self.__fingerprint, self.language_properties)
        edit_dialog.run()
        edit_dialog.destroy()
        self.__fingerprint = edit_dialog.get_fingerprint()
        self.link_button.set_uri(self.link_button_uri)
