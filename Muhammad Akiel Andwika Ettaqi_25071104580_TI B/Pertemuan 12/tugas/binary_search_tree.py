class Node:
    def __init__(self, id, judul):
        self.id = id
        self.judul = judul
        self.left = None
        self.right = None
        
class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        
    def Insert(self, id, judul):
        if self.root is None:
            self.root = Node(id, judul)
            print(f"Berhasil memasukkan ID {id} - {judul}")
            
        else:
            self._Insert_Rekursif(self.root, id, judul)
            
    def _Insert_Rekursif(self, node, id, judul):
        if id < node.id:
            if node.left is None:
                node.left = Node(id, judul)
                print(f"Berhasil memasukkan ID {id} - {judul}")
            else:
                self._Insert_Rekursif(node.left, id, judul)
                
        elif id > node.id:
            if node.right is None:
                node.right = Node(id, judul)
                print(f"Berhasil memasukkan ID {id} - {judul}")
            else:
                self._Insert_Rekursif(node.right, id, judul)
                
        else:
            print(f"Gagal, Buku ID {id} - {judul} Sudah terdaftar")
            
    def Traversal_Inorder(self):
        print("List buku berdasarkan ID (Terkecil ke terbesar)")
        self._Inorder_Rekursif(self.root, [1])
        
    def _Inorder_Rekursif(self, node, counter):
        if node:
            self._Inorder_Rekursif(node.left, counter)
            print(f"{counter[0]}. {node.id} - {node.judul}")
            counter[0] += 1
            self._Inorder_Rekursif(node.right, counter)
            
    def Search(self, id):
        hasil = self._Search_Rekursif(self.root, id)
        if hasil:
            print(f"ID {id} Ditemukan,  Judul: {hasil.judul}")
        else:
            print(f"ID {id} Tidak ditemukan.")
        return hasil
        
    def _Search_Rekursif(self, node, id):
        if node is None or node.id == id:
            return node
        
        if id < node.id:
            return self._Search_Rekursif(node.left, id)
        return self._Search_Rekursif(node.right, id)
    
    def Get_Min(self):
        current = self.root
        if current is None:
            return None
        while current.left:
            current = current.left
        return current.id
    
    def Get_Max(self):
        current = self.root
        if current is None:
            return None
        while current.right:
            current = current.right
        return current.id
    
    def height(self):
        return self._height_rekursif(self.root)
    
    def _height_rekursif(self, node):
        if node is None:
            return -1
        
        left = self._height_rekursif(node.left)
        right = self._height_rekursif(node.right)
        
        return max(left, right) + 1
    
# Main
katalog = Binary_Search_Tree()

katalog.Insert(50, "Dasar Pemrograman")
katalog.Insert(30, "Struktur Data")
katalog.Insert(70, "Kecerdasan Buatan")
katalog.Insert(20, "Matematika Diskrit")
katalog.Insert(40, "Basis Data")
katalog.Insert(60, "Jaringan Komputer")
katalog.Insert(80, "Sistem Operasi")
print()

katalog.Traversal_Inorder()
print()

katalog.Search(60)
katalog.Search(100)
print()

print(f"ID Terkecil: {katalog.Get_Min()}")
print(f"ID Terbesar: {katalog.Get_Max()}")

print(f"Tinggi (Height) Tree: {katalog.height()}")
