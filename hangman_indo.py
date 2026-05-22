#with open ("datagw.txt", "r")  as f :


import random

with open("datagw.txt", "r", encoding="utf-8") as file:
    baris = file.readlines()
print(baris)
kata = random.choice(baris).strip()

print(kata)