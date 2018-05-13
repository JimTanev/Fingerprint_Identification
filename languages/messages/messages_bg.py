class BG:

    def __init__(self):
        self.main = Main()
        self.selection = Selection()
        self.add = Add()
        self.edit = Edit()


class Main:

    def __init__(self):
        self.link_button_title = 'Посетете сървъра'
        self.button_edit_title = 'Променете пръстовият отпечатък'
        self.button_exit_title = 'Изход'
        self.tts_close_program = 'Затваряне на програмата'


class Selection:

    def __init__(self):
        self.button_change_language_title = 'English'
        self.button_select_title = 'Изберете пръстов отпечатък'
        self.button_add_title = 'Добавете пръстов отпечатък'
        self.button_exit_title = 'Изход'
        self.file_dialog_title = 'Моля изберете tif файл'
        self.tts_fingerprint_not_found = 'Пръстовият отпечатък не е намерен'
        self.tts_fingerprint_exist_in_database = 'Пръстовият отпечатък съществува в базата нанни'
        self.tts_more_than_one_fingerprint = 'Има повече от един пръстов отпечатък намерен в базата данни'


class Add:

    def __init__(self):
        self.entry_tts = 'Въведете нов идентификационен номер'
        self.button_add_title = 'Добавяне'
        self.button_cancel_title = 'Затваряне и изход'
        self.tts_add_new_fingerprint = 'Добавен нов пръстов отпечатък с индентификационен номер'


class Edit:

    def __init__(self):
        self.entry_tts = 'Въведете нов идентификационен номер'
        self.button_update_title = 'Промяна на идентификационния номер'
        self.button_delete_title = 'Изтриване на пръстовия отпечатък'
        self.button_cancel_title = 'Затваряне'
        self.tts_update_fingerprint = 'Идентификационния номер е променен на'
        self.tts_delete_complete = 'Изтриването завършено'


