import donations_pkg


def show_homepage():
    string = "=== DonateMe Homepage ==="
    print(string.center(50))
    # print(f'{"=== DonateMe Homepage ===" : ^30}') does not work for some reason
    print("""
    ------------------------------------------
    | 1.    Login       | 2.    Register     |
    ------------------------------------------
    | 3.    Donate      | 4. Show Donations  |
    ------------------------------------------
    |                5.  Exit                |
    ------------------------------------------""")


def donate(username):
    donations_amt = float(input("Enter amount to donate: "))
    donation = f"{username} donated {donations_amt}"
    print(f"Thank you for donating {username}")
    return donation


def show_donations(donations):
    headr = "--- All Donations ---\n"
    print(headr.center(50))
    if donations == []:
        print("Currently there are no donations\n")
    else:
        for donation in donations:
            print(donation)


# show_homepage()
