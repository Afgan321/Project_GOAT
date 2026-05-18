import random
import time

print("..........................")
print("    TEBAK ANGKA BULAT")
print("''''''''''''''''''''''''''")

f = 3
while f > 0 :

 try :
    print("")

    b = random.randint(1,5)
    a = int(input("Masukkan angka: ", ))

    print("\nBener ga yh?")
    time.sleep (0.5)
    if a == b :

        print("----BENAR!!!----")
        
        break

    if f == 1 :
        print("plenger bet woilah")
        print("Angka yang benar: ", b)
        break

    else:
        print("plenger")
        f -= 1
        print("Angka yang benar: ", b)
 except:
    print("Dongo Promax")
        


print("..........................")
print("       DAH SELESAI")
print("''''''''''''''''''''''''''")