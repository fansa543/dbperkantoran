# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionForm_Pegawai = QAction(main)
        self.actionForm_Pegawai.setObjectName(u"actionForm_Pegawai")
        self.actionForm_DVD = QAction(main)
        self.actionForm_DVD.setObjectName(u"actionForm_DVD")
        self.actionForm_Admin = QAction(main)
        self.actionForm_Admin.setObjectName(u"actionForm_Admin")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 17))
        self.menuHalaman_Aplikasi = QMenu(self.menubar)
        self.menuHalaman_Aplikasi.setObjectName(u"menuHalaman_Aplikasi")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHalaman_Aplikasi.menuAction())
        self.menuHalaman_Aplikasi.addAction(self.actionForm_Pegawai)
        self.menuHalaman_Aplikasi.addAction(self.actionForm_DVD)
        self.menuHalaman_Aplikasi.addAction(self.actionForm_Admin)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionForm_Pegawai.setText(QCoreApplication.translate("main", u"Form Pegawai", None))
        self.actionForm_DVD.setText(QCoreApplication.translate("main", u"Form Departemen", None))
        self.actionForm_Admin.setText(QCoreApplication.translate("main", u"Form Admin", None))
        self.menuHalaman_Aplikasi.setTitle(QCoreApplication.translate("main", u"Halaman Aplikasi", None))
    # retranslateUi

