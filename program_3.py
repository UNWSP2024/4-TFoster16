#Timothy Foster, 2/18/25, Average Rainfall Program

#Define function.
def main():

   #Define variable to keep track of total inches of rainfall.
    totalRainfall = 0

   #Get number of years user would like to keep track of rainfall for.
    num_years = int(input("For how many years would you like to input and calculate the average rainfall?"))

   #Set up nested loop with the user's requested number of years
    for years in range (num_years):

        #Get monthly rainfall for each month of the years the user asked for.
        for months in range (12):

            #Add the user's number to the total each iteration.
            totalRainfall = totalRainfall + int(input("How many inches of rainfall were there for this month?"))

    #Calculate the total number of months.
    totalMonths = num_years * 12

   #Calculate the average rainfall for each month.
    averageRainfall = totalRainfall / totalMonths

   #Print the results.
    print(f"The total number of months was {totalMonths}.")
    print(f"The total inches of rainfall was {totalRainfall}.")
    print(f"The average rainfall per month for the {num_years} years was {averageRainfall} inches.")

if __name__ == '__main__':
    main()
