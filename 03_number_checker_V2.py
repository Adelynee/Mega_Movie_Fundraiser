# functions goes here


# Checks for an intger more than 0
def int_check(question):

    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

            # ask user for number nd check it is valid
            try:
                response = int(input(question))

                if response <= 0:
                    print(error)
                else:
                    return response