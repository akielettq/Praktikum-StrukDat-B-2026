mahasiswa = {
    "nama": "Rian",
    "nim": "123456",
    "jurusan": "Teknik Informatika"
}  # Kita buat data mahasiswa

print(mahasiswa)

# 1. get(): Untuk mengambil nilai dengan aman (ga error kalau key gada)
namaMhs = mahasiswa.get("nama")

# 2. update(): Untuk menambah data baru atau mengupdate data lama
mahasiswa.update({"ipk": 3.75, "semester": 4})

# 3. pop(): Untuk menghapus item berdasarkan key
mahasiswa.pop("jurusan")

# 4. keys() dan values(): Untuk melihat semua kunci dan semua nilai
kunci = mahasiswa.keys()
isi = mahasiswa.values()

print(f"Nama: {namaMhs}")
print(f"Data Mahasiswa Update: {mahasiswa}")
print(f"List Kunci (Keys): {list(kunci)}")
print(f"List nilai (Values): {list(isi)}")