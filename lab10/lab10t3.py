#LAB10T2

class account:
    saldo = 0
    def __init__(self, saldo = 0):
        self.saldo = saldo
        print("Bank account created.")

    def start(self):
        start_amount = 2000
        self.saldo = self.saldo + start_amount
        print("Bank account balance: {:.2f}".format(self.saldo), "€")
# kahden desimaalin tarkkuus, kun käsitellään rahaa
    def add(self):
        amount = float(input("How many euros will be added? "))
        self.saldo = self.saldo + amount
        print("Bank account balance: {:.2f}".format(self.saldo), "€")

    def withdraw(self):
        amount = float(input("How many euros will be withdrawn? "))
        if (self.saldo >= amount):
            self.saldo = self.saldo - amount
            print("Bank account balance: {:.2f}".format(self.saldo), "€")
        else: 
            print("Sorry, you have only {:.2f}".format(self.saldo), "€, the withdraw cannot be done")

tili = account()
tili.start()
tili.add()
tili.withdraw()
tili.withdraw()