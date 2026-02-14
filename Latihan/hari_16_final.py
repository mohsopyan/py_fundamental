def daftar_user(username:str, *roles:str, **data_tambahan:str):
    hasil = {
        "nama": username,
        "peran": roles,
        "detail": data_tambahan
    }
    return hasil
user = daftar_user("Moyan", "Developer", "AI Specialist", alamat="Indonesia", status="Aktif")
print(user)