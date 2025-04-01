# Welcome to Windows Russian Roulette
# This is a simple game where you can play Russian Roulette on your computer
# But if you lose your compeuter will set to sleep


import os
import random

def main(agreement):

    if agreement == True:
     random1 = random.randint(1, 6)
     random2 = random.randint(1, 6)

     if random1 == random2:
         os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
     else:
         print("You survived")


# Good Luck.
