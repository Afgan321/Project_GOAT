#manajemen perpustakaan

class Buku:
    def __init__(self, namabuku, pengarang, id):
        self.namabuku = namabuku
        self.pengarang = pengarang
        self.id = id


class hashtable:
    def __init__(self,size = 10):
        self.size = size
        self.lemari = [[]for i in range(self.size)]

    def hashfunction(self,namabuku, pengarang,id):
        bukumasuk = Buku(namabuku, pengarang, id)
        return sum(ord(char) for char in bukumasuk.namabuku) % self.size , bukumasuk
    
    def masuklemari(self,namabuku,pengarang,id):

        index, bukumasuk = self.hashfunction(namabuku,pengarang,id)
        self.lemari[index].append(bukumasuk)

    def display(self):
        for i in range(self.size):
            for data in self.lemari[i]:
                print(f"Rak ke-{i}")
                print(f" nama buku : {data.namabuku}")
                print(f" nama pengarang : {data.pengarang}")
                print(f" nomor id : {data.id}")
                       
                      



perpustakaan = hashtable()

"""
perpustakaan.masuklemari("tanah","fahcrul","01")
perpustakaan.masuklemari("langit","afgan","02")
perpustakaan.masuklemari("angin","rul","03")

perpustakaan.display()
"""
while True:
    print()
    namabuku1 = input("masukkan nama buku: ")
    pengarang2 = input("masukkan nama pengarang: ")
    id3 = input("masukkan nomor id: ")

    print()
    print("MEMPROSES...")
    print("BUKU TELAH DISUSUN")
    perpustakaan.masuklemari(namabuku1,pengarang2,id3)
    perpustakaan.display()