# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

from crudDB import my_cruddb


class Pegawai(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== LOAD UI =====
        ui_file = QFile("pegawai.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPegawai = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()
        self.selected_id = None

        # ===== VALIDATOR =====
        # ID Pegawai → hanya angka
        self.formPegawai.editIDPegawai.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"\d+"))
        )

        # No Telepon → hanya angka, maksimal 12 digit
        self.formPegawai.editTelpon.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"\d{0,12}"))
        )

        # ===== SETTING TABEL =====
        tabel = self.formPegawai.tabelPegawai
        tabel.setSelectionBehavior(QTableWidget.SelectRows)
        tabel.setSelectionMode(QTableWidget.SingleSelection)
        tabel.setEditTriggers(QTableWidget.NoEditTriggers)
        tabel.verticalHeader().setVisible(False)

        # 🔥 HILANGKAN TITIK-TITIK (...)
        tabel.setTextElideMode(Qt.ElideNone)

        header = tabel.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # 🔥 KHUSUS kolom Telp → sesuaikan isi
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        tabel.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        tabel.cellClicked.connect(self.on_table_select)

        # ===== KONEKSI TOMBOL =====
        self.formPegawai.btnSimpan.clicked.connect(self.doSimpanPegawai)
        self.formPegawai.btnUbah.clicked.connect(self.doUbahPegawai)
        self.formPegawai.btnHapus.clicked.connect(self.doHapusPegawai)
        self.formPegawai.editCari.textChanged.connect(self.doCariPegawai)

        # ===== TOMBOL BERSIH =====
        if hasattr(self.formPegawai, "btnBersih"):
            self.formPegawai.btnBersih.clicked.connect(self.doBersih)

        self.tampilData()

    # ================= SIMPAN =================
    def doSimpanPegawai(self):
        if not self.formPegawai.editIDPegawai.text():
            QMessageBox.warning(None, "Peringatan", "ID Pegawai wajib diisi!")
            return
        if not self.formPegawai.editNama.text():
            QMessageBox.warning(None, "Peringatan", "Nama Pegawai wajib diisi!")
            return
        if not self.formPegawai.editTelpon.text():
            QMessageBox.warning(None, "Peringatan", "No Telepon wajib diisi!")
            return

        if QMessageBox.question(
            None, "Konfirmasi", "Simpan data pegawai?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:

            self.crud.simpanPegawai(
                self.formPegawai.editIDPegawai.text(),
                self.formPegawai.editNama.text(),
                self.formPegawai.comboStatus.currentText(),
                self.formPegawai.editTelpon.text()
            )

            QMessageBox.information(None, "Sukses", "Data berhasil disimpan")
            self.doBersih()
            self.tampilData()

    # ================= UBAH =================
    def doUbahPegawai(self):
        tabel = self.formPegawai.tabelPegawai
        row = tabel.currentRow()

        if row < 0 or not self.selected_id:
            QMessageBox.warning(None, "Peringatan", "Pilih satu baris tabel terlebih dahulu!")
            return

        new_id = self.formPegawai.editIDPegawai.text()
        new_nama = self.formPegawai.editNama.text()
        new_status = self.formPegawai.comboStatus.currentText()
        new_telp = self.formPegawai.editTelpon.text()

        if QMessageBox.question(
            None, "Konfirmasi", "Ubah data pegawai ini?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:

            self.crud.ubahPegawai(
                self.selected_id,
                new_id,
                new_nama,
                new_status,
                new_telp
            )

            tabel.setItem(row, 0, QTableWidgetItem(new_id))
            tabel.setItem(row, 1, QTableWidgetItem(new_nama))
            tabel.setItem(row, 2, QTableWidgetItem(new_status))
            tabel.setItem(row, 3, QTableWidgetItem(new_telp))

            self.selected_id = new_id
            QMessageBox.information(None, "Sukses", "Data berhasil diubah")

    # ================= HAPUS =================
    def doHapusPegawai(self):
        if not self.selected_id:
            QMessageBox.warning(None, "Peringatan", "Pilih satu baris tabel terlebih dahulu!")
            return

        if QMessageBox.question(
            None, "Konfirmasi", f"Hapus pegawai ID {self.selected_id}?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:

            self.crud.hapusPegawai(self.selected_id)
            QMessageBox.information(None, "Sukses", "Data berhasil dihapus")
            self.doBersih()
            self.tampilData()

    # ================= BERSIH =================
    def doBersih(self):
        self.formPegawai.editIDPegawai.clear()
        self.formPegawai.editNama.clear()
        self.formPegawai.editTelpon.clear()
        self.formPegawai.comboStatus.setCurrentIndex(0)

        self.selected_id = None
        self.formPegawai.tabelPegawai.clearSelection()
        self.formPegawai.editIDPegawai.setFocus()

    # ================= TAMPIL DATA =================
    def tampilData(self):
        data = self.crud.dataPegawai()
        tabel = self.formPegawai.tabelPegawai
        tabel.setRowCount(0)

        for r in data:
            row = tabel.rowCount()
            tabel.insertRow(row)
            tabel.setItem(row, 0, QTableWidgetItem(r["IDPegawai"]))
            tabel.setItem(row, 1, QTableWidgetItem(r["Nama"]))
            tabel.setItem(row, 2, QTableWidgetItem(r["Status"]))
            tabel.setItem(row, 3, QTableWidgetItem(r["Telp"]))

        # 🔥 PASTIKAN SEMUA ISI KELIHATAN
        tabel.resizeColumnsToContents()
        tabel.resizeRowsToContents()

    # ================= CARI =================
    def doCariPegawai(self):
        data = self.crud.CariPegawai(self.formPegawai.editCari.text())
        tabel = self.formPegawai.tabelPegawai
        tabel.setRowCount(0)

        for r in data:
            row = tabel.rowCount()
            tabel.insertRow(row)
            tabel.setItem(row, 0, QTableWidgetItem(r["IDPegawai"]))
            tabel.setItem(row, 1, QTableWidgetItem(r["Nama"]))
            tabel.setItem(row, 2, QTableWidgetItem(r["Status"]))
            tabel.setItem(row, 3, QTableWidgetItem(r["Telp"]))

        tabel.resizeColumnsToContents()

    # ================= PILIH TABEL =================
    def on_table_select(self, row, column):
        tabel = self.formPegawai.tabelPegawai

        self.selected_id = tabel.item(row, 0).text()
        self.formPegawai.editIDPegawai.setText(self.selected_id)
        self.formPegawai.editNama.setText(tabel.item(row, 1).text())
        self.formPegawai.comboStatus.setCurrentText(tabel.item(row, 2).text())
        self.formPegawai.editTelpon.setText(tabel.item(row, 3).text())
