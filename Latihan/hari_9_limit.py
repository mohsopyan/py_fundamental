password = "moyan"
kesempatan = 3

while kesempatan > 0:
    pw = input(f"Masukkan password (Sisa {kesempatan}x): ").lower()

    if pw == password:
        print("Akses diberikan!")
        break

    kesempatan -= 1
    if kesempatan > 0:
        print("Salah!")
    else:
        print("Akun terblokir! percobaan habis")