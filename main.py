import sys
import re
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.quitButton.clicked.connect(app.exit)
        # self.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)
        self.keyBuffer = []
        self.phrase = re.compile(r'www[.]acmetools[.]com')

    def keyPressEvent(self, event):
        self.keyBuffer.append(event.text())

        letters = "".join(self.keyBuffer)
        match = self.phrase.search(letters)
        if match:
            print("Hit!")
            self.keyBuffer = []


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
