#Timothy Foster, 2/19/25, Bank Balance Program

def main():

    #Define all of the variables that will be used.
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    #Ask for budget for the month.
    budget = int(input ("What is your budget for this month?"))

    #Start while loop.
    while spent == 1.0:

        #Get the name of an expense.
        expenseName = input("What is the name of an expense?")

        #Ask for the cost of the expense.
        total = total + int(input(f"How much does {expenseName} cost you?"))

        #See if user has more expenses to add.
        spent = int(input("Do you have more expenses for this month? Enter 1 if so and 0 if not."))

    #Calculate if the user if under/over/on budget.
    difference = int(budget - total)

    #Print the results based on the difference.
    if difference > 0:
        print(f"You are under budget by {difference}.")
    elif difference == 0:
        print("You are exactly on budget.")
    else:
        print(f"You are over budget by {difference//-1}.")

if __name__ == '__main__':
    main()
