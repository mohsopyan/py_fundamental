nilai = [85, 92, 70, 88,  76, 95, 60, 82]

# --- 1. SORTING ---
# Mengurutkan dari terkecil ke terbesar
nilai.sort()
print(f"Urutan nilai (rendah ke tinggi): {nilai}")

# Mengurutkan dari terbesar ke terkecil (Descending)
nilai.sort(reverse=True)
print(f"Urutan nilai (tinggi ke rendah): {nilai}")

# --- 2. SLICING ---
# Mengambil 3 nilai tertinggi (Top 3)
top_3 = nilai[0:3]
print(f"Siswa Terbaik (Top 3): {top_3}")

# Mengambil nilai dari urutan ke-4 sampai terakhir
sisanya = nilai[3:]
print(f"Siswa lainnya: {sisanya}")