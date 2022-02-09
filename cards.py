import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    card = input("Press enter to draw a card or print 'Q' + enter to exit")
    if card == "Q":
        break
    elif card == '':
        ran = random.randint(0, len(diamonds))
        card = diamonds.pop(ran - 1)
        hand.append(card)
        print(ran)
        print(card)
        print(diamonds)
        print("You're hand is: ", hand)

if not diamonds:
    print("There are no more cards to pick")
else:
    pass
