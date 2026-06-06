class hashtable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [[]for i in range(size)]

    def hashfunction(self,data):
        return sum((ord(char) for char in data )) % self.size
        
    def laci(self,data):
        self.table[self.hashfunction(data)].append(data)

    def display(self):
        for item in range(self.table):
            print(item, self.table[item])
        


class node :
    def __init__(self, orang):
        self.orang = orang
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def insert(self, orang):
        newnode = node(orang)
        newnode.next = self.head
        self.head = newnode

    def display(self):
        current = self.head
        while current != None:
            print (f"{current.orang}", end= "->")
            current = current.next

player = stack()
player.insert("fahrul")
player.insert("ian")
player.display()




class Node:
    def __init__(self,benda):
        self.benda = benda
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def masuk(self,benda):
        nodebaru = Node(benda)
        if self.front is None:
            self.front = self.rear = nodebaru
        else:
            self.rear.next = nodebaru
            self.rear = nodebaru
        
    def preview(self):
        current = self.front
        while current is not None:
            print(current.benda, end= "--->")
            current = current.next

meja = queue()
meja.masuk("kayu")
meja.masuk("laptop")
meja.preview()


        
         
class nodelinkedlist:
    def __init__(self,hp):
        self.hp = hp
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def tambahnode(self, hp):
        nodebaru = nodelinkedlist(hp)

        if self.head is None:
            self.head = nodebaru
            return
        
        current = self.head

        while current.next:
            current = current.next

        current.next = nodebaru
            

class nodedoublelinkedlist:
    def __init__(self,hewan):
        self.next = None
        self.prev = None
        self.hewan = hewan

class doublelinkedlist:
    def __init__(self):
        self.head = None

    def tambahhewan(self, hewan):

        nodebaru = nodedoublelinkedlist(hewan)
        if self.head is None:
            self.head = nodebaru
            return
        
        current = self.head

        while current.next:
            current = current.next

        current.next = nodebaru
        nodebaru.prev = current 
        
        
                