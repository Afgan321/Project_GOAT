import os
def num_verif(input_message="", error_massage="[Error] Masukan Hanya Angka!"):
    while True:
        try:
            num = int(input(input_message))
            return num
        except ValueError:
            if error_massage:
                print(error_massage)

def num_verif_ranged(low,up,input_message="",error_message="[Error] Masukan Hanya Angka!", error_ranged_message="[Error] Angka Diluar Jangkauan!"):
    while True:
        num = num_verif(input_message=input_message, error_massage=error_message)
        if num >= low and num <= up:
            return num
        else:
            if error_ranged_message:
                print(error_ranged_message)
        
def clear_screen():
    os.system("cls")
    