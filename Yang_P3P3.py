"""
Yang_P3P3.py
Jay Yang
10/26/2025
"""
#Class BankAccount
class BankAccount:

#instance def(self, account_number = 
    def __init__(self, account_number=1001, balance=500.0, interest_rate=3.0):
#self._account_number = account
        self.__account_number = account_number
#self.balance = balance = balance
        self.__balance = balance
#self._interest_rate = interest_rate
        self.__interest_rate = interest_rate

#get account number
    def get_account_number(self):
        return self.__account_number

#get balance
    def get_balance(self):
        return self.__balance

#get interest rate 
    def get_interest_rate(self):
        return self.__interest_rate

#set account number
    def set_account_number(self, account_number):
#
        self.__account_number = account_number

#set balance def
    def set_balance(self, balance):

        if balance >= 0:
            self.__balance = balance
        else:

            print("Balance cannot be negative.")

    def set_interest_rate(self, interest_rate):
        if interest_rate >= 0:
            self.__interest_rate = interest_rate
        else:
            print("Interest rate cannot be negative.")

#get Quarterly Interest Rate def
    def getQuarterlyInterestRate(self):
        return self.__interest_rate / 4

#get Quarterly Interest def
    def getQuarterlyInterest(self):
        quarterly_interest_rate = self.getQuarterlyInterestRate() / 100  # convert to decimal
        return self.__balance * quarterly_interest_rate

#Withdraw def
    def withdraw(self, amount):
#If small number < $10000
        if amount <= self.__balance:
#Balance -= small number 
            self.__balance -= amount
        else:
#If big number < $10000
#Insufficient Funds Withdrawal Denied Print            
            print("Insufficient funds. Withdrawal denied.")

#deposit def
    def deposit(self, amount):
#if big number(amount) > 0
        if amount > 0:
#balance + = big number(amount)
            self.__balance += amount
#if small number(amount),
#Deposit Amount Must Be Positive Print 
        else:
            print("Deposit amount must be positive.")

#Main 
if __name__ == "__main__":
#account = BankAccount()
    account = BankAccount()  
