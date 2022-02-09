def show_balance(balance):
    print(balance)


def deposit(balance):
    amount = float(input("Enter amount to deposit:"))
    balance = amount + balance
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw:"))
    balance = balance - amount
    return balance


def logout(name):
    bye = f"Goodbye {name}!"
    print(bye)
