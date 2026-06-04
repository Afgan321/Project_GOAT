import random
import tools
from classes.char import Char
import character.character_logic
import time

def show_char_UI(char):
    print("=" * 30)
    print(f"    Selamat Datang {char.name}")
    if char.type:
        print(f"         Type: {char.type}")
    print("=" * 30)
    print(f"Max Health: {char.health}")
    print(f"Damage: {char.atk}")
    print(f"Defend: {char.defend}")

def change_char_atribute(char):
    while True:
        tools.clear_screen()
        show_char_UI(char)
        print("=" * 30)
        print("1. Name")
        print("2. Max Health")
        print("3. Damage")
        print("4. Defend")
        print("5. Type")
        print("0. Keluar")
        print("=" * 30)
        choise = tools.num_verif_ranged(0,5,input_message="Masukan Angka: ")
        match choise:
            case 1:
                new_name = input("Masukan Nama Baru: ")
                char.change_name(new_name)
                time.sleep(1)
            case 2:
                much = tools.num_verif(input_message="Masukan Max Health Baru: ")
                char.change_health(much)
                time.sleep(1)
            case 3:
                much = tools.num_verif(input_message="Masukan Damage Baru: ")
                char.change_attack(much)
                time.sleep(1)
            case 4:
                much = tools.num_verif(input_message="Masukan Defend Baru: ")
                char.change_defend(much)
                time.sleep(1)
            case 5:
                ver = True
                while ver:
                    new_type = input("Masukan Type Baru: ")
                    if new_type in char.const_type:
                        char.change_type(new_type)
                        time.sleep(1)
                        ver = False
                    else:
                        print("Type Tidak Valid (1. Lanjut | 0. Keluar)")
                        choise2 = tools.num_verif_ranged(0,1,input_message="Masukan Input: ")
                        if choise2:
                            continue
                        else:
                            ver = False
            case 0:
                return

def edit_char(char):
    while True:
        tools.clear_screen()
        show_char_UI(char)
        print("=" * 30)
        print("1. Edit")
        print("0. Keluar")
        choise = tools.num_verif_ranged(0,1, input_message="Masukan Angka: ")
        if choise:
            change_char_atribute(char)
            return
        else:
            return


def main_menu(char):
    while True:
        tools.clear_screen()
        print("=" * 50)
        print("    Welcome to Computer Immortal: Boom Boom")
        print("                     v1.0")
        print("=" * 50)
        print("1. Start Game")
        print("2. Edit Character")
        print("0. Close Game")
        choise = tools.num_verif_ranged(0,2, input_message="Masukan Angka: ")
        match choise:
            case 0:
                print("Terima Kasih")
                break
            case 1:
                ...
            case 2:
                edit_char(char)
            case _:
                print("[Error]")


hero = Char(name="Fahrul")
main_menu(hero)