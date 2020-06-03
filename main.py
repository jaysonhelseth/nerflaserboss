import sys
import os
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.quitButton.clicked.connect(self.quit)
        self.resetButton.clicked.connect(self.reset)
        self.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)

        self.bossHealth.setMinimum(0)
        self.bossHealth.setMaximum(100)
        self.bossHealth.setValue(0)
        self.start_shoot()

    def keyPressEvent(self, event):
        if event.key() != QtCore.Qt.Key_Return and event.key() != QtCore.Qt.Key_Enter:
            return

        if self.bossHealth.value() < 100:
            self.bossHealth.setValue(self.bossHealth.value() + 25)

        if self.bossHealth.value() >= 100:
            self.stop_shoot()

    def reset(self):
        self.stop_shoot()
        self.bossHealth.setValue(0)
        self.start_shoot()

    def start_shoot(self):
        os.system('tmux new -d -s shoot "./shoot.sh"')

    def stop_shoot(self):
        os.system('tmux kill-session -t shoot')

    def quit(self):
        self.stop_shoot()
        app.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
