import random
from PIL import Image
img1 = Image.open('dice-1.png')
img2 = Image.open('dice-2.png')
img3 = Image.open('dice-3.png')
img4 = Image.open('Dice-4.png')
img5 = Image.open('Dice-5.png')
img6 = Image.open('Dice-6.png')

def roll_dice():
    r = random.randint(1, 6)
    if r == 1:
        img1.show()
    elif r == 2:
        img2.show()
    elif r == 3:
        img3.show()
    elif r == 4:
        img4.show()
    elif r == 5:
        img5.show()
    else:
        img6.show()


while True:
    diceq = input("Do you want to roll the dice? (yes/y to roll, anything else to exit): ").strip().lower()
    if diceq in ["yes", "y"]:
        roll_dice()
    else:
        print("Exiting the dice roller.")
        break
