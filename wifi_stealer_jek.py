import os

result = os.popen("netsh wlan show profile").read()
lines = result.splitlines()
profiles = [line.split(":")[1].strip() for line in lines if "All User Profile" in line]
print(profiles)

num = 0
for x in profiles:
    if num > 5:
        break
    
    os.system(f"netsh wlan show profile {x} key=clear")

    num += 1