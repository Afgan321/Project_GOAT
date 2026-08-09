#contoh pengunaan file handling adalah
#data mahasiswa, dataset ml, file konfigurasi, log aplikasi

#file handling 
#file handling adalah proses membaca,menulis,membuat,menghapus
#file melalui program

#komponen file
#nama file = file.txt
#path = lokasi file
#mode = cara akses file

#jenis file

#text file
#txt, csv, json
#dapat dibaca manusia

#jpg,png.mp3
#tidak bisa dibaca langsung
#mendukung text&binary mode

#mode file
"""
r read
w write
a append
t text
x create
+ read and write
b binary mode
"""

"""with open("Belajar/belajar.txt", "a") as f:
    x = 3
    while x > 0:
        f.write(input() + "\n")
        x -= 1"""

"""with open ("Belajar/belajar.txt", "r") as f:
    data = f.readlines()

data.insert(1, "gacor\n")

with open("Belajar/belajar.txt", "w") as f :
    f.writelines(data)"""


"""def hitung(n):
    if n == 0:
        return
    
    
    hitung(n-1)
    print(n)
    


hitung(6)

def pangkat(n):
    if n == 0:
        return 1
    else:
        return n * pangkat(n-1)

a = pangkat(7)
print(a)


def palindrom(teks):
    if len(teks) == 0:
        return ""
    
    else:
        return teks[-1] + palindrom(teks[:-1])
    
b = palindrom("halo")
print(b)"""

a = [2,3,4,5,6,7]
cari = 2

"""for i in range(len(a)):
    if cari == a[i]:
        print("data berhasil ditemukan pada indeks", i)
        break

    print("data tidak ditemukan")"""

kiri = 0
kanan = len(a) -1

while kiri <= kanan:
    tengah = (kiri + kanan) // 2

    if cari == a[tengah]:
        print(f"data ditemukan indeks ke {tengah}")
        break

    elif cari < a[tengah]:
        kanan = tengah - 1

    else:
        kiri = tengah +1


for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1],a[j]

print(a)