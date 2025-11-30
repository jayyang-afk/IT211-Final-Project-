#Yang_main
#BankAccount
#10/26/2025
#Jay Yang

#Yang_P3P3 Import BankAccount
from Yang_P3P3 import BankAccount
#Main Def
def main():

#Account Balance 
    account = BankAccount(account_number=2022, balance=10000.0, interest_rate=3.0)

#"Do you want to withdraw or deposit" Input
    choice = input("Do you want to withdraw or deposit?").strip().lower()
#If choice is withdraw
    if choice == 'withdraw' or choice == 'Withdraw':
#Float input "Enter the amount to withdraw:"
        amount = float(input("Enter the amount to withdraw: $"))
        account.withdraw(amount)
#Else If choice is deposit 
    elif choice == 'deposit' or choice == 'Deposit':
#asking input is "enter the amount to deposit:"
        amount = float(input("Enter the amount to deposit: $"))
        account.deposit(amount)
    else:
#Invalid Choice No Transaction Made Print
        print("Invalid choice. No transaction made.")

#New line(n) ---Account Summary print---
    print("\n--- Account Summary ---")
#Account Number Print and get_account_number(#2022)
    print("Account Number:", account.get_account_number())
#Balance Print and $ get_balance($10000 - withdraw or deposit)
    print("Balance: $", account.get_balance())
#Quarterly Interest Rate Print and getQuarterlyInterestRate(interest rate / 4) %
    print("Quarterly Interest Rate:", account.getQuarterlyInterestRate(), "%")
#Quarterly Interest Amount Print and $ getQuarterlyInterest(balance * quarterly interest rate)
    print("Quarterly Interest Amount:", "$", account.getQuarterlyInterest())

#Print __name__ == 
if __name__ == "__main__":main()

