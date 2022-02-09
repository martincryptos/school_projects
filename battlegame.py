# Week 1 workshop, interactive console based game, Martin Huber 9-21

wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_dmg = 150
elf_dmg = 100
human_dmg = 20

dragon_hp = 300
dragon_dmg = 50

print("1) Wizard")
print("2) Elf")
print("3) Human")
character = input("Choose your character: ")

while True:
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_dmg = wizard_dmg
        break
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_dmg = elf_dmg
        break
    elif character == "3":
        character = human
        my_hp = human_hp
        my_dmg = human_dmg
        break
    else:
        print("Unknown input ):")
        break

fstring = f"You have chosen a {character}, You're HP is:{my_hp}, you cause {my_dmg} damage per hit"
print(fstring)
print("You will now battle with the dragon, good luck!")

while True:
    fstring = f"the dragon takes {my_dmg} damage!! And he attacks for {dragon_dmg} damage!!"
    dragon_hp_1 = dragon_hp - my_dmg
    my_hp_1 = my_hp - dragon_dmg
    print(fstring)
    new_string = f"your HP is now {my_hp_1} and the dragons is {dragon_hp_1}"
    print(new_string)
    if my_hp_1 <= 0:
        print("you died")
        break
    else:
        print(fstring)
        my_hp_2 = my_hp_1 - dragon_dmg
        dragon_hp_2 = dragon_hp_1 - my_dmg
        string2 = f"your HP is now: {my_hp_2} and the dragons is {dragon_hp_2}"
        print(string2)
        if my_hp_2 <= 0:
            print("you're dead!! good try")
            break
        else:
            print(fstring)
            my_hp_3 = my_hp_2 - dragon_dmg
            dragon_hp_3 = dragon_hp_2 - my_dmg
            if my_hp_3 == 0:
                print("You are resilient Human, but have died nonetheless!")
                break
            else:
                print("hello 5th dimension")
                break
