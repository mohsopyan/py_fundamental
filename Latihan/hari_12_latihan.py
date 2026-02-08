data_sensor = [12, 45, 7, 23, 56, 89, 10, 31]

data_sensor.sort(reverse=True)
print(f"Terbesar ke Terkecil: {data_sensor}")

big_3 = data_sensor[0:3]
print(f"Big 3: {big_3}")

rata_rata = sum(big_3) / len(big_3)
print(f"Rata-rata: {rata_rata}")