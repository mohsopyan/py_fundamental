import os
from utils.models import User, Admin
from utils.tools import simpan_data, muat_data, ambil_data_internet

def hydrate_data(data_list):
    """Fungsi cerdas untuk mengubah data mentah (dict) menjadi object (Class)"""
    objects = []
    for item in data_list:
        if 'kode_akses' in item:
            obj = Admin(
                nama=item.get('nama'),
                email=item.get('email'),
                level=item.get('level', 10),
                kode_akses=item.get('kode_akses')
            )
        else:
            # Mapping: API internet pake 'name', databse lokal pake 'nama'
            nama = item.get('nama') or item.get('name')
            obj = User(
                nama=nama,
                email=item.get('email'),
                level=item.get('level', 1)
            )
        objects.append(obj)
    return objects

def main():
    print("⏳ Memuat sistem...")
    data_mentah = muat_data()
    semua_user = hydrate_data(data_mentah)

    while True:
        print("\n" + "="*30)
        print("USER MANAGEMENT SYSTEM v1.0")
        print("="*30)
        print(f"Status: {len(semua_user)} User Termuat")
        print("1. Lihat Semua User")
        print("2. Tarik Data User dari API Internet")
        print("3. Simpan Perubahan ke Database")
        print("4. Keluar")

        pilihan = input("\nPilih menu (1-4): ")

        if pilihan == "1":
            print(f"\n--- DAFTAR USER ({len(semua_user)}) ---")
            for u in semua_user:
                print(u.sapa())
                if isinstance(u, Admin):
                    print(f"🛡️ Akses: {u.hapus_data()}")
                print("-" * 20)

        elif pilihan == "2":
            data_api = ambil_data_internet()
            if data_api:
                user_baru = hydrate_data(data_api)
                semua_user.extend(user_baru)
                print(f"✅ Berhasil menarik {len(user_baru)} user baru!")

        elif pilihan == "3":
            simpan_data(semua_user)
            print("✅ Database diperbarui!")

        elif pilihan == "4":
            print("👋 Sistem dimatikan. Sampai jumpa, Commander!")
            break
        else:
            print("❌ Pilihan tidak tersedia.")

if __name__ == "__main__":
    main()
