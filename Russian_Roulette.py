#Russian Roulette for shutdown PC

from random import randint
import os

def russian_roulet():
    bullet = randint(1,6)
    current_chamber = randint(1,6)


    while True:
        if bullet == current_chamber:
            print("Bang")
            os.system("shutdown /s /t 1")
        else:
            print("Click...")
            choise = str(input("Continue?  Y/N  R: ")).capitalize()

            if choise == "Y":
                current_chamber -= 1
                if current_chamber == 0:
                    current_chamber = 6
            elif choise == "N":
                print("To the next...")
                break


russian_roulet()
