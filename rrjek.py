import random
pel = int(input("Masukan Berapa peluru: "))
print()
peluru = [0 for i in range(pel)]
idx = random.randint(0,len(peluru)-1)
peluru[idx] = 1

num = 1
while True:
    print("Percobaan ke-", num)
    tekan = input("Siap? [Tekan Apapun Untuk Menembak]")
    gacha = random.choice(peluru)
    if gacha:
        print("[Tertembak] Wleee")
        break
    else:
        print("Selamat Horee")
    num += 1
    print()


