import random

high_score = 0


def dice_game(high_score):
    print("Current High Score:", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
    choice_one = input("Enter your choice: ")
    if choice_one == "1":
        roll_1 = random.randint(1, 6)
        print("\nYou roll a ... ", roll_1)
        roll_2 = random.randint(1, 6)
        print("You roll a ...\n", roll_2)
        total = roll_1 + roll_2
        print("\nYou have rolled a total of: ", total)
        if total > high_score:
            print("\nNew high score!")
            print("\nCurrent High Score: ", total)
            break
    elif choice_one == "2":
        print("Goodbye!")
    else:
        dice_game(0)


dice_game(0)
