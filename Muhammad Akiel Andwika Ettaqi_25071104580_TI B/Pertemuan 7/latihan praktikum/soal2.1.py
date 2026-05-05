antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    print(f"Menyisipkan {nama_pasien} ke posisi {posisi}")
    
    antrean_array.insert(posisi - 1, nama_pasien)

sisipkan_pasien_darurat_array("Pasien Darurat X", 2)

print(antrean_array)