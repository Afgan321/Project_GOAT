class character :
    def __init__(self,nama,role,skill,hp):
        self.nama = nama
        self.role = role
        self.skill = skill
        self.hp = hp

    def skillserang(self,playerlain):
        print("\n -----Gameplay-----")
        playerlain.hp -= 1
        print(f"Pemain {self.nama} menyerang {playerlain.nama} dengan menggunakan skill {self.skill}")
        print(f"Nyawa {playerlain.nama} -1 ")
        print(f"Nyawa {playerlain.nama} tersisa {playerlain.hp}")

    def statistik(self):
        print()
        print(self.nama)
        print(self.role)
        print(self.skill)
        print(self.hp)
            


player1 = character("Fahrul", "Sniper", "tembak", 100)
player2 = character("minion", "kroco", "pukul", 50)

player1.statistik()
player2.statistik()

player1.skillserang(player2)


