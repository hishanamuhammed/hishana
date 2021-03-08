class Bank:
    def __init__(self,accno,name,type,balance):
        self.accno=accno
        self.name=name
        self.type=type
        self.balance=balance
    def deposite(self):
        amount=float(input("Enter deposite amount:"))
        self.balance=self.balance+amount
        print("current balance is:",self.balance)
    def withdraw(self):
        amount=float(input("Enter withdrawal amount:"))
        if(self.balance>amount):
            self.balance=self.balance-amount
            print("Current balance is :",self.balance)
        else:
            print("Sorry you can't withdraw this amount")
b1=Bank(676,"anu","salary",1000)
b1.deposite()
b1.withdraw()
