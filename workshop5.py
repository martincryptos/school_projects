import random


def guess_random_num(tries, start, stop):
    # use random to generate random # between start and stop inclusive
    targ = random.randrange(start, stop+1)
    # write a while loop that loops as long as tries != to 0, inside loop print tries remaining
    while tries != 0:
        print(f"Guess a number between {start} and {stop}")
        print(f"You have {tries} trie(s) remaining.\n")
    # prompt user for input of a 'guess', compare number against target number aka generated #
        guss = int(input("Make a guess yee scurvy dog!\n:  "))
        if (stop < guss) or (guss < start):
            print(
                f"Must choose number in range {start} to {stop} and you're down 1 try")
            tries -= 1
            guss = int(input("Make a guess dummy!\n "))
        else:
            continue
    # if equal print success msg,, if lower print guess higher and "" if lower, decrement tries by 1
        if guss == targ:
            print("\nCORRECT!!!")
            break
        elif guss < targ:
            print("\nguess higher!\n")
            tries -= 1
        elif guss > targ:
            print("\nguess lower!!\n")
            tries -= 1
        else:
            pass
    if tries == 0:
        print(f"\nyou have failed! \nthe number was: {targ}")


def guess_ran_num_linear(tries, start, stop):
    targ = random.randrange(start, stop+1)
    gues = start
    print(f"The number for the computer to guess is {targ}\n")

    while tries != 0:
        print(f"The computer is guessing, it has {tries} more attempt(s)")
        print(f"the computer guessed {gues} linearly")
        if gues == targ:
            print("It got it!!")
            break
        else:
            gues += 1
            tries -= 1
    if tries == 0:
        print("it failed")
    return


def guess_ran_num_binry(tries, start, stop):
    targ = random.randint(start, stop)
    lb = start
    ub = stop
    piv = (start + stop) // 2
    print(f"The number for the computer to guess is {targ}\n")
    while tries != 0:
        if targ < piv:
            print("Guess lower computer!", piv)
            tries -= 1
            ub = piv
            piv = (lb + ub) // 2
        elif targ > piv:
            print("Guess higher computer!!", piv)
            tries -= 1
            lb = piv
            piv = (ub + lb) // 2
        elif targ == piv:
            print("computer guessed it!", piv)
            break
        else:
            break
    if tries == 0:
        print("computer couldn't get it!")


# if user doesn't successfully guess by tries = 0 then print failure message
# guess_random_num(5, 0, 10)
guess_ran_num_binry(5, 0, 100)
