def num_verification(num):
    if num < 0:
        return 0
    else:
        return num
class Char:
    def __init__(self,name = "Notch", health = 100, atk = 20, defend = 5, type=None):
        self.health = health
        self.name = name
        self.atk = atk
        self.defend = defend
        self.type = type
        self.is_alive = True
        self.const_type = ['monster','player']

    def change_health(self, new_health, message=True, custom_message=None):
        new_health = num_verification(new_health)
        self.health = new_health
        if message:
            if custom_message:
                print(custom_message)
            else:
                print(f"Mengubah Max Health {self.name} Menjadi {self.health}")
    
    def change_name(self, new_name, message=True, custom_message=None):
        temp_name = self.name
        self.name = new_name
        if message:
            if custom_message:
                print(custom_message)
            else:
                print(f"Mengubah {temp_name} menjadi {self.name}")
    
    def change_attack(self, new_atk, message=True, custom_message=None):
        new_atk = num_verification(new_atk)
        self.atk = new_atk
        if message:
            if custom_message:
                print(custom_message)
            else:
                print(f"Mengubah Attack {self.name} Menjadi {self.atk}")
    
    def change_defend(self, new_defend, message=True, custom_message=None):
        new_defend = num_verification(new_defend)
        self.defend = new_defend
        if message:
            if custom_message:
                print(custom_message)
            else:
                print(f"Mengubah Defend {self.name} Menjadi {self.defend}")
    
    def change_type(self, new_type, message= True, custom_message=None):
        if new_type.lower() in self.const_type:
            self.type = new_type
            if message:
                if custom_message:
                    print(custom_message)
                else:
                    print(f"Berhasil Mengubah {self.name} Menjadi {self.type}")

    def death(self):
        print(f"{self.name} Mati Mengenaskan ")
        self.is_alive = False
    
    def hit(self, dmg):
        if dmg - self.defend < 0:
            dmg = 0
            print("Halah Poke dmg 0")
        
        if dmg - self.defend >= self.health:
            self.death()
        
        self.health = self.health - (dmg - self.defend) 
        print(f"{self.name} Terkena Hit {dmg - self.defend}, Nyawa Sekarang = {self.health}")