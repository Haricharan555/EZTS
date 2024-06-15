class Bankaccount():
    def __init__(self,account_number,balance=0):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print("The amount is:",self.balance)
        else:
            print("Not possible")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insuefficient balance")
        elif amount == 0:
            print("not possible")
        else:
            self.balance-=amount
            print("withdraw amount:",self.balance)
    def check(self):
        print("current balance:",self.balance)
a1=Bankaccount(392763288)
a2=Bankaccount(826742900,500)

a1.deposit(100)
a1.withdraw(50)
a1.check()