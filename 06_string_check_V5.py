import re


def string_check(choice, options):
    for var_list in options:

        # if the snack is in the one of the lists, return the full name
        if choice in var_list:

            # Get full name of snack and put it
            # in title case os it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valif to not
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# regular expression to find if the item starts with a number
number_regex = "^[1-9]"

# valid snacks holds list of all snacks
# Each item in valid snacks is a list with
# valid options for each snack <full name, letter code ( a - 3)
# , and possible abbreviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "o", "juice", "e"]
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# holds snack order for a single user
snack_order = []

# ask user if they want a snack

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)
    if check_snack == "invalid choice":
        print("Please enter a valid options")
        print()

# If they say yes, ask what snacks they want ( and add to our to out snack list )
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for desired snack and put it in lower case
        desired_snack = input("Snack :").lower()

        if desired_snack == "xxx":
            break

        # if item has a number, separate it into two ( number / item )
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)
        if snack_choice == "invalid choice":
            print("Please enter a valid options")
            print("")

        # check snack amount is valid ( less than 5 )
        if amount >= 5:
            print("Sorry - we have a four maximum")
            snack_choice = "invalid choice"

        # add snack AND amount to list...
        amount_snack = "{} {}".format(amount, snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(amount_snack)

    # show snack orders
    print()
    if len(snack_order) == 0:
        print("Snacks Ordered: None")

    else:
        print("Snacks Ordered:")

        for item in snack_order:
            print(item)
