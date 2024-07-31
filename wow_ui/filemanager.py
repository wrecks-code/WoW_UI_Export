import os
import shutil
import zipfile
from wow_ui import paths


def export_and_zip(export_icons: bool):
    # Destination paths
    ui_export_folder = os.path.join(
        paths.WOW_BASE_PATH, f"UI_EXPORT{paths.SELECTED_VERSION}"
    )
    destination_wtf_folder = os.path.join(ui_export_folder, "WTF")

    destination_interface = os.path.join(ui_export_folder, "Interface")
    destination_fonts = os.path.join(ui_export_folder, "Fonts")
    destination_account_folder = os.path.join(
        destination_wtf_folder,
        "Account",
        paths.SELECTED_ACCOUNT,
        "SavedVariables",
    )
    destination_char_folder = os.path.join(
        destination_wtf_folder,
        "Account",
        paths.SELECTED_ACCOUNT,
        paths.SELECTED_REALM,
        paths.SELECTED_CHARACTER,
        "SavedVariables",
    )

    # Remove destination folders if they exist
    if os.path.exists(ui_export_folder):
        shutil.rmtree(ui_export_folder)
    if os.path.exists(
        os.path.join(paths.WOW_BASE_PATH, f"UI_EXPORT{paths.SELECTED_VERSION}.zip")
    ):
        os.remove(
            os.path.join(paths.WOW_BASE_PATH, f"UI_EXPORT{paths.SELECTED_VERSION}.zip")
        )

    if export_icons:
        shutil.copytree(paths.get_interface_path(), destination_interface)
    else:
        shutil.copytree(
            os.path.join(paths.get_interface_path(), "Addons"),
            os.path.join(destination_interface, "Addons"),
        )

    shutil.copytree(paths.get_acc_saved_vars_path(), destination_account_folder)
    shutil.copytree(paths.get_char_saved_vars_path(), destination_char_folder)
    shutil.copytree(paths.get_fonts_path(), destination_fonts)

    shutil.make_archive(
        os.path.join(paths.WOW_BASE_PATH, f"UI_EXPORT{paths.SELECTED_VERSION}"),
        "zip",
        ui_export_folder,
    )
    shutil.rmtree(ui_export_folder)


def import_and_unzip():
    print("import_and_unzip")

    # delete files if they exist
    if os.path.exists(paths.get_fonts_path()):
        shutil.rmtree(paths.get_fonts_path())
    if os.path.exists(paths.get_interface_path()):
        shutil.rmtree(paths.get_interface_path())
    if os.path.exists(paths.get_acc_saved_vars_path()):
        shutil.rmtree(paths.get_acc_saved_vars_path())
    if os.path.exists(paths.get_char_saved_vars_path()):
        shutil.rmtree(paths.get_char_saved_vars_path())

    # extract_folder_from_importzip("Fonts/", paths.get_fonts_path())
    extract_folder_from_importzip("Interface/Addons/", paths.get_interface_path())

    # dest_path = os.path.join(paths.WOW_BASE_PATH, paths.SELECTED_VERSION)


def extract_folder_from_importzip(folder_name, destination_path):

    zip_path = paths.IMPORT_FILE_PATH

    with zipfile.ZipFile(zip_path, "r") as archive:
        # List all files in the zip archive
        all_files = archive.namelist()

        # Filter files that are in the specified folder
        folder_files = [f for f in all_files if f.startswith(folder_name)]

        # Extract each file to the destination path
        for file in folder_files:
            # Create the full path for the destination file
            dest_file_path = os.path.join(
                destination_path, os.path.relpath(file, folder_name)
            )
            dest_dir = os.path.dirname(dest_file_path)

            # Create directories if they don't exist
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Extract the file
            with archive.open(file) as source, open(dest_file_path, "wb") as target:
                target.write(source.read())
