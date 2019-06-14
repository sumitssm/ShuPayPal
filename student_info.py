import math

class Student:
    def __init__(self, first, last, student_id):
        self.first=first
        self.last=last
        self.student_id=student_id


first_name=input("What is you first name \n")
last_name=input("What is you last name \n")
student_id=input("What is your student_id \n")
starting_bal=float(input("What is your starting balance \n"))
student_1=Student(first_name, last_name, student_id)

class math_add:
    def __init__(self, starting_bal, transaction_bal):
        starting=int((starting_bal)*100)
        transaction=int((transaction_bal)*100)
        self.end_bal=((starting+transaction)/100)

class math_subtract:
    def __init__(self, starting_bal, transaction_bal):
        starting=int((starting_bal)*100)
        transaction=int((transaction_bal)*100)
        self.end_bal=((starting-transaction)/100)

continue_transaction = "Y"
while continue_transaction == "Y":
    while True:

        action=input("Are you making a deposit or withdrawal?\n please enter \"W\" for withdrwal or \"D\" for deposit \n ")
        if action == "D" or action == "W":
            break
        else:
            print(action + " is an Invalid Entry. Try again \n")

    while True:
    
        transaction_bal=float(input("Please enter the amount \n"))
        if transaction_bal < 0:
            print("Invalid entry, enter an amount greater than 0")
        elif action == "W" and transaction_bal > starting_bal:
            print("Not enough funds to withdraw that amount")
        else:
            break
        
    if action == "W":
        balance=math_subtract(starting_bal, transaction_bal)
    elif action == "D":
        balance=math_add(starting_bal, transaction_bal)

    print("Your new balance is:" , balance.end_bal)

    starting_bal=balance.end_bal
    
    while True:
        
        more_transaction=input("Would you like to do another transaction? \n please enter \"Y\" or \"N\" \n")
        if more_transaction =="N" or more_transaction == "Y":
            continue_transaction = more_transaction
            break
        else:
            print("Invalid entry")
