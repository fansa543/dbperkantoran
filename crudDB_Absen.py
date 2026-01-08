import mysql.connector
from datetime import datetime, time

class my_cruddb_absen:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_perkantoran'
        )

    # ===== CREATE =====
    def simpanAbsen(self, idAbsen, idPegawai, tanggal, jamMasuk, jamKeluar, status):
        # Pastikan jamMasuk & jamKeluar format HH:mm
        jamMasuk_str = self._format_jam(jamMasuk)
        jamKeluar_str = self._format_jam(jamKeluar)

        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO absen
            (IDAbsen, IDPegawai, Tanggal, JamMasuk, JamKeluar, StatusAbsen)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (idAbsen, idPegawai, tanggal, jamMasuk_str, jamKeluar_str, status)
        )
        self.conn.commit()
        cursor.close()

    # ===== UPDATE =====
    def ubahAbsen(self, idAbsen, idPegawai, tanggal, jamMasuk, jamKeluar, status):
        jamMasuk_str = self._format_jam(jamMasuk)
        jamKeluar_str = self._format_jam(jamKeluar)

        cursor = self.conn.cursor()
        cursor.execute(
            """
            UPDATE absen
            SET IDPegawai=%s,
                Tanggal=%s,
                JamMasuk=%s,
                JamKeluar=%s,
                StatusAbsen=%s
            WHERE IDAbsen=%s
            """,
            (idPegawai, tanggal, jamMasuk_str, jamKeluar_str, status, idAbsen)
        )
        self.conn.commit()
        cursor.close()

    # ===== DELETE =====
    def hapusAbsen(self, idAbsen):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM absen WHERE IDAbsen=%s", (idAbsen,))
        self.conn.commit()
        cursor.close()

    # ===== READ ALL =====
    def dataAbsen(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT
                a.IDAbsen,
                a.IDPegawai,
                a.Tanggal,
                DATE_FORMAT(a.JamMasuk, '%H:%i') AS JamMasuk,
                DATE_FORMAT(a.JamKeluar, '%H:%i') AS JamKeluar,
                a.StatusAbsen
            FROM absen a
            ORDER BY a.Tanggal DESC, a.JamMasuk ASC
            """
        )
        record = cursor.fetchall()
        cursor.close()
        return record

    # ===== SEARCH =====
    def cariAbsen(self, param):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT
                a.IDAbsen,
                a.IDPegawai,
                a.Tanggal,
                DATE_FORMAT(a.JamMasuk, '%H:%i') AS JamMasuk,
                DATE_FORMAT(a.JamKeluar, '%H:%i') AS JamKeluar,
                a.StatusAbsen
            FROM absen a
            WHERE
                a.IDAbsen LIKE %s OR
                a.IDPegawai LIKE %s OR
                a.Tanggal LIKE %s OR
                a.StatusAbsen LIKE %s
            ORDER BY a.Tanggal DESC, a.JamMasuk ASC
            """,
            (f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%")
        )
        record = cursor.fetchall()
        cursor.close()
        return record

    # ===== CEK ID PEGAWAI VALID =====
    def cekPegawai(self, idPegawai):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT IDPegawai FROM pegawai WHERE IDPegawai=%s", (idPegawai,))
        result = cursor.fetchone()
        cursor.close()
        return bool(result)

    # ===== AMBIL SEMUA ID PEGAWAI =====
    def getAllPegawaiID(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT IDPegawai FROM pegawai")
        ids = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return ids

    # ===== HELPER FORMAT JAM =====
    def _format_jam(self, jam_str):
        """Pastikan jamMasuk/jamKeluar selalu HH:mm"""
        if isinstance(jam_str, str):
            # Jika string HH:mm:ss, ambil HH:mm
            parts = jam_str.split(":")
            return f"{int(parts[0]):02d}:{int(parts[1]):02d}"
        elif isinstance(jam_str, time):
            return jam_str.strftime("%H:%M")
        return "00:00"
