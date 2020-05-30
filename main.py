import sys
import os
from PySide2 import QtCore
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.quitButton.clicked.connect(app.exit)
        self.resetButton.clicked.connect(self.reset)
        self.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)

        self.bossHealth.setMinimum(0)
        self.bossHealth.setMaximum(100)
        self.bossHealth.setValue(0)

        # game loop timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.gameEvents)
        self.timer.start()

    def keyPressEvent(self, event):
        if event.key() != QtCore.Qt.Key_Return and event.key() != QtCore.Qt.Key_Enter:
            return

        if self.bossHealth.value() < 100:
            self.bossHealth.setValue(self.bossHealth.value() + 25)
            print("Hit!")

    def gameEvents(self):
        if self.bossHealth.value() >= 100:
            return

        """
        Since this is developed on a machine without IR, we
        will swallow the error.
        """
        try:
            os.system("irsend SEND_ONCE NERFBLUE KEY_2")
        except:
            pass

    def reset(self):
        self.bossHealth.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
