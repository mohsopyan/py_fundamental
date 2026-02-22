# 🚀 User Management System v1.0

Sistem manajemen user berbasis Python yang mengintegrasikan data lokal (JSON) dan data eksternal (REST API). Proyek ini menunjukkan implementasi fundamental backend, OOP, dan integrasi sistem.

## ✨ Fitur Utama

### 1. Advanced OOP Architecture
- **Base Class `User`**: Standarisasi entitas user dengan enkapsulasi data.
- **Inheritance**: Class `Admin` dengan kapabilitas khusus (kode akses & penghapusan data).
- **Polymorphism**: Method `.sapa()` yang berperilaku berbeda antar role.

### 2. Smart Integration & Persistence
- **External API Consumption**: Menarik data user secara dinamis dari `jsonplaceholder` menggunakan library `requests`.
- **Data Hydration**: Secara otomatis mengubah data mentah (JSON) menjadi objek cerdas (Class Instance).
- **Persistence**: Penyimpanan data permanen ke dalam file `database.json`.

### 3. Professional Standards
- **Interactive CLI**: Antarmuka menu di terminal untuk pengalaman pengguna yang intuitif.
- **Robustness**: Penanganan error pada kegagalan koneksi internet dan validasi tipe data input.
- **Modular Code**: Pemisahan tanggung jawab yang jelas antara `models`, `tools`, dan `logic`.

## 📁 Struktur Proyek
```text
user_management_app/
├── main.py              # Entry point & Menu Logic
├── database.json        # Local Storage
├── requirements.txt     # Daftar Dependencies
└── utils/
    ├── models.py        # Blueprints (User & Admin)
    └── tools.py         # API & File Helpers
```

## Cara Menjalankan
### 1. Clone Repositori
```bash
git clone [https://github.com/mohsopyan/py_fundamental.git](https://github.com/mohsopyan/py_fundamental.git)
cd user_management_app
```

### 2. Instal Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
``` bash
python main.py
```

## 🛠️ Tech Stack
- **Language**: Python 3.13+
- **Library**: `requests` (API Handling), `json` (Storage)