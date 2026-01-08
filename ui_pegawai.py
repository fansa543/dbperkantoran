# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pegawai.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(371, 365)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 301, 102))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPegawaiLabel = QLabel(self.formLayoutWidget)
        self.iDPegawaiLabel.setObjectName(u"iDPegawaiLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPegawaiLabel)

        self.editIDPegawai = QLineEdit(self.formLayoutWidget)
        self.editIDPegawai.setObjectName(u"editIDPegawai")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editIDPegawai)

        self.namaLabel = QLabel(self.formLayoutWidget)
        self.namaLabel.setObjectName(u"namaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.comboStatus = QComboBox(self.formLayoutWidget)
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.setObjectName(u"comboStatus")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboStatus)

        self.noTeleponLabel = QLabel(self.formLayoutWidget)
        self.noTeleponLabel.setObjectName(u"noTeleponLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.noTeleponLabel)

        self.editTelpon = QLineEdit(self.formLayoutWidget)
        self.editTelpon.setObjectName(u"editTelpon")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTelpon)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 120, 141, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(10, 140, 141, 20))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(170, 120, 141, 20))
        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(170, 140, 141, 20))
        self.tabelPegawai = QTableWidget(Form)
        if (self.tabelPegawai.columnCount() < 4):
            self.tabelPegawai.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelPegawai.setObjectName(u"tabelPegawai")
        self.tabelPegawai.setEnabled(True)
        self.tabelPegawai.setGeometry(QRect(10, 200, 301, 192))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 170, 301, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPegawaiLabel.setText(QCoreApplication.translate("Form", u"ID Pegawai", None))
        self.namaLabel.setText(QCoreApplication.translate("Form", u"Nama Pegawai", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Status Pegawai", None))
        self.comboStatus.setItemText(0, QCoreApplication.translate("Form", u"Tetap", None))
        self.comboStatus.setItemText(1, QCoreApplication.translate("Form", u"Kontrak", None))
        self.comboStatus.setItemText(2, QCoreApplication.translate("Form", u"Magang", None))
        self.comboStatus.setItemText(3, QCoreApplication.translate("Form", u"Outsourcing", None))

        self.noTeleponLabel.setText(QCoreApplication.translate("Form", u"No Telepon", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        ___qtablewidgetitem = self.tabelPegawai.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"IDPegawai", None));
        ___qtablewidgetitem1 = self.tabelPegawai.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tabelPegawai.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Status", None));
        ___qtablewidgetitem3 = self.tabelPegawai.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"No Telpon", None));
    # retranslateUi

