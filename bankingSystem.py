class BankAccount:
    def __init__(self, account_holder, account_number, balance = 0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, currentBalance, amount):
        remainingBalance = currentBalance - amount
        return remainingBalance
    
class savingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0):
        super().__init__(account_holder, account_number, balance)

    def deposit(self, amount):
        deposited =  super().deposit(amount)
        #prints the ouput after depositing
        print(f"Yello!, {self.account_holder} have deposited {amount} \n Your current account balance is: {deposited}")
    
    def withdraw(self, currentBalance, amount):
        if (currentBalance - amount) > 500:
            withdrawn =  super().withdraw(currentBalance, amount)
            #prints the ouput after withdrawing
            print(f"Yello!, {self.account_holder} have withdrawn {amount} \n Your current account balance is: {withdrawn}")
        else:
            print(f"Dear {self.account_holder},\nThe current account balance is too low to complete the process.")

AccountOne = savingsAccount("Gilbert", 222233334444, 0)
accountDeposit = AccountOne.deposit(10000)
accountWithdraw = AccountOne.withdraw(AccountOne.balance, 50000)

class checkingAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0):
        super().__init__(account_holder, account_number, balance)

    def deposit(self, amount):
        deposited = super().deposit(amount)
         #prints the ouput after depositing
        print(f"Yello!, {self.account_holder} have deposited {amount} \n Your current account balance is: {deposited}")

    def withdraw(self, currentBalance, amount):
        if (currentBalance - amount) >= -1000:
            withdrawn =  super().withdraw(currentBalance, amount)
            #prints the ouput after withdrawing
            print(f"Yello!, {self.account_holder} have withdrawn {amount} \n Your current account balance is: {withdrawn}")
        else:
            print(f"Dear {self.account_holder},\nThe current account balance is too low to complete the process.")

AccountTwo = checkingAccount("Jojo", 222233335555, 0)
accountTwoDeposit = AccountTwo.deposit(50000)
accountTwoWithdraw = AccountTwo.withdraw(AccountTwo.balance, 52000)
  