# 1. Fungsi tanpa timbal balik (Hanya menjalankan aksi)
def sapa_user(nama):
    print(f"Halo {nama}, selamat datang di sistem Backend!")

# 2. Fungsi dengan return (Mengembalikan hasil perhitungan)
def hitung_persen(skor, total):
    hasil = (skor / total) * 100
    return hasil

# --- Cara memanggil ---
sapa_user("Moyan")

skor_ai = hitung_persen(45, 50)
print(f"Akurasi Model: {skor_ai}%")