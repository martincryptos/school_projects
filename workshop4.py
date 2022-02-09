class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"{self.name} has a balance of: {self.balance}")

    def withdraw(self, amount):
        new_bal = self.balance - amount
        self.balance = new_bal

    def deposit(self, amount):
        new_bal = self.balance + amount
        self.balance = new_bal

    def transfer_money(self, transferee, amount):
        print("\n", self.name, "you are transferring",
              amount, "to", transferee.name)
        if self.pin == int(input("Input your PIN: ")):
            self.withdraw(amount)
            # self.balance -= amount
            transferee.deposit(amount)
            return True
        else:
            print("PIN Invalid \ntransaction aborted\n")
            return False

    def take_money(self, takee, amount):
        print(self.name, "is taking", amount, "from", takee.name, "\n")
        if takee.pin == int(input("input their PIN: ")):
            print("\n", self.name)
            vr = int(input("To verify input your PIN: "))
            if vr == self.pin:
                takee.withdraw(amount)
                # takee.balance -= amount
                self.balance += amount
                return True
            else:
                print("Verification failed!!\ntransaction aborted")
                return False
        else:
            print("PIN invalidades\ntransaction aborted")
            return False

            # driver code for task 1
            # bob = User("Bob", 1234, "password")
            # print(f"{bob.name} {bob.pin} {bob.password}"

            # driver code for task 2
            # bob = User("Bob", 1234, "password")
            # print(f"{bob.name} {bob.pin} {bob.password}")
            # bob.change_name("jack")
            # bob.change_pin(3456)
            # bob.change_password("herro")
            # print(f"{bob.name} {bob.pin} {bob.password}")

            # driver code for task 3
            # bob = BankUser("jill", 4334, "hike")
            # print(f"{bob.name} {bob.pin} {bob.password} {bob.balance}")
            # driver code for task 4

# jill = BankUser("jill", 4444, "hike")
# print(jill.show_balance())
# jill.deposit(900)
# print(jill.show_balance())
# jill.withdraw(450)
# print(jill.show_balance())


# Drive code for task 5
jack = BankUser("Jack", 7777, "jackat")
rack = BankUser("Rack", 8888, "rackat")
rack.deposit(5000)
print(rack.show_balance())
print(jack.show_balance())
rack.transfer_money(jack, 500)
print(rack.show_balance())
print(jack.show_balance())
rack.take_money(jack, 200)
print(rack.show_balance())
print(jack.show_balance())
