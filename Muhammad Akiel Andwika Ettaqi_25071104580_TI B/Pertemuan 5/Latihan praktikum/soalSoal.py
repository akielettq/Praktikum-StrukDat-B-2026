# Soal 1

# a
nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas[nilai_tugas.index(65)] = 75
print(nilai_tugas)

# b
nilai_tugas.append(95)
nilai_tugas.sort()
nilai_tugas.reverse()
print(nilai_tugas)

# c
total = sum(nilai_tugas)
print(total)

# d
for x in nilai_tugas:
    if x in nilai_tugas == 100:
        ada += 1

ada = 0
if ada >= 1:
    print("Ada nilai sempurna")
else:
    print("Tidak ada")

# Soal 2

# a
kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]
for x in kumpulan_nilai:
    if x[1] >= 75:
        print(f"Selamat {x[0]}, anda lulus!")
    else:
        print(f"Maaf {x[0]} anda harus remedi.")
        
# Soal 3

# a
sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

duasesi = sesi_pagi.intersection(sesi_siang)
print(duasesi)

# b
unikpagi = sesi_pagi - sesi_siang
uniksiang = sesi_siang - sesi_pagi

namaunik = unikpagi.union(uniksiang)
print(namaunik)

# c
sesi_hari_ini = sesi_pagi.union(sesi_siang)
print(sesi_hari_ini)

# Soal 4

# a
transaksi = [
{"produk": "Buku", "harga": 10000, "jumlah": 3},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

transaksi[0]['jumlah'] = 8
print(transaksi)

# b
transaksi += [{"produk": "Pensil", "harga": 3000, "jumlah": 20}]
transaksi += [{"produk": "Penggarus", "harga": 9000, "jumlah": 15}]
print(transaksi)

# c
for x in range(len(transaksi)):
    print(f"Produk: {transaksi[x]["produk"]} | Total: {transaksi[x]["harga"] * transaksi[x]["jumlah"]}")
