"""
project Bank System
"""
from project import *

welcome()
print("1 - Create New Account")
print("2 - View Account Details")
print("3 - Show Balance")
print("4 - Deposit money")
print("5 - Withdraw Amount")
account=BankSystem()
option=int(input("\nEnter Your Choice :"))
if option==1:
    account.new_account()
elif option==2:
    account.show_account_details()
elif option==3:
    account.show_balance()
elif option==4:
    account.deposit()
elif option==5:
    account.withdraw()
elif option==6:
    account.delete_account()
else:
    print("Enter valid choice")
