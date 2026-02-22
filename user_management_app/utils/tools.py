import json
import requests

def simpan_data(list_user, filename="database.json"):
    """Menyimpan list objek User/Admin ke file JSON"""
    try:
        data_to_save = []
        for u in list_user:
            # Mengonversi atribut objek menjadi dictionary
            data_to_save.append(vars(u))

        with open(filename, "w") as file:
            json.dump(data_to_save, file, indent=4)
        print(f"✅ Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"❌ Gagal menyimpan data: {e}")

def muat_data(filename="database.json"):
    """Memuat data mentah dari file JSON"""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("ℹ️ Info: File database belum ada, memulai dengan database kosong.")
        return []
    except json.JSONDecodeError:
        print("⚠️ Warning: File database rusak, memulai dari nol.")
        return []
    
def ambil_data_internet():
    """Mengambil data dummy user dari API eksternal"""
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        print(f"🌐 Menghubungkan ke {url}...")
        respons = requests.get(url, timeout=5)

        respons.raise_for_status()

        return respons.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Koneksi gagal: {e}")
        return []
