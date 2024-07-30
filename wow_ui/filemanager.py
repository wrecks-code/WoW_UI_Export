import os
import shutil
from wow_ui import paths

# Destination paths
destination_folder = os.path.join(paths.WOW_BASE_PATH, "UI_EXPORT")
destination_wtf_folder = os.path.join(destination_folder, "WTF")

destination_account_folder = os.path.join(
    destination_wtf_folder, "Account", paths.WOW_SELECTED_ACCOUNT, "SavedVariables"
)
destination_char_folder = os.path.join(
    destination_wtf_folder,
    "Account",
    paths.WOW_SELECTED_ACCOUNT,
    paths.WOW_SELECTED_REALM,
    paths.WOW_SELECTED_CHARACTER,
)
destination_interface_addons = os.path.join(destination_folder, "Interface")
destination_fonts = os.path.join(destination_folder, "Fonts")


def copy_stuff():
    # Remove destination folders if they exist
    if os.path.exists(destination_account_folder):
        shutil.rmtree(destination_account_folder)
    if os.path.exists(destination_char_folder):
        shutil.rmtree(destination_char_folder)
    if os.path.exists(destination_interface_addons):
        shutil.rmtree(destination_interface_addons)
    if os.path.exists(destination_fonts):
        shutil.rmtree(destination_fonts)

    shutil.copytree(paths.get_acc_saved_variables_path(), destination_account_folder)
    shutil.copytree(paths.get_char_path(), destination_char_folder)
    shutil.copytree(paths.get_interface_path(), destination_interface_addons)
    shutil.copytree(paths.get_fonts_path(), destination_fonts)
