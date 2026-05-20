import random
import time
print("..........................")
print("    TEBAK ANGKA BULAT")
print("       1 sampai 10")
print("''''''''''''''''''''''''''")

f = 5
while f > 0 :

 try :
    print("")

    b = random.randint(1,10)
    a = int(input("Masukkan angka: ", ))

    print("\nBener ga yh?")
    time.sleep (1)
    if a == b :

        print("----BENAR!!!----")
        
        break

    if f == 1 :
        print("plenger bet woilah")
        print("Angka yang benar: ", b)
        print("Nyawa lu abis")
        break

    else:
        print("plenger")
        f -= 1
        print("Angka yang benar: ", b)
        print(f"nyawa lu tinggal {f}")
 except:
    print("Dongo Promax")
        


print("..........................")
print("       DAH SELESAI")
print("''''''''''''''''''''''''''")

A = input()