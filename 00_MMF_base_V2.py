# import statements
import re
import pandas


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
    error = "Please enter a whole number that is more than 12 and less than 130"

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


# Checks number of tickets left and warn user
# if maximum is being approached
def check_ticket(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats left".format(ticket_limit - tickets_sold))

    # warns user that only one seat is left
    else:
        print("*** There is ONE seat left!! ***")

    return ""


# Gets ticket price based on age
def get_ticket_price():
    # Get age ( between 12 and 130 )
    age = int_check("Age: ")

    # check that sge is valid
    if age < 12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - it looks like  mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price


# ******************* Main Routine **************


# Set up dictionaries / lists needed to hold date


# initialise loop so that it runs at least once

MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists ( to make data - frame in due course )
all_names = []
all_tickets = []

# Data Frame Dictionary
movie_dad_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# Ask user if they have used the program before & show instruction

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # checks number of ticket limit has not been exceeded...
    check_ticket(ticket_count, MAX_TICKETS)

    # **** Get details for each ticket ... ****

    # Get name ( can't be blank )
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # Get ticket price based on age
    ticket_price = get_ticket_price()
    # if age is invalid, restart loop ( and get name again )
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # add names and ticket price lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks

    # Get payment method ( ie: work out if surcharge is needed )

# End of tickets / snacks / payment loop

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# Calculate ticket profit ...
ticket_profit = ticket_price - (5 * ticket_count)
print("Ticket profit: $ {:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets ...
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")





