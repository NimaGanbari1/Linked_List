#When we use lists, the elements of the list are stored sequentially in memory.
#When we want to add an element to this list, what actually happens is that if this list is not spaced,
#it looks for a place in memory that is three times the space of the previous list and forms the new list there.
#to give Due to these changes, a linked list was generated.

#A linked list is a list whose elements are in the playback memory and are connected by a link.
#There are different types of linked list.

#This is the element class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#This is a linked list class       
class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0
    #This function adds the received element to the first of the list    
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        self.length += 1
    #This function adds the received element to the end of the list
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
    #This function takes two inputs, one is the index and the other is the value,
    #and adds the value in the list with the house number of the index.
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
    #These two functions are for printing            
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
    #Returns the number of elements in the list.
    def __len__(self):
        return self.length
    
    

ll = Linked_list()
ll.append(1)
ll.append(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.insert(2,6)
ll.insert(-10,7)
ll.insert(100,8)


print(ll)