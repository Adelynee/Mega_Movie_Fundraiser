# function goes here


# Checks for an integer more than 0
def int_check(question) :
    print("test")
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

def int_check(question, low_num, high_num):

            error = "Please enter a whole number between {} " \
                    "and {}".format(low_num, high_num)

            valid = False
            while not valid:

                # ask user for a number and check it is valid
                try:
                    response = int(input(question))

                    if low_num <= response <= high_num:
                        return response
                    else:
                        print(error)

                # if an integer is nt entered, display an error
                except ValueError:
                    print(error)