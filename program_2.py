#Timothy Foster, 2/18/25, Movie Tix Program

def main():
    ######################

    #Define variable to keep track of number of tickets.
    movieTix = 0

    #Define variable for while loop.
    moreMovies = "Yes"

    while moreMovies == 'Yes':
        #Get user input for the name of a movie.
        movieTitle = input("Enter the name of a movie you would like to see.")

        #Get user input for the number of tickets desired and add this to the total so far.
        movieTix = movieTix + int(input(f"How many tickets would you like for {movieTitle}?"))

        #See if the user would like to continue.
        moreMovies = input("Would you like to see more movies? Answer 'Yes' if so.")

    #Display the total number of tickets requested.
    print(f"The total number of tickets you would like is {movieTix}.")


    ######################


if __name__ == '__main__':
    main()
