class Account():

    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def get_name(self):
        return self.name

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance

    def deposit(self, amount_to_deposit):
        self.balance += amount_to_deposit   #deposit

    def withdraw(self, amount_to_withdraw):
        if(self.balance - amount_to_withdraw >= 0):  # Check if enough balance
            self.balance -= amount_to_withdraw  # withdraw
        else:
            print("Insufficient funds\n")

    def report(self):
        print("Name:\t\t", self.get_name(), \
              "\nPin:\t\t", self.get_pin(), \
              "\nBalance:\t", self.get_balance(),"\n")

# account = Account("Devid","1234", 50)
# account.report()
# account.deposit(40)
# account.report()
# account.withdraw(20)
# account.report()
# account.withdraw(100)
# account.report()