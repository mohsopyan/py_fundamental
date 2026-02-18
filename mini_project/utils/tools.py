def sapa_user(nama:str):
    return f"Halo {nama}, Selamat datang di sistem backend"

def hitung_pajak(harga: int):
    try:
        return harga * 0.1
    except TypeError:
        return "Error: Harga harus berupa angka (int/float)!"

def cek_akses(level: int):
    try:
        if level > 5:
            return True
        else:
            return False
    except (TypeError, Exception):
        print("Log: Input level tidak valid!")
        return False
    finally:
        print("Pengecekan selesai.")
    
def daftar_user(username:str, email:str):
    hasil = {
        "nama": username,
        "email": email
    }
    return hasil