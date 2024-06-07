import os
import platform

def clear_screen():
    if platform.system() == "windows":
        os.system("cls")
    else:
        os.system("clear")



