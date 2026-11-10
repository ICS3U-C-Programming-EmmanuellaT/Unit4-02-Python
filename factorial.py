#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on11th november, 2026
# This program asks the user for a factorial number as an integer
# and calculates the factorial of that number.in a true while loop and
# catches errors that are not integers and displays
# an error message to the user.


def main():
    # get the number from the user
    user_number = input("Enter a number ")
    while_counter = 0
    factorial = 1
    # get the number from the user and convert to an integer
    try:
        user_number = int(user_number)
        if user_number >= 0:
            if user_number == 0 or user_number == 1:
                print(
                    "The factorial of {user_number} is 1".format(
                        user_number=user_number
                    )
                )
            else:
                while while_counter < user_number:
                    while_counter += 1
                    factorial *= while_counter
                print(
                    "The factorial of {user_number} is {factorial}".format(
                        user_number=user_number, factorial=factorial
                    )
                )
        else:
            print(
                "{user_number} is not a positive number, please enter a positive number".format(
                    user_number=user_number
                )
            )
    except Exception:
        print(
            "{user_number} is not a valid number, enter a valid integer".format(
                user_number=user_number
            )
        )


if __name__ == "__main__":
    main()
