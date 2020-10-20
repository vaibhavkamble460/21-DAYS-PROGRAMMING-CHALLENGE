import os
check = input("DoYou Want shutdown PC?(YES/NO):")
if check == 'NO':
    exit()
else:
    os.system("shutdown /s /t")