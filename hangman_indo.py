import random

with open("datagw.txt", "r") as file:
    baris = file.readlines()

kata = random.choice(baris).strip()
kataTersembunyi = kata[0] + ((len(kata)-1) * "*")
a = 1
b = len(kata) - 1

while True:
    print(kataTersembunyi)
    tebakanKata = str(input("masukkan tebakanlu: ", ).lower())

    if tebakanKata == kata:
        print("benar")
        
    else:
        print("tebakan lu salah")
        a += 1
        b -= 1
        kataTersembunyi = kata[:a] + kataTersembunyi[a:]

    if b == 0:
        print("\nplenger")
        print(f"kata yang benar itu: {kata}")
        break

    print()
