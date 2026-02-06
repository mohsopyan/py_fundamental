password = "moyan"
pw = ""

while pw != password:
    pw = input("Masukkan password: ").lower()
    if pw != password:
        print("Salah, coba lagi!")

print("Mantap! Silakan masuk.")