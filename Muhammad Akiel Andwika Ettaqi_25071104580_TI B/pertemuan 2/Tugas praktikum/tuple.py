angka = (10, 20, 30, 20, 40, 20)  # Buat contoh tuple

# 1. count(): Untu menghitung berapa kali angka 20 muncul
jumlah_dua_puluh = angka.count(20)

# 2. index(): Untuk mencari posisi index pertama dari angka 30
posisi_tiga_puluh = angka.index(30)

print(f"Tuple Angka: {angka}")
print(f"Jumlah angka 20 muncul: {jumlah_dua_puluh} kali")
print(f"Angka 30 ada di index ke: {posisi_tiga_puluh}")

# Kita gabisa pake append dan remove di tuple