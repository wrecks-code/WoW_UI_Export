from wow_ui import export_ui


def main():
    setup_gui = export_ui.Application()
    setup_gui.root_window.mainloop()


if __name__ == "__main__":
    main()
