import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QRegularExpression, QTime, QDate
from PySide6.QtGui import QRegularExpressionValidator
from crudDB_Absen import my_cruddb_absen


class Absen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== LOAD UI =====
        ui_file = QFile("absen.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formAbsen = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb_absen()
        self.selected_id = None
        self.selected_row_data = None  # untuk cek perubahan

        # ===== VALIDATOR =====
        self.formAbsen.comboIDPegawai.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"\d+"))
        )

        # ===== ISI COMBO PEG =====
        self.isiComboPegawai()

        # ===== SETTING TABEL =====
        tabel = self.formAbsen.tabelPegawai
        tabel.setSelectionBehavior(QTableWidget.SelectRows)
        tabel.setSelectionMode(QTableWidget.SingleSelection)
        tabel.setEditTriggers(QTableWidget.NoEditTriggers)
        tabel.verticalHeader().setVisible(False)
        tabel.setTextElideMode(Qt.ElideNone)
        tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabel.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        tabel.cellClicked.connect(self.on_table_select)

        # ===== KONEKSI TOMBOL =====
        self.formAbsen.btnSimpan.clicked.connect(self.doSimpanAbsen)
        self.formAbsen.btnUbah.clicked.connect(self.doUbahAbsen)
        self.formAbsen.btnHapus.clicked.connect(self.doHapusAbsen)
        self.formAbsen.editCari.textChanged.connect(self.doCariAbsen)
        self.formAbsen.comboStatusAbsen.currentTextChanged.connect(self.cekStatusDisableJam)
        if hasattr(self.formAbsen, "btnBersih"):
            self.formAbsen.btnBersih.clicked.connect(self.doBersih)

        # ===== INISIAL DEFAULT =====
        self.doBersih()
        self.tampilData()

    # ===== HELPER =====
    def format_time(self, time_val):
        """Ubah None atau HH:MM:SS jadi HH:mm, bersihkan tanda ':' tambahan"""
        if time_val is None:
            return "00:00"
        # jika time_val sudah QTime
        if hasattr(time_val, "toString"):
            return time_val.toString("HH:mm")
        # jika datetime.time
        if hasattr(time_val, "strftime"):
            return time_val.strftime("%H:%M")
        # jika string
        t = str(time_val)
        if len(t) >= 5:
            return t[:5]
        return t

    def generate_random_id(self):
        """Buat IDAbsen 3 digit random"""
        return random.randint(100, 999)

    # ===== ISI COMBO PEG =====
    def isiComboPegawai(self):
        self.formAbsen.comboIDPegawai.clear()
        pegawai_list = self.crud.getAllPegawaiID()
        for idp in pegawai_list:
            self.formAbsen.comboIDPegawai.addItem(str(idp))

    # ===== CEK STATUS UNTUK JAM =====
    def cekStatusDisableJam(self, status):
        if status in ["Sakit", "Izin", "Alpha"]:
            self.formAbsen.editJamMasuk.setReadOnly(True)
            self.formAbsen.editJamKeluar.setReadOnly(True)
            self.formAbsen.editJamMasuk.setTime(QTime(0, 0))
            self.formAbsen.editJamKeluar.setTime(QTime(0, 0))
        else:
            self.formAbsen.editJamMasuk.setReadOnly(False)
            self.formAbsen.editJamKeluar.setReadOnly(False)

    # ===== SIMPAN =====
    def doSimpanAbsen(self):
        idAbsen = self.generate_random_id()
        idPegawai = self.formAbsen.comboIDPegawai.currentText()
        tanggal = self.formAbsen.editTanggal.date().toString("yyyy-MM-dd")
        jamMasuk = self.formAbsen.editJamMasuk.time().toString("HH:mm")
        jamKeluar = self.formAbsen.editJamKeluar.time().toString("HH:mm")
        status = self.formAbsen.comboStatusAbsen.currentText()

        if not idPegawai or not tanggal:
            QMessageBox.warning(None, "Peringatan", "ID Pegawai dan Tanggal wajib diisi!")
            return

        if not self.crud.cekPegawai(idPegawai):
            QMessageBox.warning(None, "Error", f"ID Pegawai {idPegawai} tidak ada di database!")
            return

        if QMessageBox.question(None, "Konfirmasi", "Simpan data absen?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.crud.simpanAbsen(idAbsen, idPegawai, tanggal, jamMasuk, jamKeluar, status)
            QMessageBox.information(None, "Sukses", "Data berhasil disimpan")
            self.doBersih()
            self.tampilData()

    # ===== UBAH =====
    def doUbahAbsen(self):
        if not self.selected_id:
            QMessageBox.warning(None, "Peringatan", "Pilih satu baris tabel terlebih dahulu!")
            return

        # Ambil nilai sekarang
        idPegawai = self.formAbsen.comboIDPegawai.currentText()
        tanggal = self.formAbsen.editTanggal.date().toString("yyyy-MM-dd")
        jamMasuk = self.formAbsen.editJamMasuk.time().toString("HH:mm")
        jamKeluar = self.formAbsen.editJamKeluar.time().toString("HH:mm")
        status = self.formAbsen.comboStatusAbsen.currentText()

        # ===== CEK PERUBAHAN =====
        if (self.selected_row_data and
            self.selected_row_data["IDPegawai"] == idPegawai and
            self.selected_row_data["Tanggal"] == tanggal and
            self.selected_row_data["JamMasuk"] == jamMasuk and
            self.selected_row_data["JamKeluar"] == jamKeluar and
            self.selected_row_data["StatusAbsen"] == status):
            QMessageBox.warning(None, "Peringatan", "Data belum diubah!")
            return

        if QMessageBox.question(None, "Konfirmasi", "Ubah data absen ini?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.crud.ubahAbsen(self.selected_id, idPegawai, tanggal, jamMasuk, jamKeluar, status)
            QMessageBox.information(None, "Sukses", "Data berhasil diubah")
            self.tampilData()

    # ===== HAPUS =====
    def doHapusAbsen(self):
        if not self.selected_id:
            QMessageBox.warning(None, "Peringatan", "Pilih satu baris tabel terlebih dahulu!")
            return

        if QMessageBox.question(None, "Konfirmasi", f"Hapus absen ID {self.selected_id}?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.crud.hapusAbsen(self.selected_id)
            QMessageBox.information(None, "Sukses", "Data berhasil dihapus")
            self.doBersih()
            self.tampilData()

    # ===== BERSIH =====
    def doBersih(self):
        self.isiComboPegawai()
        self.formAbsen.editTanggal.setDate(QDate.currentDate())
        # default jam masuk/keluar = 00:00
        self.formAbsen.editJamMasuk.setTime(QTime(0, 0))
        self.formAbsen.editJamKeluar.setTime(QTime(0, 0))
        self.formAbsen.comboStatusAbsen.setCurrentIndex(0)
        self.selected_id = None
        self.selected_row_data = None
        self.formAbsen.tabelPegawai.clearSelection()
        self.formAbsen.comboIDPegawai.setFocus()
        self.cekStatusDisableJam(self.formAbsen.comboStatusAbsen.currentText())

    # ===== TAMPIL DATA =====
    def tampilData(self, data=None):
        if data is None:
            data = self.crud.dataAbsen()
        tabel = self.formAbsen.tabelPegawai
        tabel.setRowCount(0)
        for r in data:
            row = tabel.rowCount()
            tabel.insertRow(row)
            tabel.setItem(row, 0, QTableWidgetItem(str(r["IDAbsen"])))
            tabel.setItem(row, 1, QTableWidgetItem(str(r["IDPegawai"])))
            tanggal_str = (
                r["Tanggal"].strftime("%Y-%m-%d") if hasattr(r["Tanggal"], "strftime") else str(r["Tanggal"])
            )
            tabel.setItem(row, 2, QTableWidgetItem(tanggal_str))
            tabel.setItem(row, 3, QTableWidgetItem(self.format_time(r["JamMasuk"])))
            tabel.setItem(row, 4, QTableWidgetItem(self.format_time(r["JamKeluar"])))
            tabel.setItem(row, 5, QTableWidgetItem(str(r["StatusAbsen"])))
        tabel.resizeColumnsToContents()
        tabel.resizeRowsToContents()

    # ===== CARI =====
    def doCariAbsen(self):
        param = self.formAbsen.editCari.text()
        data = self.crud.cariAbsen(param)
        self.tampilData(data)

    # ===== PILIH TABEL =====
    def on_table_select(self, row, column):
        tabel = self.formAbsen.tabelPegawai
        self.selected_id = tabel.item(row, 0).text()
        idPegawai = tabel.item(row, 1).text()
        tanggal = tabel.item(row, 2).text()
        jamMasuk = tabel.item(row, 3).text()
        jamKeluar = tabel.item(row, 4).text()
        status = tabel.item(row, 5).text()

        self.selected_row_data = {
            "IDPegawai": idPegawai,
            "Tanggal": tanggal,
            "JamMasuk": jamMasuk,
            "JamKeluar": jamKeluar,
            "StatusAbsen": status
        }

        self.formAbsen.comboIDPegawai.setCurrentText(idPegawai)
        date_parts = tanggal.split("-")
        self.formAbsen.editTanggal.setDate(QDate(int(date_parts[0]), int(date_parts[1]), int(date_parts[2])))
        self.formAbsen.editJamMasuk.setTime(QTime.fromString(jamMasuk, "HH:mm"))
        self.formAbsen.editJamKeluar.setTime(QTime.fromString(jamKeluar, "HH:mm"))
        self.formAbsen.comboStatusAbsen.setCurrentText(status)
        self.cekStatusDisableJam(status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Absen()
    window.show()
    sys.exit(app.exec())
