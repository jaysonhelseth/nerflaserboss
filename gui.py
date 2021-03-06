# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'g.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"#MainWindow {\n"
"	background-color: rgb(46, 52, 54);\n"
"	background-image: url(\"tron-wallpaper.jpg\");\n"
"	background-position: center;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bossHealth = QProgressBar(self.centralwidget)
        self.bossHealth.setObjectName(u"bossHealth")
        self.bossHealth.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(78, 154, 6);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(164, 0, 0);\n"
"}")
        self.bossHealth.setValue(24)
        self.bossHealth.setTextVisible(False)
        self.bossHealth.setInvertedAppearance(False)

        self.verticalLayout_2.addWidget(self.bossHealth)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(100, 50))
        self.resetButton.setStyleSheet(u"#resetButton {\n"
"	background-color: rgb(0, 255, 255)\n"
"}")

        self.verticalLayout.addWidget(self.resetButton)

        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setMinimumSize(QSize(100, 50))
        self.quitButton.setStyleSheet(u"#quitButton {\n"
"	background-color: rgb(0, 255, 255)\n"
"}")

        self.verticalLayout.addWidget(self.quitButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

