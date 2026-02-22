# 🐍 My Python Journey: From Zero to Backend Engineer

Jurnal ini mendokumentasikan proses belajar Python saya mulai dari nol, fokus pada logika backend dan standarisasi kode.

## 📊 Ringkasan Belajar (Log)

| Hari | Topik Utama | Key Tools / Fungsi | Status |
| :--- | :--- | :--- | :--- |
| 1 | Setup & Output | `print()`, VS Code Interpreter | ✅ Berhasil |
| 2 | Variabel | `f-string`, Variable Naming | ✅ Berhasil |
| 3 | Tipe Data & Casting | `type()`, `int()`, `str()`, `bool` | ✅ Berhasil |
| 4 | Input & Operator | `input()`, `*`, `//`, `%` | ✅ Berhasil |
| 5 | String Manipulation | .upper(), .title(), len(), in | ✅ Selesai |
| 6 | Percabangan Logic | and, or, if-elif-else | ✅ Berhasil |
| 7 | Nested IF | if inside if (Logic levels) | ✅ Berhasil |
| 8 | For Loop | for, range() | ✅ Berhasil |
| 9 | While Loop | while, Conditionals | ✅ Berhasil |
| 10 | Nested Loop & Menu | while True, break | ✅ Selesai |
| 11 | Python List(Basic) | append(), len(), indexing | ✅ Berhasil |
| 12 | List Slicing & Sorting | .sort(), [start:stop], sum() | ✅ Berhasil |
| 13 | Tuple (Immutable) | (value1, value2) | ✅ Berhasil |
| 14 | Dictionary | {key: value}, del, update | ✅ Berhasil |
| 15 | Function | def, return, parameters, scope | ✅ Berhasil |
| 15 | Pro Function | Type Hinting, Default Params | ✅ Berhasil |
| 16 | Dynamic Arguments | *args, **kwargs | ✅ Berhasil |
| 17 | Modules | import, from ... import | ✅ Berhasil |
| 18 | Object Oriented (OOP) | class, __init__, self | ✅ Berhasil |
| 19 | Inheritance & Overriding | super(), Child Class | ✅ Berhasil |
| 20 | Reliability (Error Handling) | try, except, isintance() | ✅ Berhasil |
| 21 | Data Persistence | json.dump(), json.load() | ✅ Berhasil |
| 22 | External Integration (API) | requests, get(), Hydration | ✅ Berhasil |

---

## 💡 Pelajaran Penting (Key Takeaways)

### 🔹 Fondasi & String
- **Interpreter:** Mesin "penerjemah" Python di VS Code (Set via `Ctrl+Shift+P`).
- **F-String:** Cara termudah menggabungkan teks dan variabel: `f"Halo {nama}"`.
- **String Methods:** - `.upper()` (Kapital semua), `.title()` (Besar di awal kata).
    - `len()` (Hitung panjang karakter), `in` (Cek keberadaan kata).

### 🔹 Penanganan Error & Logika
- **Casting:** Ingat bahwa `input()` selalu menghasilkan String. Gunakan `int()` untuk angka.
- **Math Operators:** `/` (Desimal), `//` (Bulat), `%` (Sisa bagi).
- **Logical Operators:** - `if-elif-else`: Mengambil keputusan berdasarkan kondisi.
    - `and`: Semua syarat harus benar.
    - `or`: Salah satu syarat benar sudah cukup.
- **Nested IF (Logika Bersarang)**
    - Digunakan untuk validasi bertahap.
    - Blok kode di dalam `if` kedua harus memiliki indentasi ekstra (2x Tab/4x Spasi).
    - Struktur: Mengecek kondisi luar dulu, baru masuk ke kondisi dalam.

### 🔹 Perulangan (Looping)
- **For Loop:** Digunakan untuk mengulang kode dengan jumlah yang sudah ditentukan.
- **Fungsi range(start, stop, step):** - `start`: Angka awal (inklusif).
    - `stop`: Batas akhir (eksklusif, angka ini tidak akan dicetak).
    - `step`: Jarak/lompatan antar angka (misal: lompat 2 untuk angka genap).
- **Modulo (%) dalam Loop:** Sangat berguna untuk memfilter angka (contoh: `i % 2 == 0` untuk mencari angka genap).

### 🔹 While Loop (Perulangan Dinamis)
- Digunakan saat jumlah perulangan tidak diketahui secara pasti.
- **Kondisi Berhenti:** Harus ada perubahan variabel di dalam loop agar tidak terjadi *Infinite Loop*.
- **Break:** Perintah untuk keluar paksa dari perulangan.
- **Continue:** Melewati sisa baris kode dan lanjut ke putaran loop berikutnya.

### 🔹 Object Oriented Programming (OOP)
- **Class vs Object:** Class adalah cetakan(blueprint), Object adalah hasil cetakannya.
- **Inheritance:** Mewariskan sifat dari Parent Class ke Child Class (misal: `Admin` mewarisi `User`) untuk menghindari pengulangan kode.
- **Method Overriding:** Mengubah cara kerja fungsi bawaan Parent Class di dalam Child Class agar lebih spesifik.

### 🔹 Backend Reliability & Persistence
- **Error Handling:** Mencegah aplikasi mati total saat terjadi kesalahan (seperti internet putus atau file hilang).
- **JSON Handling:** Standar industri untuk menyimpan data.
    - **Serialization:** Object -> JSON.
    - **Hydration:** JSON -> Objek pintar (Class Instance).
- **Isintance:** Mengecek identitas objek secara aman sebelum menjalankan perintah khusus (Type Checking).

### 🔹 External Integartion
-- **API Request:** Mengambil data dari server lain menggunakan `requests.get()`.
-- **Status Codes:** Selalu gunakan `raise_for_status()` untuk memastikan data yang diambil valid dan server tujuan tidak error.

### 🔹 Best Practices
- **Indentasi:** Spasi/Tab setelah tanda titik dua `:` pada `if` adalah wajib untuk menentukan blok kode.
- **Git Flow:** Selalu cek `git status` sebelum `add`, `commit`, dan `push`.

### 🔹 Masalah & Solusi
- **TypeError:** Muncul jika mencampur `str` dan `int`. Solusi: Ubah salah satu tipe datanya agar seragam.