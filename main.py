import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from pegawai import Pegawai
from Absen import Absen  # huruf kecil sesuai nama file

class HalamanUtama(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # load main.ui
        file_form_utama = QFile("main.ui")
        file_form_utama.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form_utama = loader.load(file_form_utama, self)
        file_form_utama.close()

        self.setMenuBar(self.form_utama.menuBar())
        self.resize(self.form_utama.size())

        # ===== MENU TRIGGER =====
        self.form_utama.actionForm_Pegawai.triggered.connect(self.buka_pegawai)
        self.form_utama.actionForm_Absen.triggered.connect(self.buka_absen)

    # ===== BUKA FORM PEGAWAI =====
    def buka_pegawai(self):
        self.form_pegawai = Pegawai()
        self.form_pegawai.show()

    # ===== BUKA FORM ABSEN =====
    def buka_absen(self):
        self.form_absen = Absen()
        self.form_absen.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HalamanUtama()
    window.show()
    sys.exit(app.exec())
