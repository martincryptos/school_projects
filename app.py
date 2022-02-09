from donations_pkg import *
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    elif authorized_user == "admin":
        print("Logged in as: ", authorized_user)
    choice = input("Choose an option: ")
    if choice == "1":
        user = input("Please input user name: ")
        pasw = input("Please input your password: ")
        authorized_user = login(database, user, pasw)
    elif choice == "2":
        user = input("Please input user name: ")
        pasw = input("Please input Password: ")
        authorized_user = register(database, user)
        if authorized_user != "":
            database[user] = pasw
        else:
            choice = input("Choose an option: ")
    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in!")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
        # choice = input("Choose an option: ")
    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("Goodbye thank you so much!")
        break
    else:
        print("ERROR ERROR")
        break
