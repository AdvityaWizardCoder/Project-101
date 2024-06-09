import random 
import time
from playsound import playsound
def dice_main():
    rand_val = random.randint(1,6)
    if rand_val == 1:
        playsound("dice-142528.mp3")
        time.sleep(0.05)
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if rand_val == 2:
        playsound("dice-142528.mp3")
        time.sleep(0.05)
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")
    if rand_val == 3:
        playsound("dice-142528.mp3")
        time.sleep(0.05)
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")
    if rand_val == 4:
        playsound("dice-142528.mp3")
        time.sleep(0.05)
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if rand_val == 5:
        playsound("dice-142528.mp3")
        time.sleep(0.05)
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if rand_val == 6:
        playsound("dice-142528.mp3")
        time.sleep(0.05)
        print("[-----]")
        print("[ 000 ]")
        print("[ 000 ]")
        print("[ 000 ]")
        print("[-----]")

while True:
    diceq = input("Do you want to roll the dice? (yes/y to roll, anything else to exit): ").strip().lower()
    if diceq in ["yes", "y"]:
        dice_main()
    else:
        print("Exiting the dice roller.")
        break