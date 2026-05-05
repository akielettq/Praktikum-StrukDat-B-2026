# 1. Buat class Node
class NodeCircular:  # Buat class
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_tail(self, nama):  # Fungsi insertnya
        new_node = NodeCircular(nama)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head # Membentuk sirkular (menunjuk ke dirinya sendiri)
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head # Tail selalu menunjuk kembali ke head

    def print_antrian(self):  # Fungsi print antrian
        if not self.head:
            print("Antrian Kosong")
            return
        
        curr = self.head
        print("Kondisi Antrian:")
        while True:
            print(curr.nama, end=" -> ")
            curr = curr.next
            if curr == self.head: # Kalau udah kembali ke awal, hentikan loop
                break
        print(f"(kembali ke {self.head.nama})")

    def delete_head(self):  # fungsi delete
        if not self.head:
            print("Antrian Kosong, tidak ada yang bisa dilayani.")
            return
        
        dihapus = self.head.nama
        # Kalau antrian hanya sisa 1 orang
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head # Update tail biar menunjuk ke head yang baru
            
        print(f"\n{dihapus} sudah dilayani (dihapus dari antrian).")

# --- EKSEKUSI BAGIAN B ---
print("=== BAGIAN B: CIRCULAR LINKED LIST ===")
cll = CircularLinkedList()

# Tambahkan 4 pelanggan awal
cll.insert_tail("Andi")
cll.insert_tail("Budi")
cll.insert_tail("Citra")
cll.insert_tail("Dina")

# Tampilkan satu putaran antrian
cll.print_antrian()

# 3. Tambahkan pelanggan baru (Edo) lalu tampilkan
print("\nEdo masuk ke antrian.")
cll.insert_tail("Edo")
cll.print_antrian()

# 4. Hapus Andi (dilayani) lalu tampilkan
cll.delete_head()
cll.print_antrian()