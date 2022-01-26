from WindowClass import *

def main():
    app = QApplication(sys.argv)
    wnd = WindowClass()
    wnd.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    