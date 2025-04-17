class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account = account_number
        self.balance = balance

    def deposit(self, amount):
        

        return f'{self.balance} increases by the deposited_amount'

    def withdraw(self, amount):
        if balance >1:
            
           return f' balance sufficient'
    
        if balance > 0:
           return f' withdrawal amount deducted'

        elif withdraw_amount > balance:
           return f' error message'

#creating
bankaccount1 = BankAccount
BankAccount.__init__(123456789, 3000)
print(BankAccount())
