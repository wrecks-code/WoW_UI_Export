from wow_ui import import_ui


def main():
    setup_gui = import_ui.Application()
    setup_gui.root_window.mainloop()


if __name__ == "__main__":
    main()
