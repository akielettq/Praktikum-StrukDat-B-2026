class NodeNode:  # Buat classnya
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_tail(self, judul, pengarang):  # Ini fungsi insert
        new_node = NodeNode(judul, pengarang)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_forward(self):
        print("Daftar Buku (Forward):")  # Buat fungsi print maju (forward)
        curr = self.head
        if not curr:
            print("List Kosong")
            return
        while curr:
            print(f"[{curr.judul} - {curr.pengarang}]", end=" -> " if curr.next else "\n")
            curr = curr.next

    def print_backward(self):
        print("Daftar Buku (Backward):")  # Buat fungsi print mundur (backward)
        curr = self.tail
        if not curr:
            print("List Kosong")
            return
        while curr:
            print(f"[{curr.judul} - {curr.pengarang}]", end=" -> " if curr.prev else "\n")
            curr = curr.prev

    def delete_by_judul(self, judul):  # Fungsi delete
        curr = self.head
        while curr:
            if curr.judul == judul:
                if curr == self.head and curr == self.tail:
                    self.head = None
                    self.tail = None
                # kalau node ada di head
                elif curr == self.head:
                    self.head = curr.next
                    self.head.prev = None
                # kalau node ada di tail
                elif curr == self.tail:
                    self.tail = curr.prev
                    self.tail.next = None
                # kalau node ada di tengah
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                print(f"\nBuku '{judul}' berhasil dihapus.")
                return
            curr = curr.next
        print(f"\nBuku '{judul}' tidak ditemukan.")

# --- EKSEKUSI BAGIAN A ---
print("=== BAGIAN A: DOUBLE LINKED LIST ===")
dll = DoubleLinkedList()

# Tambah buku
dll.insert_tail("Laskar Pelangi", "Andrea Hirata")
dll.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
dll.insert_tail("Sang Pemimpi", "Andrea Hirata")

# Jalankan print_forward dan print_backward
dll.print_forward()
dll.print_backward()

# Hapus "Bumi Manusia" dan tampilkan kembali
dll.delete_by_judul("Bumi Manusia")
dll.print_forward()
print("\n")