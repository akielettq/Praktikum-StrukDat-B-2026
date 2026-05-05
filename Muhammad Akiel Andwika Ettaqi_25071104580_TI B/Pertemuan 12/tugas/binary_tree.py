class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        
        self.root.right.right = Node('F')

    def traverse_preorder(self, node, hasil):
        if node is not None:
            hasil.append(node.data) 
            self.traverse_preorder(node.left, hasil) 
            self.traverse_preorder(node.right, hasil) 

    def traverse_inorder(self, node, hasil):
        if node is not None:
            self.traverse_inorder(node.left, hasil) 
            hasil.append(node.data) 
            self.traverse_inorder(node.right, hasil) 

    def traverse_postorder(self, node, hasil):
        if node is not None:
            self.traverse_postorder(node.left, hasil) 
            self.traverse_postorder(node.right, hasil) 
            hasil.append(node.data) 

    def get_leaf_nodes(self, node, hasil):
        if node is not None:
            if node.left is None and node.right is None:
                hasil.append(node.data)
            self.get_leaf_nodes(node.left, hasil)
            self.get_leaf_nodes(node.right, hasil)

# Main
tree = BinaryTree()
tree.insert_manual()

hasil_preorder = []
tree.traverse_preorder(tree.root, hasil_preorder)
print(f"1. Pre-Order   : {' - '.join(hasil_preorder)}")

hasil_inorder = []
tree.traverse_inorder(tree.root, hasil_inorder)
print(f"2. In-Order    : {' - '.join(hasil_inorder)}")

hasil_postorder = []
tree.traverse_postorder(tree.root, hasil_postorder)
print(f"3. Post-Order  : {' - '.join(hasil_postorder)}")

hasil_leaf = []
tree.get_leaf_nodes(tree.root, hasil_leaf)
print(f"Leaf nodes: {', '.join(hasil_leaf)}")
