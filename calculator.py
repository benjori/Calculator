def welcome():
    print('''
Welcome to the Calculator
''')

# Define our function
def calculate():
    operation = input('''
Please type in the math opperation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''') 
    try:
        number_1 = int(input('Enter your first number '))
        number_2 = int(input('Enter your second number: '))
    except ValueError:
        print('Please input numbers only')
        again()

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        try: 
            print(number_1 / number_2)
        # Add try and except in case of ZeroDivisionError
        except ZeroDivisionError:
            print(0)

    else:
        print('You have not typed a valid opperator, please run the program again.')

    # Add again() function to calculate() function
    again()

# Define again() function to ask user if they want to use the calculator again
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for Yes or N for No.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
       print('See you later.')
       quit()

    # If user types another key, run the function again
    else:
        again()

# Call calculate() outside of the function
welcome()
calculate()
