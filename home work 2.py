def deposit(balance, amount):
    balance = balance + amount
    return balance
def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient Balance")
        return balance
    else:
        balance = balance - amount
        return balance
def displaydetails(name, balance):
    print("\n----- ATM DETAILS -----\n")
    print("Account Holder :", name)
    print("Final Balance  :", balance)


name = input("Enter account holder name: ")
balance = int(input("Enter current balance: "))
deposit_amount = int(input("Enter deposit amount: "))
withdraw_amount = int(input("Enter withdrawal amount: "))
balance = deposit(balance, deposit_amount)
balance = withdraw(balance, withdraw_amount)
displaydetails(name, balance)