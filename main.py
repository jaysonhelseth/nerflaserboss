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
        self.resetButton.clicked.connect(self.reset)
        # self.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)
        self.keyBuffer = []
        self.phrase = re.compile(r'www[.]acmetools[.]com')

        self.bossHealth.setMinimum(0)
        self.bossHealth.setMaximum(100)
        self.bossHealth.setValue(0)

    def keyPressEvent(self, event):
        self.keyBuffer.append(event.text())

        letters = "".join(self.keyBuffer)
        match = self.phrase.search(letters)
        if match and self.bossHealth.value() < 100:
            self.bossHealth.setValue(self.bossHealth.value() + 25)
            print("Hit!")
            self.keyBuffer = []

    def reset(self):
        self.bossHealth.setValue(0)
        self.keyBuffer = []


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
