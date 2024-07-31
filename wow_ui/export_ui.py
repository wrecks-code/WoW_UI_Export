import sys
import tkinter
import customtkinter
from customtkinter import (
    CTkFrame,
    CTkLabel,
    CTkOptionMenu,
    CTkButton,
    CTkCheckBox,
)
from wow_ui import paths, strings, filemanager


class Application:
    version_menu: CTkOptionMenu = None
    account_menu: CTkOptionMenu = None
    realm_menu: CTkOptionMenu = None
    char_menu: CTkOptionMenu = None

    include_icons: bool = False

    def __init__(self):
        customtkinter.set_ctk_parent_class(tkinter.Tk)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root_window = customtkinter.CTk()
        self.root_window.title(strings.TITLE_EXPORTER)
        self.root_window.resizable(False, False)
        self.root_window.protocol("WM_DELETE_WINDOW", self.exit_application)

        self.selection_frame = CTkFrame(master=self.root_window)
        self.selection_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.execute_btn_frame = CTkFrame(master=self.root_window)
        self.execute_btn_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # self.root_window.iconbitmap(paths.ASSETS_ICO_PATH)
        self.show_version_selector()
        self.show_account_selector()
        self.show_realm_selector()
        self.show_char_selector()
        self.show_icons_checkbox()
        self.show_btn()

        paths.SELECTED_VERSION = paths.get_installed_wow_versions()[0]
        self.refresh_menus(0)

    def exit_application(self):
        self.root_window.destroy()
        sys.exit(1)

    # ! Version Selector Menu

    def show_version_selector(self):

        label = CTkLabel(
            text=strings.LABEL_SELECT_VERSION,
            master=self.selection_frame,
            justify=customtkinter.CENTER,
        )
        label.pack(pady=5, padx=5)

        def select_version(selected_option):
            paths.SELECTED_VERSION = selected_option
            self.refresh_menus(0)

        self.version_menu = CTkOptionMenu(
            self.selection_frame,
            values=paths.get_installed_wow_versions(),
            command=select_version,
        )
        self.version_menu.pack(pady=10, padx=10)

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
            paths.SELECTED_REALM = selected_option
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

    def show_icons_checkbox(self):
        def checkbox_event():
            self.include_icons = not self.include_icons

        checkbox = CTkCheckBox(
            master=self.selection_frame,
            text=strings.LABEL_CHECKBOX,
            command=checkbox_event,
        )
        checkbox.pack(pady=10, padx=10)

    def show_btn(self):
        def execute_btn():
            filemanager.export_and_zip(self.include_icons)

        btn = CTkButton(
            text=strings.BTN_EXPORT_TXT,
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
