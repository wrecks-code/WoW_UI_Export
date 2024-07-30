import winreg


def get_wow_install_path() -> str:
    key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        r"SOFTWARE\WOW6432Node\Blizzard Entertainment\World of Warcraft",
    )
    install_location, _ = winreg.QueryValueEx(key, "InstallPath")
    return str(install_location)
