#Antrian pesanan makanan
class node:
    def __init__(self,makanan):
        self.next = None
        self.makanan = makanan


class queue:
    def __init__(self):
        self.front= None
        self.rear=None

    def tambahantrian(self,makanan):
        antrianbaru = node(makanan)

        if self.front is None:
            self.front = self.rear = antrianbaru
            return
        
        self.rear.next = antrianbaru
        self.rear = antrianbaru

    def display(self):

        current = self.front
        ke = 1
        while current.next:
            print(f"antrian ke-{ke} : {current.makanan}")
            current = current.next
            ke +=1
        return
        

antrian = queue()
antrian.tambahantrian("mie ayam")
antrian.tambahantrian("spaghetti")
antrian.tambahantrian("salad")
antrian.tambahantrian("bakso")
antrian.tambahantrian("rendang")
antrian.tambahantrian("sate")

antrian.display()