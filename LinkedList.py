class Node : 
	def __init__(self, value = 0, next = None):
		self.value = value
		self.next = next
            

first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value): # O(n)
        new_node = Node(value)
        if self.head is None : 
            self.head = new_node
        # 맨 뒤의 node가 new_node를 가리켜야함
        else: 
            current = self.head
            while(current.next):
                 current = current.next
            current.next = new_node

    def get(self, idx): # O(n)
        current = self.head
        for _ in range(idx):
             current = current.next
        return current.value
         
    def insert(self, idx, value):
        current = self.head
        new_node = Node(value)
        for _ in range(idx-1):
             current = current.next
        new_node.next = current.next
        current.next = new_node
    
    def remove(self,idx):
        current = self.head
        for _ in range(idx-1):
          current = current.next
        current.next = current.next.next

    def print(self, idx = 0):
        print("====== Linked List ======")
        current = self.head
        while(current):
            if current.next is not None :
                str_value = str(current.value)
                str_next = str(current.next)[-12:-1]
            else :
                str_value = str(current.value)
                str_next = str(current.next)
            print(" Node(" + str_value + ")=", end='')
            print("(" + str_value + "," + str_next + ")")
            current = current.next
        print("=========================\n")



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert(2,9)
ll.print()

ll.remove(2)
ll.print()