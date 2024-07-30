import os
import shutil
import zipfile
from tqdm import tqdm  # Import tqdm for progress bars

# Get user input
AccountNameVar = input("Enter AccountNameVar: ")
RealmNameVar = input("Enter RealmNameVar: ")
CharNameVar = input("Enter CharNameVar: ")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Source paths  UNCOMMENT/CHANGE THIS IF YOU WANT TO EXPORT _classic_ OR _classic_era_ INSTEAD


# RETAIL
source_saved_variables = r"D:\Game_Install\World of Warcraft\_retail_\WTF\Account\2BIGGZ2ISBACK\SavedVariables"
source_char_folder = r"D:\Game_Install\World of Warcraft\_retail_\WTF\Account\2BIGGZ2ISBACK\Echsenkessel\Wreck"
source_interface_addons = r"D:\Game_Install\World of Warcraft\_retail_\Interface"
source_fonts = r"D:\Game_Install\World of Warcraft\_retail_\Fonts"

# CLASSIC
#source_saved_variables = r"D:\Game_Install\World of Warcraft\_classic_\WTF\Account\2BIGGZ2ISBACK\SavedVariables"
#source_char_folder = r"D:\Game_Install\World of Warcraft\_classic_\WTF\Account\2BIGGZ2ISBACK\Firemaw\Wrckk"
#source_interface_addons = r"D:\Game_Install\World of Warcraft\_classic_\Interface"
#source_fonts = r"D:\Game_Install\World of Warcraft\_classic_\Fonts"


# CLASSIC_ERA
#source_saved_variables = r"D:\Game_Install\World of Warcraft\_classic_era_\WTF\Account\2BIGGZ2ISBACK\SavedVariables"
#source_char_folder = r"D:\Game_Install\World of Warcraft\_classic_era_\WTF\Account\2BIGGZ2ISBACK\Stitches\Wrck"
#source_interface_addons = r"D:\Game_Install\World of Warcraft\_classic_era_\Interface"
#source_fonts = r"D:\Game_Install\World of Warcraft\_classic_era_\Fonts"


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Destination paths
destination_folder = r"D:\Game_Install\World of Warcraft\UI_EXPORT"
destination_wtf_folder = os.path.join(destination_folder, "WTF")
destination_account_folder = os.path.join(destination_wtf_folder, "Account", AccountNameVar, "SavedVariables")
destination_char_folder = os.path.join(destination_wtf_folder, "Account", AccountNameVar, RealmNameVar, CharNameVar)
destination_interface_addons = os.path.join(destination_folder, "Interface")
destination_fonts = os.path.join(destination_folder, "Fonts")

# Remove destination folders if they exist
if os.path.exists(destination_account_folder):
    shutil.rmtree(destination_account_folder)
if os.path.exists(destination_char_folder):
    shutil.rmtree(destination_char_folder)
if os.path.exists(destination_interface_addons):
    shutil.rmtree(destination_interface_addons)
if os.path.exists(destination_fonts):
    shutil.rmtree(destination_fonts)

# Create destination folders
os.makedirs(destination_account_folder, exist_ok=True)
os.makedirs(destination_char_folder, exist_ok=True)

# Copy individual files and folders
for root, dirs, files in os.walk(source_saved_variables):
    for file in files:
        src_file = os.path.join(root, file)
        dst_file = os.path.join(destination_account_folder, file)
        shutil.copy2(src_file, dst_file)

for root, dirs, files in os.walk(source_char_folder):
    for file in files:
        src_file = os.path.join(root, file)
        dst_file = os.path.join(destination_char_folder, file)
        shutil.copy2(src_file, dst_file)

# Copy AddOns only if the destination folder does not exist
if not os.path.exists(destination_interface_addons):
    shutil.copytree(source_interface_addons, destination_interface_addons)

# Copy Fonts only if the destination folder does not exist
if not os.path.exists(destination_fonts):
    shutil.copytree(source_fonts, destination_fonts)

print(f"Files and folders copied successfully to:\n{destination_account_folder}\n{destination_char_folder}\n{destination_interface_addons}\n{destination_fonts}")
# Get the parent directory of UI_EXPORT
parent_directory = os.path.dirname(destination_folder)

# Zip the UI_EXPORT folder
zip_filename = os.path.join(parent_directory, "UI_EXPORT.zip")

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Get the total number of files for progress bar
    total_files = sum(len(files) for _, _, files in os.walk(destination_folder))

    # Create a progress bar
    with tqdm(total=total_files, unit=' files') as pbar:
        for root, _, files in os.walk(destination_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, destination_folder)
                zipf.write(file_path, arcname=arcname)
                pbar.update(1)  # Update progress bar

print(f"UI_EXPORT folder has been zipped to {zip_filename}")

# Delete the UI_EXPORT folder
shutil.rmtree(destination_folder)
print(f"UI_EXPORT folder has been deleted")
