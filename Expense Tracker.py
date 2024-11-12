# Create a simple expense tracker where you can:
# Add expenses with a description and amount.
# View all expenses.
# Calculate the total amount spent.

# Subscriptable objects in Python are those that allow them to be indexed using the square bracket notation, such as lists, dictionaries, and strings
# Non-subscriptable objects don't support indexing operation, so will return a 'type object is not subscriptable' error

# To push updates:
# git add .
# git commit -m "Description of changes made"
# git push

from decimal import Decimal

expenseLog = {}

# This function allows users to input expenses with a description and a dollar amount
def expenseGet():
    try:    
        expAmount = Decimal(input("How much is the expense?")) # Using Decimal() due to the money nature of the input. You should pass strings to Decimal in the User input
        print(f"You submitted an expense of ${expAmount}")    
    except ValueError:
        print("You're entering a money value here dummy, so make it a number when inputting!!!!\n")
        return None
    expDisc = input("What is the expense for?")
    print(f"You submitted an expense with description {expDisc}")
    return {expDisc:expAmount}

# This function will add the user inputted expense to the bigger dictionary for storage & organization
def expenseAdd(newExpense):
    if newExpense:
        expenseLog.update(newExpense)
    return expenseLog

# This function will take the expenseLog from the expenseAdd() and pull it for user viewing. Still figuring out how to pull a key/value and print it one a single line
def expenseView(expenseDictionary):
    # Will use .keys() which pulls all keys from a dict and returns them in a form of alist
    # After the keys are in the list, I will then loop through the list, pulling the keys and values to print on a single line
    # expDictKeys = expenseDictionary.keys()
    # Using .get() to pull the value from a key-value pair
    print("Your expenses are:\n")
    for i in expenseDictionary.keys():
        # print(f"Expense: {expenseDictionary[i]}: ${expenseDictionary.get(i)}\n")
        print(f"${expenseDictionary[i]}\n| {i}")
    




# This function will pull all values from the expenseLog dict and sum them together
def totalExpenseCalc(expenseDictionary):
    # Will use .values() to pull all values into a list
    # Then sum() the list to find the total expenses
    expDictValues = expenseDictionary.values()
    return round(sum(expDictValues),2)


print("Welcome user to the expense tracker 'SNAKE EDITION' TM\n")

while True:
    userChoice = input("What would you like to do? Type the option you would like\n\
          ADD - You can add an expense and its description\n\
          VIEW - You can view all expenses and their descriptions\n\
          CALC - You can calculate the sum of all your expenses\n\
          BREAK - To quit this program and go kiss your loved one <3\n")
    if userChoice == "ADD":
        newExp = expenseGet()
        expenseAdd(newExp)
    elif userChoice == "VIEW":
        expenseView(expenseLog)
    elif userChoice == "CALC":
        print(f"Your total expenses sum up to: {totalExpenseCalc(expenseLog)}")
    else:
        break
    
          
