class User:
    def __init__(self, nama: str, email: str, level: int = 1):
        self.nama = nama
        self.email = email

        try:
            self.level = int(level)
        except ValueError:
            self.level = 1
            print(f"Peringatan: Level untuk {nama} tidak valid, diset ke 1")
            
    def sapa(self):
        return f"Halo, saya {self.nama}, Email saya {self.email}."
    
    def cek_status_akses(self):
        if self.level > 5:
            return f"User {self.nama} memilik akses EXPERT."
        else:
            return f"User {self.nama} hanya memiliki akses STANDARD."
        
class Admin(User):
    def __init__(self, nama: str, email: str, level: int = 10, kode_akses: str = "DEFAULT_ADMIN"):
        super().__init__(nama, email, level)
        self.kode_akses = kode_akses

    def hapus_data(self):
        return f"Admin {self.nama} menggunakan kode {self.kode_akses} untuk hapus data."
    
    def sapa(self):
        return f"DASHBOARD ADMIN: Selamat datang, Commander {self.nama}."