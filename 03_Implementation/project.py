"""
project Bank System
"""
from os.path import exists
import os
import sys
def welcome():
    """welcome function."""
    print("-------------------------")
    print("WELCOME TO BANKING SYSTEM")
    print("-------------------------")
class BankSystem:
    """
    class BankSystem
    """
    name = ''
    mobile_no = 0
    adhar_no = 0
    amount=0
    acctype = ''
    pin=0

    @classmethod
    def new_account(cls):
        """Method to create New Account."""
        cls.name = input("Enter the account holder name : ")
        txt='.txt'
        filename = cls.name+txt
        cls.name=cls.name.upper()
        if exists(filename):
            print("Account name already exist")
        else:
            cls.mobile_no= int(input("Enter the Mobile no : "))
            if len(str(cls.mobile_no))!=10:
                print(" Error!!! Please Enter Correct Mobile Number")
                sys.exit()
            cls.adhar_no= int(input("Enter the Adhar no : "))
            if len(str(cls.adhar_no))!=12:
                print(" Error!!! Please Enter Correct Adhar Number")
                sys.exit()
            print("Enter the type of account :")
            print("\t\tFor Current press 1")
            print("\t\tFor Saving press 2")
            cls.acctype = int(input())
            if cls.acctype==1:
                cls.acctype='Saving'
            if cls.acctype:
                cls.acctype='current'
            else:
                print("Error!!! Please Enter correct option")
                sys.exit()
            cls.amount = int(input("Enter The Initial "
                                   "amount(Enter Amount in "
                                   "multiples of Hundred only) :"))
            if (cls.amount%100)!=0:
                print("Enter amount in multiples of hundred only")
                sys.exit()
            cls.pin=int (input("Set 4 digit password"))
            if len(str(cls.pin))!=4:
                print("enter 4 digit pin only")
            data = cls.name +','+ str(cls.pin)+','+ str(cls.amount)+','+ cls.acctype+','+str(cls.adhar_no)+','+str(cls.mobile_no)+'\n'
            file = open(filename,'a+',encoding="utf8")
            file.write(data)
            file.close()
            print("\nCongratulations!!!! Account Created Successfully")

    @classmethod
    def show_account_details(cls):
        """Method to Show All the Details of the Account."""
        accountname=str(input("Enter Account Holder Name :"))
        accountname=accountname.lower()
        pin=int(input("Enter your Pin :"))
        txt='.txt'
        filename = accountname+txt
        accountname=accountname.upper()
        if exists(filename):
            file = open(filename,'r',encoding="utf8")
            for line in file:
                data = line.split(',')
                if data[0]==accountname and data[1]==str(pin):
                    os.system('cls')
                    print("\nAccount Holder Name :",data[0],"\n")
                    print("Account Holder Mobile no. :",data[5])
                    print("Account Holder Adhar no. :",data[4],"\n")
                    print("Account Type :",data[3],"\n")
                    print("Account Balance :",data[2],"\n")
                    sys.exit()
                else:
                    print("Enter correct pin")
        else:
            print("Account Not Exists")

    @classmethod
    def deposit(cls):
        """Method to deposit money in the Bank."""
        accountname=str(input("Enter Account Holder Name :"))
        accountname=accountname.lower()
        pin=int(input("Enter your Pin :"))
        txt='.txt'
        filename = accountname+txt
        accountname=accountname.upper()
        if exists(filename):
            file = open(filename,'r+',encoding="utf8")
            for line in file:
                data = line.split(',')
                if data[0]==accountname and data[1]==str(pin):
                    addamount=int(input("Enter the amount "
                                        "you want to add"
                                        "(only  in the multiples of hundred):"))
                    if (addamount%100)==0:
                        balance=int(data[2])
                        balance += addamount
                        print("Balance is updated")
                        print("Available Balance is",balance)
                        update = data[0] +','+ data[1]+','+ str(balance)+','+ data[3]+','+data[4]+','+data[5]+'\n'
                        file = open(filename,'w',encoding="utf8")
                        file.write(update)
                        file.close()
                        sys.exit()
                    else:
                        print("Please enter amount in the multiples of hundred only")
                        sys.exit()
                else:
                    print("Enter correct pin")
                    sys.exit()
        else:
            print("Account does not exists")
            sys.exit()

    @classmethod
    def withdraw(cls):
        """Method to wihdraw money from the Bank."""
        accountname=str(input("Enter Account Holder Name :"))
        accountname=accountname.lower()
        pin=int(input("Enter your Pin :"))
        txt='.txt'
        filename = accountname+txt
        accountname=accountname.upper()
        if exists(filename):
            file = open(filename,'r+',encoding="utf8")
            for line in file:
                data = line.split(',')
                if data[0]==accountname and data[1]==str(pin):
                    withdrawamount=int(input("Enter the amount "
                                            "you want to withdraw"
                                            "(only  in the multiples of hundred):"))
                    if (withdrawamount%100)==0:
                        balance=int(data[2])
                        if balance<withdrawamount:
                            print("Insufficient Balance")
                            sys.exit()
                        else:
                            balance -= withdrawamount
                            print("Balance is updated")
                            print("Available Balance is",balance)
                            update = data[0] +','+ data[1]+','+ str(balance)+','+ data[3]+','+data[4]+','+data[5]+'\n'
                            file = open(filename,'w',encoding="utf8")
                            file.write(update)
                            file.close()
                            sys.exit()
                    else:
                        print("Please enter amount in the multiples of hundred only")
                        sys.exit()
                else:
                    print("Enter correct pin")
                    sys.exit()
        else:
            print("Account does not exists")
            sys.exit()

    @classmethod
    def show_balance(cls):
        """Method to show account Balance."""
        accountname=str(input("Enter Account Holder Name :"))
        accountname=accountname.lower()
        pin=int(input("Enter your Pin :"))
        txt='.txt'
        filename = accountname+txt
        accountname=accountname.upper()
        if exists(filename):
            file = open(filename,'r',encoding="utf8")
            for line in file:
                data = line.split(',')
                if data[0]==accountname and data[1]==str(pin):
                    os.system('cls')
                    print("Account Balance :",data[2],"\n")
                    sys.exit()
                else:
                    print("Enter correct pin")
        else:
            print("Account Not Exists")

    @classmethod
    def delete_account(cls):
        """Method to delete account."""
        accountname=str(input("Enter Account Holder Name :"))
        accountname=accountname.lower()
        pin=int(input("Enter your Pin :"))
        txt='.txt'
        filename = accountname+txt
        accountname=accountname.upper()
        if exists(filename):
            file = open(filename,'r',encoding="utf8")
            for line in file:
                data = line.split(',')
                if data[0]==accountname and data[1]==str(pin):
                    file.close()
                    os.remove(filename)
                    print("Account Balance :",data[2],"\n")
                    sys.exit()
                else:
                    print("Enter correct pin")
        else:
            print("Account Not Exists")
