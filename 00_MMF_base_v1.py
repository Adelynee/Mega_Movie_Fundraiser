# import statements


# functions go here

# checks that ticket name is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        # If name in not blank, program continues

        if response != "":
            return response

        # If name is not blank, show error (& repeat loop)

        else:
            print(error_message)


def int_check(question):
    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
                print(error)

# checks for an integer between two values


#  ----   Main Routine   -----

# Set up dictionaries / Lists needed to gold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

# Initialise loop so that it runs at least once
# Start of loop

# Initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats left".format(MAX_TICKETS - count))

    # Warns user that one seat is left!
    else:
        print("*** There is ONE seat left!! ***")


    # Get details...
    name = input("Name: ")

    # end the lo[ if the exit code is entered
    if name == "xxx":
        break

    # main routine goes here
    age = int_check("Age: ")

    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like  mistake")
        continue

    count += 1

    #if count == MAX_TICKETS:
        #print("You have sold all the available tickets!")
    #else:
        #print("You have sold {} tickets. \n"
              #"There are {} places still available".format(count, MAX_TICKETS - count))

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method ( and apply surchage if necesary )

# Calculate Total sales and profit

# Output data to text files