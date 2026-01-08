# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Absen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTimeEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 387)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 20, 331, 177))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.IDPegawai = QLabel(self.formLayoutWidget)
        self.IDPegawai.setObjectName(u"IDPegawai")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.IDPegawai)

        self.Absen = QLabel(self.formLayoutWidget)
        self.Absen.setObjectName(u"Absen")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Absen)

        self.editIDAbsen = QLineEdit(self.formLayoutWidget)
        self.editIDAbsen.setObjectName(u"editIDAbsen")
        self.editIDAbsen.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIDAbsen)

        self.Tanggal = QLabel(self.formLayoutWidget)
        self.Tanggal.setObjectName(u"Tanggal")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.Tanggal)

        self.editTanggal = QDateEdit(self.formLayoutWidget)
        self.editTanggal.setObjectName(u"editTanggal")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editTanggal)

        self.Jammasuk = QLabel(self.formLayoutWidget)
        self.Jammasuk.setObjectName(u"Jammasuk")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.Jammasuk)

        self.editJamMasuk = QTimeEdit(self.formLayoutWidget)
        self.editJamMasuk.setObjectName(u"editJamMasuk")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editJamMasuk)

        self.Jamkeluar = QLabel(self.formLayoutWidget)
        self.Jamkeluar.setObjectName(u"Jamkeluar")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.Jamkeluar)

        self.editJamKeluar = QTimeEdit(self.formLayoutWidget)
        self.editJamKeluar.setObjectName(u"editJamKeluar")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editJamKeluar)

        self.Status = QLabel(self.formLayoutWidget)
        self.Status.setObjectName(u"Status")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.Status)

        self.comboStatusAbsen = QComboBox(self.formLayoutWidget)
        self.comboStatusAbsen.addItem("")
        self.comboStatusAbsen.addItem("")
        self.comboStatusAbsen.addItem("")
        self.comboStatusAbsen.addItem("")
        self.comboStatusAbsen.setObjectName(u"comboStatusAbsen")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.comboStatusAbsen)

        self.comboIDPegawai = QComboBox(self.formLayoutWidget)
        self.comboIDPegawai.setObjectName(u"comboIDPegawai")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboIDPegawai)

        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(200, 210, 161, 20))
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(30, 210, 151, 20))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(30, 230, 151, 20))
        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(200, 230, 161, 20))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(30, 260, 331, 20))
        self.tabelPegawai = QTableWidget(Form)
        if (self.tabelPegawai.columnCount() < 6):
            self.tabelPegawai.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabelPegawai.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabelPegawai.setObjectName(u"tabelPegawai")
        self.tabelPegawai.setEnabled(True)
        self.tabelPegawai.setGeometry(QRect(10, 290, 381, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.IDPegawai.setText(QCoreApplication.translate("Form", u"ID Pegawai", None))
        self.Absen.setText(QCoreApplication.translate("Form", u"ID Absen", None))
        self.Tanggal.setText(QCoreApplication.translate("Form", u"Tanggal", None))
        self.Jammasuk.setText(QCoreApplication.translate("Form", u"Jam Masuk", None))
        self.Jamkeluar.setText(QCoreApplication.translate("Form", u"Jam Keluar", None))
        self.Status.setText(QCoreApplication.translate("Form", u"Status", None))
        self.comboStatusAbsen.setItemText(0, QCoreApplication.translate("Form", u"Hadir", None))
        self.comboStatusAbsen.setItemText(1, QCoreApplication.translate("Form", u"Sakit", None))
        self.comboStatusAbsen.setItemText(2, QCoreApplication.translate("Form", u"Izin", None))
        self.comboStatusAbsen.setItemText(3, QCoreApplication.translate("Form", u"Alpha", None))

        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        ___qtablewidgetitem = self.tabelPegawai.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"IDAbsen", None));
        ___qtablewidgetitem1 = self.tabelPegawai.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"IDPegawai", None));
        ___qtablewidgetitem2 = self.tabelPegawai.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tanggal", None));
        ___qtablewidgetitem3 = self.tabelPegawai.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jam Masuk", None));
        ___qtablewidgetitem4 = self.tabelPegawai.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Jam Keluar", None));
        ___qtablewidgetitem5 = self.tabelPegawai.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Status", None));
    # retranslateUi

