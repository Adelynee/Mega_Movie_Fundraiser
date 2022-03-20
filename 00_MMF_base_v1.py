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

        # If name is not blank, show error ($ repeat loop)

        else:
            print(error_message)


# Main Routine goes here

name = not_blank("Name: ", "Sorry - this can't be blank, "
                           "please enter your name")


#  ----   Main Routine   -----

# Set up dictionaries / Lists needed to gold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

    # Get name (can't be blank)

    name = not_blank("Name: ")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method ( and apply surchage if necesary )

# Calculate Total sales and profit

# Output data to text files