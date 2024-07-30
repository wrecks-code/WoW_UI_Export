import os
import sys

from wow_ui import registry, strings


def _get_base_path() -> str:
    if getattr(sys, "frozen", False):
        module_dir = os.path.dirname(sys.executable)
    else:
        module_dir = os.path.dirname(os.path.abspath(__file__))
    return _strip_package_name_from_path(module_dir)


def _strip_package_name_from_path(path) -> str:
    suffix = "wow_ui"
    return path[: -len(suffix)] if path.endswith(suffix) else path


# INTERNAL
APP_NAME = strings.EXE_NAME

EXE_FILE_NAME = f"{APP_NAME}.exe"
CONFIG_FILE_NAME = "config.ini"

BASE_PATH = _get_base_path()
EXE_PATH = os.path.join(BASE_PATH, EXE_FILE_NAME)
CONFIG_PATH = os.path.join(BASE_PATH, CONFIG_FILE_NAME)

# WOW
WOW_BASE_PATH = os.path.dirname(registry.get_wow_install_path().rstrip(os.sep))


def get_wow_acc_path() -> str:
    return os.path.join(WOW_BASE_PATH, WOW_SELECTED_VERSION, "WTF", "Account")


def get_wow_selected_account_path() -> str:
    return os.path.join(get_wow_acc_path(), WOW_SELECTED_ACCOUNT)


def get_wow_selected_realm_path() -> str:
    return os.path.join(get_wow_selected_account_path(), WOW_SELECTED_REALM)


def get_acc_saved_variables_path() -> str:
    return os.path.join(get_wow_selected_account_path(), "SavedVariables")


def get_char_path() -> str:
    return os.path.join(get_wow_selected_realm_path(), WOW_SELECTED_CHARACTER)


def get_interface_path() -> str:
    return os.path.join(WOW_BASE_PATH, WOW_SELECTED_VERSION, "Interface")


def get_fonts_path() -> str:
    return os.path.join(WOW_BASE_PATH, WOW_SELECTED_VERSION, "Fonts")


def get_installed_wow_versions() -> list:
    return [
        name
        for name in os.listdir(WOW_BASE_PATH)
        if os.path.isdir(os.path.join(WOW_BASE_PATH, name))
        and name.startswith("_")
        and name.endswith("_")
    ]


def get_available_accounts() -> list:
    try:
        return [
            name
            for name in os.listdir(get_wow_acc_path())
            if os.path.isdir(os.path.join(get_wow_acc_path(), name))
            and name != "SavedVariables"
        ]
    except Exception as e:
        print(f"Error getting available accounts: {e}")
        return []


def get_available_realms() -> list:
    try:
        return [
            name
            for name in os.listdir(get_wow_selected_account_path())
            if os.path.isdir(os.path.join(get_wow_selected_account_path(), name))
            and name != "SavedVariables"
        ]
    except Exception as e:
        print(f"Error getting available realms: {e}")
        return []


def get_available_chars() -> list:
    try:
        return [
            name
            for name in os.listdir(get_wow_selected_realm_path())
            if os.path.isdir(os.path.join(get_wow_selected_realm_path(), name))
        ]
    except Exception as e:
        print(f"Error getting available chars: {e}")
        return []


WOW_SELECTED_VERSION = get_installed_wow_versions()[0]
WOW_SELECTED_ACCOUNT = get_available_accounts()[0]
WOW_SELECTED_REALM = get_available_realms()[0]
WOW_SELECTED_CHARACTER = get_available_chars()[0]


def reset_selected_values():
    global WOW_SELECTED_VERSION, WOW_SELECTED_ACCOUNT, WOW_SELECTED_REALM, WOW_SELECTED_CHARACTER
    WOW_SELECTED_VERSION = get_installed_wow_versions()[0]
    WOW_SELECTED_ACCOUNT = get_available_accounts()[0]
    WOW_SELECTED_REALM = get_available_realms()[0]
    WOW_SELECTED_CHARACTER = get_available_chars()[0]
