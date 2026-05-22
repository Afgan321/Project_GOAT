print("\nBATU GUNTING KERTAS ")


import random

while True :
    game = ["batu","gunting","kertas"]
    komputer = random.choice(game)


    player = str(input("\ntuliskan pilihan anda[batu/gunting/kertas]: ", ).lower())


    if player == komputer :
        print("\nSERI")



    elif ((player =="gunting" and komputer=="kertas")or
        (player=="kertas" and komputer=="batu")or
        (player=="batu" and komputer=="gunting")):

        print("\nMENANG")

    else:
        print("\nKALAH")
        print(f"komputer memilih: {komputer}" )

    b = str(input("main lagi? (y/n)", ).lower())
    if b!= "y" :
        print("\nselesai")
        break





