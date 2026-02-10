angka = [10, 20, 30, 40, 50]  # Membuat list berisi angka angka

angka.append(60)  # Menambahkan 60 ke belakang list
print(angka)

angka.remove(20)  # Menghapus 20 dari dalam list
print(angka)

max = angka[0]  # Deklarasi max
min = angka[0]  # Deklarasi min
for x in angka:  # Lakukan perulangan untuk cek semua isi list
    if x > max: 
        max = x  # Kalau x lebih besar dari max, ubah x menjadi max
print(max)

for x in angka:
    if x < min:
        min = x  # Kalau x lebih kecil dari min, ubah x menjadi min
print(min)

ratarata = sum(angka) / len(angka)
ratarata = int(ratarata)  # Ubah float ke integer
print(ratarata)

print(angka)

    




