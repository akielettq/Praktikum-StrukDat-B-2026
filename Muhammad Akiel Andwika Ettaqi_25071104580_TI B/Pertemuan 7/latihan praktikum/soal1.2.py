class Node:
    def __init__(self, data):
        self.keyword = data
        self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None

    def tambah_pencarian_linked(self, keyword):
        baru = Node(keyword)
        
        baru.next = self.head
        
        self.head = baru
        print(f"Menambahkan: '{keyword}' ke riwayat.")

    def tampilkan_history(self):
        print("Riwayat Pencarian")
        if self.head is None:
            print("Riwayat kosong.")
            return
        
        current = self.head
        while current:
            print(f"{current.keyword}")
            current = current.next

history = HistoryLinkedList()

history.tambah_pencarian_linked("Struktur Data")
history.tambah_pencarian_linked("Python Tutorial")
history.tambah_pencarian_linked("Algoritma Sorting")

history.tampilkan_history()