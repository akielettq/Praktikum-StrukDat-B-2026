class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        new = Node(data)
        
        if self.root == None:
            self.root = new
            return
        
        P = self.root
        Q = self.root
        
        while Q != None and new.data != P.data:
            P = Q
            
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right
            
        if new.data == P.data:
            print("Woi datanya duplikat")
            return
            
        if new.data < P.data:
            P.left = new
        else:
            P.right = new
            
bst = BinarySearchTree()

bst.insert(12)
bst.insert(8)
bst.insert(4)
bst.insert(7)
bst.insert(14)
bst.insert(99)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)
        
in_order(bst.root)