# This Python file uses the following encoding: utf-8
import mysql.connector

class my_cruddb:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_perkantoran'  # ubah nama database sesuai kebutuhan kamu
        )

    # ===== CREATE =====
    def simpanPegawai(self, id, nama, status, noTelp):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO pegawai (IDPegawai, Nama, Status, Telp) VALUES (%s, %s, %s, %s)",
            (id, nama, status, noTelp)
        )
        self.conn.commit()
        cursor.close()

    # ===== UPDATE =====
    # Sekarang menerima original_id (WHERE) dan new_id (SET) agar ID bisa diubah juga
    def ubahPegawai(self, original_id, new_id, nama, status, noTelp):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE pegawai SET IDPegawai=%s, Nama=%s, Status=%s, Telp=%s WHERE IDPegawai=%s",
            (new_id, nama, status, noTelp, original_id)
        )
        self.conn.commit()
        cursor.close()

    # ===== DELETE =====
    def hapusPegawai(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM pegawai WHERE IDPegawai=%s", (id,))
        self.conn.commit()
        cursor.close()

    # ===== READ ALL =====
    def dataPegawai(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pegawai ORDER BY IDPegawai ASC")
        record = cursor.fetchall()
        cursor.close()
        return record

    # ===== SEARCH =====
    def CariPegawai(self, param):
        sql = """
        SELECT * FROM pegawai
        WHERE IDPegawai LIKE %s OR Nama LIKE %s OR Status LIKE %s OR Telp LIKE %s
        """
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, [f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = cursor.fetchall()
        cursor.close()
        return record
