papan = [

["", "", "",],
["", "", "",],
["", "", "",]

]

def tampilkanPapan():
    print(f"--RONDE KE- {b}!!!--")
    print("-" * 18)
    for i in papan:
        print("    |   ".join(i))
        print("-" * 18)



giliran = "X"
a = 9
b = 1
while True :
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
        giliran = "O"
        a -= 1
        
        
    elif giliran == "O":
        papan[baris-1][kolom-1] = "O"
        giliran = "X"
        a -= 1
        

    

#horizontal
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
        break

