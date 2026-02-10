mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

for nim in mahasiswa:  # Untuk semua elemen didalam mahasiswa
    if mahasiswa[nim]["ipk"] > 3.5:  # Hanya pakai ipknya saja
        print(mahasiswa[nim]['nama'])

total = 0
for nim in mahasiswa:
    total += mahasiswa[nim]["ipk"]  # Untuk mencari total ipk

mean = total/len(mahasiswa)  # Untuk mencari rata rata
print(f"{mean:.2f}")

# nim = input("nim:")
# nama = input("nama:")
# prodi = input("prodi:")
# ipk = input("ipk:")
mahasiswa.update({"A004": {"nama": "akiel", "prodi": "Informatika", "ipk": 4.0}})
print(mahasiswa)