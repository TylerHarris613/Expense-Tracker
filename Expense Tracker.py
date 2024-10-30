# Create a simple expense tracker where you can:
# Add expenses with a description and amount.
# View all expenses.
# Calculate the total amount spent.

# To push updates:
# git add .
# git commit -m "Description of changes made"
# git push

from decimal import Decimal

# This function allows users to input expenses with a description and a dollar amount
def expenseGet():
    try:    
        expAmount = Decimal(input("How much is the expense?")) # Using Decimal() due to the money nature of the input. You should pass strings to Decimal in the User input
        print(f"You submitted an expense of ${expAmount}")    
    except ValueError:
        print("You're entering a money value here dummy, so make it a number when inputting!!!!\n")
    expDisc = input("What is the expense for?")
    print(f"You submitted an expense with description {expDisc}")
    return {expDisc:expAmount}

# This function will add the user inputted expense to the bigger dictionary for storage & organization
def expenseAdd(expenseDisc, expenseAmount):
    expenseLog = {}
    expenseLog.update({expenseDisc:expenseAmount})
    return expenseLog

# This function will take the expenseLog from the expenseAdd() and pull it for user viewing
# def expenseView(expenseDictionary):




def totalExpenseCalc(expenseDictionary):
    expenseSum = 0
    for key in expenseDictionary.keys():
        expenseSum += expenseDictionary[key]
    return expenseSum


print("Welcome user to the expense tracker 'SNAKE EDITION' TM\n")

while 0<1:
    userChoice = input("What would you like to do?\
          Type the option you would like\n\
          ADD - You can add an expense and its description\n\
          VIEW - You can view all expenses and their descriptions\n\
          CALC - You can calculate the sum of all your expenses\n\
          BREAK - To quit this program and go kiss your loved one <3\n")
    if userChoice == "ADD":
        newExp = expenseGet
        expenseAdd(newExp)
    elif userChoice == "VIEW":
        print(f"Your expenses are {expenseAdd}")
    elif userChoice == "CALC":
        print(f"Your total expenses sum up to: {totalExpenseCalc(expenseAdd)}")
    else:
        break
    
          
