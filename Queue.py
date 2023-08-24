#In this section, we have a queue implemented with a linked list, and we have a queue whose addition and subtraction are O(1).


#This is the element class
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None
#This is a linked list class       
class Queue:
    def __init__(self):
        self.head = None
        self.length = 0
        self.front = None
      
    def enqueue(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.front = new_node
        
        self.length += 1
    
    def dequeue(self):
        if self.length <= 1:
            if self.length == 0:
                print("Queue is empty!")
            else:
                value = self.front.value
                self.head = None
                self.front = None
                self.length -= 1
                return value
        else:
            value = self.front.value
            self.front = self.front.prev
            self.front.next = None
            self.length -= 1
            return value
    
    
    #This function is for printing the linked list
    def __str__(self):
        if self.length: 
            _str = ""
            temp = self.head
            while temp.next:
                _str += str(temp.value) + " <-> "
                temp = temp.next
            else:
                _str += str(temp.value)
            return _str
        else:
            return ""
        


my_que = Queue()
my_que.enqueue(1)
my_que.enqueue(5)
my_que.enqueue(-1)
my_que.enqueue(12)
my_que.enqueue(50)
my_que.enqueue(-2)
print(my_que.dequeue())


print(my_que)