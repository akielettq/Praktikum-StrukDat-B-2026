from tabulate import tabulate
from kurs import kurs
from konverter import konversi

def tampilkan_tabel_kurs():
    data = []
    for kode, nilai in kurs.items():
        data.append([kode, nilai])
    print(tabulate(data, headers=["Kode", "Kurs (IDR)"], tablefmt="pretty"))

def main():
    print("=== KONVERTER MATA UANG ===")
    print()

    tampilkan_tabel_kurs()
    print()

    dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
    ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))

    hasil = konversi(jumlah, dari, ke)

    print()
    if dari == "IDR":
        print(f"Rp {jumlah:,.0f} = {hasil:.2f} {ke}")
    elif ke == "IDR":
        print(f"{jumlah:.2f} {dari} = Rp {hasil:,.0f}")
    else:
        print(f"{jumlah:.2f} {dari} = {hasil:.2f} {ke}")

main()