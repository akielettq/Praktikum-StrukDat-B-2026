class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.jumlah_pasien = 0
        
    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self.jumlah_pasien
    
    def enqueue(self, nama, keluhan):
        nodeBaru = Node(nama, keluhan)
        
        if self.is_empty():
            self.head = nodeBaru
            self.tail = nodeBaru
            
        else:
            self.tail.next = nodeBaru
            self.tail = nodeBaru
        
        self.jumlah_pasien += 1
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        pasien_dipanggil = self.head
        
        self.head = self.head.next
        self.jumlah_pasien -= 1
        
        if self.head is None:
            self.tail = None
            
        return pasien_dipanggil
    
    def peek(self):
        if self.is_empty():
            return None
        return self.head
    
    def clear(self):
        self.head = None
        self.tail = None
        self.jumlah_pasien = 0
        
    def tampilkan_antrian(self):
        current = self.head
        nomor = 1
        while current is not None:
            print(f"{nomor}. {current.nama.upper()}")
            print(f"{current.keluhan}")
            current = current.next
            nomor += 1

print("=" * 35)
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("=" * 35)

poli_antrian = Queue()
no_urut = 1

cek_awal = poli_antrian.is_empty()
if cek_awal == True:
    teks_status = "YA, antrian masih kosong."
else:
    teks_status = "TIDAK, antrian ada isinya."
print(f"[CEK] Apakah antrian kosong? {teks_status}")

poli_antrian.enqueue("Budi", "demam tinggi")
print(f"[DAFTAR] Budi terdaftar dengan keluhan: demam tinggi (No. Antrian: {no_urut})")
no_urut += 1

poli_antrian.enqueue("Ani", "batuk pilek")
print(f"[DAFTAR] Ani terdaftar dengan keluhan: batuk pilek (No. Antrian: {no_urut})")
no_urut += 1

poli_antrian.enqueue("Citra", "sakit kepala")
print(f"[DAFTAR] Citra terdaftar dengan keluhan: sakit kepala (No. Antrian: {no_urut})")
no_urut += 1

print(f"\n[INFO] Jumlah pasien menunggu: {poli_antrian.size()} orang")

pasien_berikutnya = poli_antrian.peek()
print(f"[PEEK] Pasien berikutnya: {pasien_berikutnya.nama.upper()} {pasien_berikutnya.keluhan}")

pasien_dipanggil = poli_antrian.dequeue()
print(f"[PANGGIL] Dokter memanggil: {pasien_dipanggil.nama.upper()} (keluhan: {pasien_dipanggil.keluhan})")

poli_antrian.enqueue("Dodi", "nyeri perut")
print(f"[DAFTAR] Dodi terdaftar dengan keluhan: nyeri perut (No.Antrian: {no_urut})")

print("\n[ANTRIAN SAAT INI]")
poli_antrian.tampilkan_antrian()

pasien_dipanggil = poli_antrian.dequeue()
print(f"\n[PANGGIL] Dokter memanggil: {pasien_dipanggil.nama.upper()} (keluhan: {pasien_dipanggil.keluhan})")

print(f"[INFO] Jumlah pasien masih menunggu: {poli_antrian.size()} orang")

poli_antrian.clear()
print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan")

status_akhir = "YA, antrian sudah kosong." if poli_antrian.is_empty() else "TIDAK"
print(f"[CEK] Apakah antrian kosong? {status_akhir}")

print("\nSimulasi Selesai!")