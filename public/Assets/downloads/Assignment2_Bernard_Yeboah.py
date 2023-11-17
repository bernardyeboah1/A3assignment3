import sys


# Define function
def main():
    # OPERATIONS
    # 1.  Add
    # 2. Subtract
    # 3. Multiply
    # 4.  Divide
    # 5. Raise exponents
    print(""" Please select an operation to perform by typing the operation """)
    print("1. Addition = add")
    print("2. Subtraction = subtract")
    print("3. Multiplication = multiply")
    print("4. Division = divide")
    print("5. Raise exponents = raise exponents")
    print("6. Or enter 'Q' to exit")
    operation = input(": ").lower()

    if operation == 'q'.lower():
        # Allow user to quit
        sys.exit("You quit the program")

    if operation == "add":
        # Perform addition
        try:
            number_1 = int(input("Please enter your first number"))
            number_2 = int(input("Please enter your second number"))
            result_1 = number_1 + number_2
            print(f"{number_1} + {number_2} = {result_1}")
        except ValueError as ERROR:
            print("Perhaps you made a mistake? \n")
            print(f"You went wrong here : {ERROR}")
            retry1 = input("Would you like to try again? Yes or No?: ")
            if retry1 == 'Yes'.lower():
                main()
            elif retry1 == 'No'.lower():
                exit()

    elif operation == "subtract":
        # Perform subtraction
        try:
            number_3 = int(input("Please enter your first number"))
            number_4 = int(input("Please enter your second number"))
            result_2 = number_3 - number_4
            print(f"{number_3} - {number_4} = {result_2}")
        except ValueError as Error:
            print("Perhaps you made a mistake? \n")
            print(f"You went wrong here : {Error}")
            retry2 = input("Would you like to try again? Yes or No?: ")
            if retry2 == 'Yes'.lower():
                main()
            elif retry2 == 'No'.lower():
                exit()

    elif operation == "multiply":
        # Perform multiplication
        try:
            number_5 = int(input("Please enter your first number"))
            number_6 = int(input("Please enter your second number"))
            result_3 = number_5 * number_6
            print(f"{number_5} x {number_6} = {result_3}")
        except ValueError as Error:
            print("Perhaps you made a mistake? \n")
            print(f"You went wrong here : {Error}")
            retry3 = input('Would you like to try again? Yes or No?: ')
            if retry3 == 'yes'.lower():
                main()
            elif retry3 == 'No'.lower():
                exit()


    elif operation == "divide":
        # Perform division
        try:
            number_6 = int(input("Please enter your first number"))
            number_7 = int(input("Please enter your second number"))
            result_4 = number_6 / number_7
            print(f"{number_6}/ {number_7} = {result_4}")
        except ValueError as Error:
            print("Perhaps you made a mistake? \n")
            print(f"You went wrong here: {Error}")
            retry4 = input("Would you like to try again? Yes or No?: ")
            if retry4 == 'yes'.lower():
                main()
            elif retry4 == 'no'.lower():
                exit()

    elif operation == "raise exponents":
        # Perform power
        try:
            def raise_to_power():
                base_num = int(input("Please enter a number"))
                power_num = int(input("Please enter a number"))
                result = 1
                for index in range(power_num):
                    result = result * base_num
                print(f"{base_num} ^ {power_num} = {result}")

            raise_to_power()
        except ValueError as Error:
            print("Perhaps you made a mistake? \n")
            print(f"You went wrong here: {Error}")
            retry5 = input("Would you like to try again?: ")
            if retry5 == 'yes'.lower():
                main()
            elif retry5 == 'no'.lower():
                exit()

    else:
        print("Invalid entry, please try again!")

    # Ask user if they want to restart
    restart = input("""If you'd like to use the calculator again please enter 'Yes' to continue, if not, please enter 
    'exit' to exit """).lower()
    if restart == "yes":
        main()
    elif restart == "exit":
        exit()


# Where code starts
main()
