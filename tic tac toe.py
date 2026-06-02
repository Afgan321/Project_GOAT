papan = [

["", "", "",],
["", "", "",],
["", "", "",]

]

def tampilkanPapan():
    print()
    print(f"--RONDE KE- {b}!!!--")
    print("-" * 18)
    for i in papan:
        print("    |   ".join(i))
        print("-" * 18)

def hitung_menang(giliran):
    for i in range(3):
        if papan[i][1-1] == papan[i][2-1] == papan[i][3-1] ==  giliran :
            tampilkanPapan()
            print(f"{giliran} menang")
            return 1
            

        if papan[1-1][i] == papan[2-1][i] == papan[3-1][i] ==  giliran :
            tampilkanPapan()
            print(f"{giliran} Menang")
            return 1
            

    if papan[1-1][1-1] == papan[2-1][2-1] == papan[3-1][3-1] ==  giliran :
        tampilkanPapan()
        print(f"{giliran} Menang")
        return 1
        

    if papan[1-1][3-1] == papan[2-1][2-1] == papan[3-1][1-1] ==  giliran :
        tampilkanPapan()
        print(f"{giliran} Menang")
        return 1
        


giliran = "X"
a = 9
b = 1
while True:
    print()
    tampilkanPapan()
    print(f"Giliran {giliran} bermain")

    try:
        baris = int(input("baris ke: ", ))
        kolom = int(input("kolom ke: ", ))
    except ValueError:
        print("ERROR: BUKAN ANGKA!!!")
        continue

    if baris not in [1,2,3] or kolom not in [1,2,3]:
        print("ERROR: BARIS ATAU KOLOM TIDAK TERSEDIA!!!")
        continue
    if papan[baris-1][kolom-1] != "":
        print("ERROR: KOTAK SUDAH TERISI!!!")
        continue

    if giliran ==  "X" :
        papan[baris - 1][kolom - 1] = "X"   
        c = hitung_menang("X")
        if c == 1 :
            break
        giliran = "O"
        a -= 1
        
        
        
    elif giliran == "O":
        papan[baris-1][kolom-1] = "O"
  
        c = hitung_menang("O")
        if c == 1 :
            break
        giliran = "X"
        a -= 1

    if a == 0 :
        tampilkanPapan()
        print("SERI")
        break
    
    b += 1
    




















"""#horizontal
    if papan[1-1][1-1] == papan[1-1][2-1] == papan[1-1][3-1] ==  "O" :
        tampilkanPapan()
        print(f"O MENANG") 
        break
    if papan[2-1][1-1] == papan[2-1][2-1] == papan[2-1][3-1] ==  "O" :
        tampilkanPapan()
        print(f"O MENANG")
        break
    if papan[3-1][1-1] == papan[3-1][2-1] == papan[3-1][3-1] ==  "O" :
        tampilkanPapan()
        print(f"O MENANG")
        break

#vertikal
    if papan[1-1][1-1] == papan[2-1][1-1] == papan[3-1][1-1] ==  "O" :
        tampilkanPapan()
        print(f"O MENANG")
        break
    if papan[1-1][2-1] == papan[2-1][2-1] == papan[3-1][2-1] ==  "O" :
        tampilkanPapan()
        print(f"O MENANG")
        break
    if papan[1-1][3-1] == papan[2-1][3-1] == papan[3-1][3-1] ==  "O" :
        tampilkanPapan()
        print(f"O MENANG")
        break

#diagonal
    if papan[1-1][1-1] == papan[2-1][2-1] == papan[3-1][3-1] ==  "O" :
        tampilkanPapan()
        print(f"O MENANG")
        break
    if papan[1-1][3-1] == papan[2-1][2-1] == papan[3-1][1-1] ==  "O" :
        tampilkanPapan()
        print(f"O MENANG")
        break


#horizontal
    if papan[1-1][1-1] == papan[1-1][2-1] == papan[1-1][3-1] ==  "X" :
        tampilkanPapan()
        print(f"X MENANG")
        break
    if papan[2-1][1-1] == papan[2-1][2-1] == papan[2-1][3-1] ==  "X" :
        tampilkanPapan()
        print(f"X MENANG")
        break
    if papan[3-1][1-1] == papan[3-1][2-1] == papan[3-1][3-1] ==  "X" :
        tampilkanPapan()
        print(f"X MENANG")
        break
    
#Vertikal
    if papan[1-1][1-1] == papan[2-1][1-1] == papan[3-1][1-1] ==  "X" :
        tampilkanPapan()
        print(f"X MENANG")
        break
    if papan[1-1][2-1] == papan[2-1][2-1] == papan[3-1][2-1] ==  "X" :
        tampilkanPapan()
        print(f"X MENANG")
        break
    if papan[1-1][3-1] == papan[2-1][3-1] == papan[3-1][3-1] ==  "X" :
        tampilkanPapan()
        print(f"X MENANG")
        break

#Diagonal
    if papan[1-1][1-1] == papan[2-1][2-1] == papan[3-1][3-1] ==  "X" :
        tampilkanPapan()
        print(f"X MENANG")
        break
    if papan[1-1][3-1] == papan[2-1][2-1] == papan[3-1][1-1] ==  "X" :
        tampilkanPapan()
        print(f"X MENANG")
        break

    b += 1

    if a == 0:
        tampilkanPapan()
        print("SERI")
        break"""