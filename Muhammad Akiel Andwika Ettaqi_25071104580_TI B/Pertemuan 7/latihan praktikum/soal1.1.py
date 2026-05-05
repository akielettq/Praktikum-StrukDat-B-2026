history_array = ["google.com", "python.org"]

cari = str

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)
    print(f"Berhasil menambahkan {keyword}")

while cari:
    cari = input("search apa: ")
    
    if cari == "|":
        break
    
    tambah_pencarian_array(cari)

print(history_array)
        