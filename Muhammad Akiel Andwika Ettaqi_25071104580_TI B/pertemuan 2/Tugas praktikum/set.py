kelas_a = {"Ani", "Budi", "Citra"}  # Kita buat 2 tuple berbeda
kelas_b = {"Budi", "Dedi", "Eka"}

# 1. add(): Untuk menambah satu elemen baru
kelas_a.add("Feri")
print(kelas_a)

# 2. union(): Untuk menggabungkan dua set (semua siswa)
gabunganKelas = kelas_a.union(kelas_b)

# 3. intersection(): Untuk mencari irisan (siswa yang ada di kedua kelas)
siswaSama = kelas_a.intersection(kelas_b)

# 4. difference(): Mencari siswa yang hanya ada di kelas A tapi tidak ada di B
hanyaKelasA = kelas_a.difference(kelas_b)

print(f"Gabungan: {gabunganKelas}")
print(f"Siswa yang sama (Irisan): {siswaSama}")
print(f"Hanya di Kelas A: {hanyaKelasA}")