# singly linked list is called singly linked list because every node is having a single link or next variable which points to next node or null(in python , None)

# operations in singly linked list :
#   1. insertion(at the start or at the end or after a particular node)
#   2. deletion(starting node , last node or a particular node)
#   3. searching(searching a particular node through its value)
#   4. traversal(visiting each node for one time)

# We would create node class for intializing nodes and SLL(shortcut for singly linked list) class for intialising head and for operations on singly  linked list
class Node :
    def __init__(self,item=None,next=None) :
        self.item = item
        self.next = next
class SLL :
    def __init__(self):
        self.head = None
    def is_empty(self) :
        return self.head == None
    def insert_at_the_start(self,item) :
        node = Node(item,self.head)
        self.head = node
    def delete_starting_node(self) :
        if self.head is not None :
            self.head = self.head.next
    def insert_at_the_end(self,item) :
        node = Node(item)
        if not self.is_empty() :
            curr = self.head 
            while curr.next is not None :
                curr = curr.next
            curr.next = node
        else : 
            self.head = node 
    def delete_last_node(self) :
        if self.head is not None :
            curr = self.head 
            if curr.next is None :
                self.head = None
                return
            while curr.next.next is not None :
                curr = curr.next
            curr.next = None
    def insert_after_particular_node(self,target_node,new_node_item) :
        # target node comes from searching the node with node value so first do the searching
        if target_node is not None :
            node = Node(new_node_item,target_node.next)
            target_node.next = node
    def delete_particular_node(self,deleting_node_value) :
        if self.head is None :
            pass
        elif self.head.next is None :
            if self.head.item == deleting_node_value :
                self.head = None
        else :
            curr = self.head
            if curr.item == deleting_node_value :
                self.head = curr.next
            while curr.next is not None :
                if curr.next.item == deleting_node_value :
                    curr.next = curr.next.next
                    break
                curr = curr.next
    def search_node(self,target_node_value) :
        curr = self.head 
        while curr is not None :
            if curr.item == target_node_value :
                return curr
            curr = curr.next
        return None
    def display(self) :
        curr = self.head
        while curr :
            print(curr.item)
            curr = curr.next
    def __iter__(self) :
        return SLLIterator(self.head)
class SLLIterator :
    def __init__(self,start):
        self.current = start
    def __iter__(self) :
        return self
    def __next__(self) :
        if not self.current : 
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
sll1 = SLL()
sll1.insert_at_the_start(20)
sll1.display()
print("*"*3)
sll1.insert_at_the_start(10)
sll1.display()
print("*"*3)
sll1.insert_at_the_end(30)
sll1.display()
print("*"*3)
sll1.insert_after_particular_node(sll1.search_node(20),25)
sll1.display()
print("*"*3)
sll1.delete_starting_node()
sll1.display()
print("*"*3)
sll1.delete_last_node()
sll1.display()
print("*"*3)
sll1.delete_particular_node(20)
sll1.display()
print("*"*3)
sll1.delete_particular_node(25)
sll1.display()
# Now the list is empty so we will new values and will use iterator to print items of nodes one by one 
sll1.insert_at_the_end(10)
sll1.insert_at_the_end(20)
sll1.insert_at_the_end(30)
sll1.insert_at_the_end(40)
sll1.display()
print("*"*3)
# testing iterator class
for item in sll1 :
    print(item,end=" ") # 10 20 30 40
