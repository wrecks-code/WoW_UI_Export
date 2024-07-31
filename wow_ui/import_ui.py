import sys
import tkinter
import customtkinter
from customtkinter import (
    CTkFrame,
    CTkLabel,
    CTkOptionMenu,
    CTkButton,
    filedialog,
)
from wow_ui import paths, strings, filemanager


class Application:
    account_menu: CTkOptionMenu = None
    realm_menu: CTkOptionMenu = None
    char_menu: CTkOptionMenu = None

    def __init__(self):
        # sourcery skip: swap-if-else-branches, use-named-expression
        customtkinter.set_ctk_parent_class(tkinter.Tk)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root_window = customtkinter.CTk()
        self.root_window.title(strings.TITLE_IMPORTER)
        self.root_window.resizable(False, False)
        self.root_window.protocol("WM_DELETE_WINDOW", self.exit_application)

        file_path = filedialog.askopenfilename(
            title=strings.FILE_DIALOG_TITLE, filetypes=[("Zip files", "*.zip")]
        )
        if not file_path:
            self.exit_application()
        else:
            paths.get_version_from_import_file(file_path)
            print(f"Selected file: {file_path}")
            print(f"detected version: {paths.SELECTED_VERSION}")

        self.selection_frame = CTkFrame(master=self.root_window)
        self.selection_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.execute_btn_frame = CTkFrame(master=self.root_window)
        self.execute_btn_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # self.root_window.iconbitmap(paths.ASSETS_ICO_PATH)
        self.show_account_selector()
        self.show_realm_selector()
        self.show_char_selector()
        self.show_btn()
        self.refresh_menus(0)

    def exit_application(self):
        self.root_window.destroy()
        sys.exit(1)

    # ! Account Selector Menu

    def show_account_selector(self):
        label = CTkLabel(
            text=strings.LABEL_SELECT_ACCOUNT,
            master=self.selection_frame,
            justify=customtkinter.CENTER,
        )

        def select_account(selected_option):
            paths.SELECTED_ACCOUNT = selected_option
            self.refresh_menus(1)

        self.account_menu = CTkOptionMenu(
            self.selection_frame,
            values=paths.get_available_accounts(),
            command=select_account,
        )

        label.pack(pady=5, padx=5)
        self.account_menu.pack(pady=10, padx=10)

    def show_realm_selector(self):
        label = CTkLabel(
            text=strings.LABEL_SELECT_REALM,
            master=self.selection_frame,
            justify=customtkinter.CENTER,
        )

        def select_realm(selected_option):
            paths.IMPORT_SELECTED_REALM = selected_option
            self.refresh_menus(2)

        self.realm_menu = CTkOptionMenu(
            self.selection_frame,
            values=paths.get_available_realms(),
            command=select_realm,
        )

        label.pack(pady=5, padx=5)
        self.realm_menu.pack(pady=10, padx=10)

    # ! Char Selector Menu
    def show_char_selector(self):
        label = CTkLabel(
            text=strings.LABEL_SELECT_CHAR,
            master=self.selection_frame,
            justify=customtkinter.CENTER,
        )

        def select_char(selected_option):
            paths.SELECTED_CHARACTER = selected_option

        self.char_menu = CTkOptionMenu(
            self.selection_frame,
            values=paths.get_available_chars(),
            command=select_char,
        )

        label.pack(pady=5, padx=5)
        self.char_menu.pack(pady=10, padx=10)

        # ! Button Functions

    def show_btn(self):
        def execute_btn():
            filemanager.import_and_unzip()

        btn = CTkButton(
            text=strings.BTN_IMPORT_TXT,
            master=self.execute_btn_frame,
            command=execute_btn,
        )
        btn.pack(pady=10, padx=10)

    def refresh_menus(self, level):
        if level == 0:
            paths.SELECTED_ACCOUNT = paths.get_available_accounts()[0]
            self.account_menu.configure(values=paths.get_available_accounts())
            self.account_menu.set(paths.SELECTED_ACCOUNT)

            paths.SELECTED_REALM = paths.get_available_realms()[0]
            self.realm_menu.configure(values=paths.get_available_realms())
            self.realm_menu.set(paths.SELECTED_REALM)

            paths.SELECTED_CHARACTER = paths.get_available_chars()[0]
            self.char_menu.configure(values=paths.get_available_chars())
            self.char_menu.set(paths.SELECTED_CHARACTER)
        if level == 1:
            paths.SELECTED_REALM = paths.get_available_realms()[0]
            self.realm_menu.configure(values=paths.get_available_realms())
            self.realm_menu.set(paths.SELECTED_REALM)

            paths.SELECTED_CHARACTER = paths.get_available_chars()[0]
            self.char_menu.configure(values=paths.get_available_chars())
            self.char_menu.set(paths.SELECTED_CHARACTER)
        if level == 2:
            paths.SELECTED_CHARACTER = paths.get_available_chars()[0]
            self.char_menu.configure(values=paths.get_available_chars())
            self.char_menu.set(paths.SELECTED_CHARACTER)

        print("refreshing menus...")
        print(f"selected_version: {paths.SELECTED_VERSION}")
        print(f"selected_account: {paths.SELECTED_ACCOUNT}")
        print(f"selected_realm: {paths.SELECTED_REALM}")
        print(f"selected_character: {paths.SELECTED_CHARACTER}")
