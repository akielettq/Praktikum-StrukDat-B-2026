buku = []
nama = str
harga = float
stok = int
total = 0

def tambah_buku(nama, harga, stok, total):
    total = int(input("Mau masukin berapa buku: "))
    
    for x in range(total):
     nama = input("Masukkan nama buku: ")
     buku.append(nama)
    
     harga = float(input("Masukkan harga buku: "))
     if harga <= 0:
        print("Tidak valid")
        return 0
    
     buku.append(harga)
    
     stok = int(input("Masukkan stok buku: "))
     if stok <= 0:
        print("Tidak valid")
        return 0
    
     buku.append(stok)

tambah_buku(nama, harga, stok, total)

print(buku)