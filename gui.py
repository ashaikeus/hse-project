from PySide6.QtWidgets import QApplication, QMainWindow
from main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
