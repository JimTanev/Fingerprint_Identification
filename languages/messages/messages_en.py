class EN:

    def __init__(self):
        self.main = Main()
        self.selection = Selection()
        self.add = Add()
        self.edit = Edit()


class Main:

    def __init__(self):
        self.link_button_title = 'Visit the server'
        self.button_edit_title = 'Change fingerprint'
        self.button_exit_title = 'Exit'
        self.tts_close_program = 'Close the program'


class Selection:

    def __init__(self):
        self.button_change_language_title = 'Bulgarian'
        self.button_select_title = 'Select fingerprint'
        self.button_add_title = 'Add fingerprint'
        self.button_exit_title = 'Exit'
        self.file_dialog_title = 'Please choose tif file'
        self.tts_fingerprint_not_found = 'The fingerprint is not found'
        self.tts_fingerprint_exist_in_database = 'Fingerprint exist in database'
        self.tts_more_than_one_fingerprint = 'There is more than one fingerprint found in database'


class Add:

    def __init__(self):
        self.entry_tts = 'Add new identification number'
        self.button_add_title = 'Add'
        self.button_cancel_title = 'Close and exit'
        self.tts_add_new_fingerprint = 'New fingerprint has been added'


class Edit:

    def __init__(self):
        self.entry_tts = 'Add new identification number'
        self.button_update_title = 'Update identification number'
        self.button_delete_title = 'Delete fingerprint'
        self.button_cancel_title = 'Cancel'
        self.tts_update_fingerprint = 'The identification number has been changed to'
        self.tts_delete_complete = 'Delete is complete'


