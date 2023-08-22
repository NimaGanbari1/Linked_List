class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        self.length += 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            else:
                temp.next = new_node
        else:
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        if index <= 0:
            self.push(value)
        elif index >= self.length-1:
            self.append(value)
        else:
            temp = pre = self.head
            while index:
                pre = temp
                temp = temp.next
                index -= 1
            else:
                new_node = Node(value)
                new_node.next = temp
                pre.next = new_node
                
    def setter(self, lst):
        self.head = None
        self.length = 0
        for value in lst[::-1]:
            self.push(value)
    def __str__(self):
        _str = ""
        temp = self.head
        while temp.next:
            _str += str(temp.data) + " -> "
            temp = temp.next
        else:
            _str += str(temp.data)
        return _str
    
    def __len__(self):
        return self.length