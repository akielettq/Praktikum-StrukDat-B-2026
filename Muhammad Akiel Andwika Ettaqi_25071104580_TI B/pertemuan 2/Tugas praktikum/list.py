buah = ["Apel", "Jeruk", "Mangga"]  # Buat contoh list

# 1. append(): Untuk menambah data di akhir
buah.append("Pisang")
print(buah)

# 2. insert(): Untuk menyisipkan data di posisi tertentu (ini contohnya index 1)
buah.insert(1, "Anggur")
print(buah)

# 3. remove(): Untuk menghapus elemen yang dipilih
buah.remove("Jeruk")
print(buah)

# 4. sort(): Untuk mengurutkan list sesuai abjad
buah.sort()
print(buah)

# 5. pop(): Untuk menghapus elemen terakhir dan mengambil nilainya
buahTerhapus = buah.pop()

print(f"List Buah Akhir: {buah}")
print(f"Buah yang di-pop: {buahTerhapus}")