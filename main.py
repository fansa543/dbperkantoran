# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from pegawai import Pegawai  # ubah dari 'anggota' ke 'pegawai'


class HalamanUtama(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # variabel untuk menampung file main.ui
        file_form_utama = QFile("main.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        file_form_utama.open(QFile.ReadOnly)
        # membuat objek loader Ui
        form_loader = QUiLoader()
        self.form_utama = form_loader.load(file_form_utama, self)
        self.setMenuBar(self.form_utama.menuBar())
        self.resize(self.form_utama.size())

        # ubah menu trigger menjadi actionForm_Pegawai
        self.form_utama.actionForm_Pegawai.triggered.connect(self.buka_pegawai)

    def buka_pegawai(self):
        self.form_pegawai = Pegawai()
        self.form_pegawai.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = HalamanUtama()
    widget.show()
    sys.exit(app.exec())
