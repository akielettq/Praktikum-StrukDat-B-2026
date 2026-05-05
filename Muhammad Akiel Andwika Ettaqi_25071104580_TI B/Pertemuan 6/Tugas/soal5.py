import soal1 as satu
import soal2 as dua
import soal3 as tiga
import soal4 as empat

print("=== PyBook Store ===")

print(" 1. Tambah buku")
print(" 2. Tampilkan semua buku")
print(" 3. Beli buku")
print(" 4. Laporan penjualan")
print(" 5. Keluar")

inputan = int(input("Masukkan nomor berapa"))

match (inputan):
    case 1:
        satu.tambah_buku
    case 2:
        dua.cari_buku
    case 3:
        tiga.proses_transaksi
    case 4:
        empat.hitung_diskon
        









