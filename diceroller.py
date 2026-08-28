import random


while True:
    question = input("Roll the dice?(Y/N): ")
    if question == "Y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'({dice1},{dice2})')
    elif question == "N":
        print("Thanks for playing!")
        break
    elif question != "Y" or question != "N":
        print("Invalid input")

