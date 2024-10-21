'''
BASIC QUESTION
'''

# Create a dictionary that stores a value of specific days in a month 
monthdays = {
    1: 31,
    2: 28,  #Assuming a non-leap year
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask user to input the month number that will convert to an integer 
nmonth = int(input("Enter the month number (1-12): "))

# Declare a conditional statement to check if the month number is valid and existing and output the number of days
if nmonth in monthdays:
    print(f"The number of days in month {nmonth} is {monthdays[nmonth]}.")
else: #if the input is not valid then it will show error message 
    print("Invalid month number. Please enter a number between 1 and 12.")

'''
ADVANCE QUESTION 
'''

# Create a dictionary that stores a value of specific days in a month 
monthdays = {
    1: 31,
    2: 28,  #Default value for febuarary 
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask user to input the month number that will convert to an integer 
nmonth = int(input("Enter the month number (1-12): "))



# Check if the month number is valid by using conditional statement of if 
if nmonth in monthdays:
    # Verify if the month is in February
    if nmonth == 2:
        # Ask the user if it is a leap year
        lyear = input("Is it a leap year? (yes/no): ").strip().lower()
        if lyear == "yes":
            days = 29  # Adjust for leap year
        else:
            days = 28  # Regular February
    else:
        days = monthdays[nmonth]

    print(f"The number of days in month {nmonth} is {days}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
