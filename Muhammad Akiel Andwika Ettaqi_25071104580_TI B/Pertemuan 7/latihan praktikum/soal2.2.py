class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class AntreanLinkedList:
    def __init__(self, data_awal):
        self.head = None

        for nama in reversed(data_awal):
            self.tambah_di_awal(nama)

    def tambah_di_awal(self, nama):
        baru = Node(nama)
        baru.next = self.head
        self.head = baru

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert_at_position(self, nama_pasien, posisi):
        baru = Node(nama_pasien)
        panjang_list = self.get_length()

        if posisi <= 1 or self.head is None:
            baru.next = self.head
            self.head = baru
            print(f"{nama_pasien} dimasukkan di posisi awal.")
            return

        if posisi > panjang_list:
            current = self.head
            while current.next:
                current = current.next
            current.next = baru
            print(f"Posisi {posisi} melebihi antrean. {nama_pasien} otomatis di posisi akhir ({panjang_list + 1}).")
            return

        current = self.head
        for _ in range(posisi - 2):
            current = current.next
        
        baru.next = current.next
        current.next = baru
        print(f"{nama_pasien} berhasil disisipkan di posisi {posisi}.")

    def tampilkan_antrean(self):
        print("\nStatus Antrean Pasien:")
        current = self.head
        i = 1
        while current:
            print(f"{i}. {current.nama}")
            current = current.next
            i += 1
        

data_awal = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]
antrean = AntreanLinkedList(data_awal)

antrean.tampilkan_antrean()

antrean.insert_at_position("Pasien Darurat X", 2)
antrean.insert_at_position("Pasien Baru Y", 10)

antrean.tampilkan_antrean()