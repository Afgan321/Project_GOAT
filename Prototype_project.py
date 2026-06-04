import random
import time

#VARIABEL
skorplayer = 0
skorbot = 0
giliran = "PLAYER"
tebakanplayer = 0
angkabenar = 0
angkasalah= 0
pilihan = 0



#FUNCTION
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
    
    a =  input("Apakah anda ingin jujur?(y/n)").lower()
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

def decisionbot(pilihanbot):
    if pilihanbot == 1:
        jujur(angkabenarbot,angkasalahbot,giliran)
    else:
        bohong(angkabenarbot,angkasalahbot,giliran)

def logikamenangplayer(skorplayer11):   
    if tebakanplayer1 == angkabenarbot:
        print("tebakan player benar")
        return skorplayer11 + 1
    else:
        print("tebakan player salah")
        return skorplayer11 -1

def decisionplayer():
    if pilihan == 1:
        jujur(angkabenar,angkasalah,giliran)
    else:
        bohong(angkabenar,angkasalah,giliran)

def logikamenangbot(skorbot11):
    if tebakan == angkabenar:
        print("tebakan bot benar")
        return skorbot11 + 1
    else:
        print("tebakan bot salah")
        return skorbot11 - 1



#MAIN
while True:
        
    try:
        time.sleep(0.5)
        print()
        if giliran == "PLAYER" :
            print(f"===Giliran {giliran} MEMBERI ANGKA===")
            angkabenar,angkasalah,pilihan= masukkanangkaplayer()
            decisionplayer()
            tebakan = tebakanbot(angkabenar,angkasalah)
            skorbot = logikamenangbot(skorbot)
            tampilkanskor()
            giliran = "BOT"

        elif giliran == "BOT":
            print(f"===GILIRAN {giliran} MEMBERI ANGKA===")
            angkabenarbot,angkasalahbot,pilihanbot= masukkanangkaBot(skorplayer,skorbot)
            decisionbot(pilihanbot)
            tebakanplayer1 = logikatebakanplayer(angkabenarbot,angkasalahbot,tebakanplayer)
            skorplayer = logikamenangplayer(skorplayer)
            tampilkanskor()
            giliran = "PLAYER"

    except ValueError:
        print("ERROR: SILAHKAN ULANG DAN HANYA MASUKKAN ANGKA!!!")
        



    

    







    


