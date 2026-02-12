data_test = {
    "objek": "Mobil",
    "akurasi": 0.85
}

def analisis_deteksi(data):
    if data["akurasi"] > 0.8:
        return "Objek Valid"
    else:
        return "Objek Meragukan"

hasil = analisis_deteksi(data_test)
print(f"Hasil Analisis {data_test['objek']}: {hasil}")