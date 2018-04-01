import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gui.selection import SelectionDialog
from gui.edit import EditDialog


class MainWindow(Gtk.Window):
    __fingerprint = None

    def __init__(self):
        Gtk.Window.__init__(self, title="Demo")

        self.executing_selection_dialog()
        self.set_default_size(800, 500)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.link_button = Gtk.LinkButton("http://localhost:8080/finger/" + self.__fingerprint.get_id(),
                                          "Visit localhost", expand=True)
        vbox.add(self.link_button)

        button_edit = Gtk.Button("Edit fingerprint", expand=True)
        button_edit.connect("clicked", self.on_edit_clicked)
        vbox.add(button_edit)

        exit_button = Gtk.Button("Exit", hexpand=True)
        exit_button.connect("clicked", lambda widget: exit(0))
        vbox.add(exit_button)

    def executing_selection_dialog(self):
        dialog = SelectionDialog(self)
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
