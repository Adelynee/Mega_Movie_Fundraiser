#  import statements
import re
import pandas

# Function goes here
# WARNING: The response is returned in Title Case
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full name of the snack
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"


  # Main routine

pay_methos = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# loop until exit code ...
name = ""
while name != "xxx":
    name = input("Name: ")
    if name == "xxx":
        break
        