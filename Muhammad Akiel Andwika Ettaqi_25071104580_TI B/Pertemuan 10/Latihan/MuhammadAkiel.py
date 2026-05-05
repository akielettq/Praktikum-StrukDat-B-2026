class StackList:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, url):
        self.items.append(url)
        
    def pop(self):
        if self.is_empty():
            return "Isi stack kosong"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
myStack = StackList()

myStack.push('google.com')
myStack.push('reddit.com')
myStack.push('browser.com')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.is_empty())
print("Size: ", myStack.size())
    
#Pake linked list
    
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 
        
    def is_empty(self):
        return self.top is None 
    
    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        
    def pop(self):
        if self.is_empty(): 
            return "Riwayat kosong"
        popped_url = self.top.url
        self.top = self.top.next
        self.count -= 1
        return popped_url
    
    def peek(self):
        if self.is_empty(): 
            return None
        return self.top.url
    
    def size(self):
        return self.count
    
myStackLL = StackLinkedList()
myStackLL.push("google.com")
myStackLL.push("reddit.com")
myStackLL.push("browser.com")

print("\n--- Testing StackLinkedList ---")
print("Peek: ", myStackLL.peek())
print("Pop: ", myStackLL.pop())
print("isEmpty: ", myStackLL.is_empty()) 
print("Size: ", myStackLL.size()) 