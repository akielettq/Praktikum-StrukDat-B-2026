katalog = [
 {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
 {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
 {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

keyword = []
cocok = 0


def cari_buku(katalog, keyword, cocok):
    keyword = input("Masukkan keyword yang mau dicari: ")
    for x in keyword:
        for i in katalog[0]:
            if i == x:
                cocok += 1
    if cocok >= 1:
        return katalog[0][i]
    else:
        return ("Tidak ada yang cocok")
    
cari_buku(katalog, keyword, cocok)