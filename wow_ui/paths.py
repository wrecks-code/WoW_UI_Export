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
    return os.path.join(WOW_BASE_PATH, SELECTED_VERSION, "WTF", "Account")


def get_wow_selected_account_path() -> str:
    return os.path.join(get_wow_acc_path(), SELECTED_ACCOUNT)


def get_wow_selected_realm_path() -> str:
    return os.path.join(get_wow_selected_account_path(), SELECTED_REALM)


def get_acc_saved_vars_path() -> str:
    return os.path.join(get_wow_selected_account_path(), "SavedVariables")


def get_char_saved_vars_path() -> str:
    return os.path.join(
        get_wow_selected_realm_path(), SELECTED_CHARACTER, "SavedVariables"
    )


def get_interface_path() -> str:
    return os.path.join(WOW_BASE_PATH, SELECTED_VERSION, "Interface")


def get_fonts_path() -> str:
    return os.path.join(WOW_BASE_PATH, SELECTED_VERSION, "Fonts")


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


def get_version_from_import_file(import_file):
    global SELECTED_VERSION, IMPORT_FILE_PATH
    IMPORT_FILE_PATH = import_file

    # Remove the .zip extension
    import_file = os.path.splitext(import_file)[0]

    # Split the filename by underscores
    parts = import_file.split("_")

    # Check if there are enough parts to extract the third word
    if len(parts) >= 3:
        # Construct the result with underscores
        result = f"_{parts[3]}_"
        SELECTED_VERSION = result
    else:
        SELECTED_VERSION = "Invalid filename format"


SELECTED_VERSION = get_installed_wow_versions()[0]
SELECTED_ACCOUNT = get_available_accounts()[0]
SELECTED_REALM = get_available_realms()[0]
SELECTED_CHARACTER = get_available_chars()[0]

IMPORT_FILE_PATH = None
