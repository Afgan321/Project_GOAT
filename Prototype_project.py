import random
import time
skorplayer = 0
skorbot = 0
giliran = "PLAYER"
tebakanplayer = 0

angkabenar = 0
angkasalah= 0
pilihan = 0

def tampilkanskor():
    time.sleep(0.5)
    print()
    print(f"===Skor saat ini===")
    print(f"Player = {skorplayer}") 
    print(f"Bot = {skorbot}") 

def masukkanangkaplayer():
    time.sleep(0.5)
    angkabenar = int(input("Masukan angka pertama: "))
    angkasalah = int(input("Masukan angka kedua: "))
    
    a =  input("Apakah anda ingin jujur?(y/n)" .lower())
    if a == "y":
        return angkabenar, angkasalah, 1
    else:
        return angkabenar, angkasalah, 0
    
def jujur(angkabenar,angkasalah,giliran):
    time.sleep(0.5)
    print()
    print()
    print(f"{giliran} berkata bahwa: ")
    print(f"{angkabenar} angka benar")
    print(f"{angkasalah} angka salah")
    
def bohong(angkabenar,angkasalah, giliran):
    time.sleep(0.5)
    print()
    print(f"{giliran} berkata bahwa: ")
    print(f"{angkasalah} angka benar")
    print(f"{angkabenar} angka salah")
    
def masukkanangkaBot(skorplayer,skorbot):
    angkabenarbot = random.randint(1,100)
    angkasalahbot = random.randint(1,100)
    if angkabenarbot == angkasalahbot:
        angkasalahbot += 1
    if skorplayer == 3 or skorbot == -2:
        return angkabenarbot, angkasalahbot, 0
    return angkabenarbot, angkasalahbot,  1

def tebakanbot(angkabenar,angkasalah):
    time.sleep(0.5)
    print()
    print("Bot sedang menebak...")
    time.sleep(2)
    print("===TEBAKAN BOT===")
    isitebakan = [angkabenar, angkasalah]
    tebakan = random.choice(isitebakan)
    print("       ", tebakan)
    return tebakan

def logikatebakanplayer(angkabenarbot, angkasalahbot,tebakanplayer):
    time.sleep(0.5)
    print()
    print(f"===Player menebak===")
    tebakanplayer = int(input("Tebakan player adalah: "))
    return tebakanplayer



while True:
    time.sleep(0.5)
    print()
    if giliran == "PLAYER" :
        print(f"===Giliran {giliran} MEMBERI ANGKA===")
        angkabenar,angkasalah,pilihan= masukkanangkaplayer()

        if pilihan == 1:
            jujur(angkabenar,angkasalah,giliran)
        else:
            bohong(angkabenar,angkasalah,giliran)

        tebakan = tebakanbot(angkabenar,angkasalah)

        if tebakan == angkabenar:
            print("tebakan bot benar")
            skorbot += 1
        else:
            print("tebakan bot salah")
            skorbot -=1

        tampilkanskor()

        giliran = "BOT"

        

    elif giliran == "BOT":
        print(f"===GILIRAN {giliran} MEMBERI ANGKA===")
        angkabenarbot,angkasalahbot,pilihanbot= masukkanangkaBot(skorplayer,skorbot)

        if pilihanbot == 1:
            jujur(angkabenarbot,angkasalahbot,giliran)
        else:
            bohong(angkabenarbot,angkasalahbot,giliran)

        tebakanplayer1 = logikatebakanplayer(angkabenarbot,angkasalahbot,tebakanplayer)

        if tebakanplayer1 == angkabenarbot:
            print("tebakan player benar")
            skorplayer += 1
        else:
            print("tebakan player salah")
            skorplayer -=1

        tampilkanskor()

    
        giliran = "PLAYER"
        

    else:
        print("Error")

    


    







    


