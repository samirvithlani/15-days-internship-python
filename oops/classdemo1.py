class Bank:
    
    amount =2000

    def balance(self):
        return 15000

    def deposit(self):
        print("deposit function called..",self.amount)
        print(self.balance())



#b will object..
b = Bank()

b.deposit()