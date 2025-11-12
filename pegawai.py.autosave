# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class Pegawai(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file = QFile("pegawai.ui")  # ubah file ui dari anggota.ui ke pegawai.ui
        ui_file.open(QFile.ReadOnly)

        # membuat object loader ui
        loader = QUiLoader()
        self.formPegawai = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        # koneksi tombol ke fungsi
        self.formPegawai.btnSimpan.clicked.connect(self.doSimpanPegawai)
        self.formPegawai.btnUbah.clicked.connect(self.doUbahPegawai)
        self.formPegawai.btnHapus.clicked.connect(self.doHapusPegawai)
        self.formPegawai.editCari.textChanged.connect(self.doCariPegawai)

        # tampilkan data awal
        self.tampilData()

    def doSimpanPegawai(self):
        if not self.formPegawai.editID.text().strip():
            QMessageBox.information(None, "Informasi", "ID Pegawai belum diisi")
            self.formPegawai.editID.setFocus()
        elif not self.formPegawai.editNama.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Pegawai belum diisi")
            self.formPegawai.editNama.setFocus()
        elif not self.formPegawai.comboStatus.currentText().strip():
            QMessageBox.information(None, "Informasi", "Status belum diisi")
            self.formPegawai.comboStatus.setFocus()
        elif not self.formPegawai.editTelpon.text().strip():
            QMessageBox.information(None, "Informasi", "Nomor Telepon belum diisi")
            self.formPegawai.editTelpon.setFocus()
        else:
            pesan = QMessageBox.information(
                None, "Informasi", "Apakah Anda yakin menyimpan data ini?",
                QMessageBox.Yes | QMessageBox.No
            )

            if pesan == QMessageBox.Yes:
                tempID = self.formPegawai.editID.text()
                tempNama = self.formPegawai.editNama.text()
                tempStatus = self.formPegawai.comboStatus.currentText()
                tempNoTelp = self.formPegawai.editTelpon.text()
                self.crud.simpanPegawai(tempID, tempNama, tempStatus, tempNoTelp)
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def doUbahPegawai(self):
        tempID = self.formPegawai.editID.text()
        tempNama = self.formPegawai.editNama.text()
        tempStatus = self.formPegawai.comboStatus.currentText()
        tempNoTelp = self.formPegawai.editTelpon.text()
        self.crud.ubahPegawai(tempID, tempNama, tempStatus, tempNoTelp)
        QMessageBox.information(None, "Informasi", "Data pegawai berhasil diubah")
        self.tampilData()

    def doHapusPegawai(self):
        tempID = self.formPegawai.editID.text()
        pesan = QMessageBox.question(None, "Konfirmasi", f"Hapus data pegawai ID {tempID}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            self.crud.hapusPegawai(tempID)
            QMessageBox.information(None, "Informasi", "Data pegawai berhasil dihapus")
            self.tampilData()

    def tampilData(self):
        baris = self.crud.dataPegawai()
        self.formPegawai.tabelPegawai.setRowCount(0)
        for r in baris:
            i = self.formPegawai.tabelPegawai.rowCount()
            self.formPegawai.tabelPegawai.insertRow(i)
            self.formPegawai.tabelPegawai.setItem(i, 0, QTableWidgetItem(r["IDPegawai"]))
            self.formPegawai.tabelPegawai.setItem(i, 1, QTableWidgetItem(r["Nama"]))
            self.formPegawai.tabelPegawai.setItem(i, 2, QTableWidgetItem(r["Status"]))
            self.formPegawai.tabelPegawai.setItem(i, 3, QTableWidgetItem(r["Telp"]))

    def doCariPegawai(self):
        cari = self.formPegawai.editCari.text()
        baris = self.crud.CariPegawai(cari)
        self.formPegawai.tabelPegawai.setRowCount(0)
        for r in baris:
            i = self.formPegawai.tabelPegawai.rowCount()
            self.formPegawai.tabelPegawai.insertRow(i)
            self.formPegawai.tabelPegawai.setItem(i, 0, QTableWidgetItem(r["IDPegawai"]))
            self.formPegawai.tabelPegawai.setItem(i, 1, QTableWidgetItem(r["Nama"]))
            self.formPegawai.tabelPegawai.setItem(i, 2, QTableWidgetItem(r["Status"]))
            self.formPegawai.tabelPegawai.setItem(i, 3, QTableWidgetItem(r["Telp"]))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Pegawai()
#     window.show()
#     sys.exit(app.exec())
