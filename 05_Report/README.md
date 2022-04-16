# BankingSystem
-----------------

# Description
Banking System allows a user to conduct financial transactions via the Internet. Online banking is also known as Internet banking or web banking. Online banking offers customers almost every service traditionally available through a local branch including deposits, transfers, and online bill payments.The online banking system will typically connect to or be part of the core banking system operated by a bank to provide customers access to banking services in place of traditional branch banking.

# Identifing Features
* The application shall have the ability to Create New Account.
* The application shall have the ability to show account details.
* The application shall have the ability to Deposite amount.
* The application shall have the ability to Withdraw amount.
* The application shall have the ability to do Balance Enquiry.

# State of Art
* The main objetive of this project is to make peoples life little easy by making banking hassle free.
* To make banking process more efficient.

# Requirments
## High Level Requirments
 | --ID | Desciption | Status |
 |:------------:|:-----------:|:---------:|
 | HLR1 | It shall have the the feature to create new account | Implemented |
 | HLR2 | It shall have the the feature to show Account Details | Implemented |
 | HLR3 | It shall have the the feature to Add amount | Implemented |
 | HLR4 | It shall have the the feature to Withdraw amount | Implemented |
 | HLR5 | It shall have the the feature to do Balance Enquiry | Implemented |
 | HLR6 | It shall have the the feature to delete the existing account | Implemented |

## Low Level Requirments
 | --ID | Desciption | Status |
 |:------------:|:-----------:|:---------:|
 | LLR1 | It shall create new account in the system with correct information | Implemented |
 | LLR2 | It shall check if account already exists in the system | Implemented |
 | LLR3 | It shall show an account details only when correct account user name and psssword is inserted | Implemented |
 | LLR4 | It shall not create duplicate accounts | Implemented |
 | LLR5 | It shall store all the account details securely | Implemented |
 | LLR7 | It shall be able to add amount in the bank system | Implemented |
 | LLR8 | It shall be able to withdraw amount from the bank system | Implemented |
 | LLR9 | It shall be able to show the amount avilable in users bank account | Implemented |
 | LLR10 | It shall be able to delete the existing account | Implemented |

# SWOT ANALYSIS

![_get_premium_download_high_resolution_imagedesigned_with_EDIT org](https://user-images.githubusercontent.com/98864424/161673315-fbf70ca6-1104-4a52-a008-cb2e8be34861.jpg)

# 5W'S AND 1H

## WHEN
Whenever the baking application is needed.

## WHO
 Anyone who needs to do some Banking Work.

## WHAT
A smart banking system which will provide hassle free banking system.

## WHERE
Where ever there is a need of smart banking system. 

## WHY
* To save peoples time.
* To provide hassle free Banking system.

## HOW
By making system very easy to use.

# Block Diagram
![image](https://user-images.githubusercontent.com/98864424/163664641-19578003-174a-4732-b383-ae3c66399e37.png)

# UML Diagram
![image](https://user-images.githubusercontent.com/98864424/163663605-c174943c-3832-443b-a71e-bf7b17d8563a.png)

# High Level Structural Diagram
![image](https://user-images.githubusercontent.com/98864424/163365987-548abc8a-8956-4c15-9a73-636589d611de.png)

# Low Level Structural Diagram
![image](https://user-images.githubusercontent.com/98864424/163383514-64704194-f984-4d6f-a4bb-97821325fa95.png)

# Test Plan 
 | --ID | Desciption | Status | Input | Actual Output | Expected Output | Test |
 |:------------:|:-----------:|:---------:|:--------:|:--------:|:--------:|:-------:|
 | LLR1 | It shall create new account in the system with correct information | Implemented | All the correct Information | created new Account | created new Account | Passed |
 | LLR2 | It shall check if account already exists in the system | Implemented | correct account name and pin | checked if account already exists in the system or not | checked if account already exists in the system or not | Passed |
 | LLR3 | It shall show an account details only when correct account user name and psssword is inserted | Implemented | Check correct name and pin is given or not| Displayed all the account details | Displayed all the account details | Passed |
 | LLR4 | It shall not create duplicate accounts | Implemented | Account name and pin | Did not create duplicate account | Did not create duplicate account | Passed |
 | LLR5 | It shall be able to add amount in the bank system | Implemented | Add Amount to bank | Added amount to the bank | Added amount to the bank | Passed |
 | LLR6 | It shall be able to withdraw amount from the bank system | Implemented | Withdraw Amount from bank | Withdrawn amount from the bank | Withdrawn amount from the bank | Passed |
 | LLR6 | It shall be able to show the amount avilable in users bank account | Implemented | Account name and pin | Displayed account balance | Displayed account balance | Passed |
 | LLR7 | It shall be able to delete the existing account | Implemented | Account name and pin | Deleted the existing account | Deleted the existing account | Passed |

