import sys
import tkinter
import customtkinter
from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu, CTkButton, CTkCheckBox
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

        # self.root_window.iconbitmap(paths.ASSETS_ICO_PATH)
        self.show_version_selector()
        self.show_account_selector()
        self.show_realm_selector()
        self.show_char_selector()
        self.show_btn()
        self.show_icons_checkbox()

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
            paths.WOW_SELECTED_VERSION = selected_option
            self.refresh_menus(0)

        global version_menu
        version_menu = CTkOptionMenu(
            self.selection_frame,
            values=paths.get_installed_wow_versions(),
            command=select_version,
        )
        version_menu.pack(pady=10, padx=10)

    # ! Account Selector Menu

    def show_account_selector(self):
        label = CTkLabel(
            text=strings.LABEL_SELECT_ACCOUNT,
            master=self.selection_frame,
            justify=customtkinter.CENTER,
        )

        def select_account(selected_option):
            paths.WOW_SELECTED_ACCOUNT = selected_option
            self.refresh_menus(1)

        global account_menu
        account_menu = CTkOptionMenu(
            self.selection_frame,
            values=paths.get_available_accounts(),
            command=select_account,
        )

        label.pack(pady=5, padx=5)
        account_menu.pack(pady=10, padx=10)

    def show_realm_selector(self):
        label = CTkLabel(
            text=strings.LABEL_SELECT_REALM,
            master=self.selection_frame,
            justify=customtkinter.CENTER,
        )

        def select_realm(selected_option):
            paths.WOW_SELECTED_REALM = selected_option
            self.refresh_menus(2)

        global realm_menu
        realm_menu = CTkOptionMenu(
            self.selection_frame,
            values=paths.get_available_realms(),
            command=select_realm,
        )

        label.pack(pady=5, padx=5)
        realm_menu.pack(pady=10, padx=10)

    # ! Char Selector Menu
    def show_char_selector(self):
        label = CTkLabel(
            text=strings.LABEL_SELECT_CHAR,
            master=self.selection_frame,
            justify=customtkinter.CENTER,
        )

        def select_char(selected_option):
            paths.WOW_SELECTED_CHARACTER = selected_option

        global char_menu
        char_menu = CTkOptionMenu(
            self.selection_frame,
            values=paths.get_available_chars(),
            command=select_char,
        )

        label.pack(pady=5, padx=5)
        char_menu.pack(pady=10, padx=10)

        # ! Button Functions

    def show_btn(self):
        def select_acc_btn():
            filemanager.copy_stuff()

        ok_btn = CTkButton(
            text=strings.BTN_EXPORT_TXT,
            master=self.selection_frame,
            command=select_acc_btn,
        )
        ok_btn.pack(pady=10, padx=10)

    def show_icons_checkbox(self):
        def checkbox_event():
            print("toggle")

        checkbox = CTkCheckBox(
            master=self.selection_frame,
            text=strings.LABEL_CHECKBOX,
            command=checkbox_event,
        )
        checkbox.pack(pady=10, padx=10)

    def refresh_menus(self, level):
        # available_chars = paths.get_available_chars()

        if level == 0:
            paths.WOW_SELECTED_ACCOUNT = paths.get_available_accounts()[0]
            account_menu.configure(values=paths.get_available_accounts())
            account_menu.set(paths.WOW_SELECTED_ACCOUNT)

            paths.WOW_SELECTED_REALM = paths.get_available_realms()[0]
            realm_menu.configure(values=paths.get_available_realms())
            realm_menu.set(paths.WOW_SELECTED_REALM)

            paths.WOW_SELECTED_CHARACTER = paths.get_available_chars()[0]
            char_menu.configure(values=paths.get_available_chars())
            char_menu.set(paths.WOW_SELECTED_CHARACTER)
        if level == 1:
            paths.WOW_SELECTED_REALM = paths.get_available_realms()[0]
            realm_menu.configure(values=paths.get_available_realms())
            realm_menu.set(paths.WOW_SELECTED_REALM)

            paths.WOW_SELECTED_CHARACTER = paths.get_available_chars()[0]
            char_menu.configure(values=paths.get_available_chars())
            char_menu.set(paths.WOW_SELECTED_CHARACTER)
        if level == 2:
            paths.WOW_SELECTED_CHARACTER = paths.get_available_chars()[0]
            char_menu.configure(values=paths.get_available_chars())
            char_menu.set(paths.WOW_SELECTED_CHARACTER)

        print("refreshing menus...")
        print(f"selected_version: {paths.WOW_SELECTED_VERSION}")
        print(f"selected_account: {paths.WOW_SELECTED_ACCOUNT}")
        print(f"selected_realm: {paths.WOW_SELECTED_REALM}")
        print(f"selected_character: {paths.WOW_SELECTED_CHARACTER}")
