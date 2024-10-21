'''
BASIC QUESTION
'''


correct_password = "12345" # Define the correct password


user_input = "" # Initialize a variable to store the user's input


while user_input != correct_password: # Use a while loop to repeatedly ask for the password until it matches the correct one
    user_input = input("Enter the password: ")
    if user_input == correct_password: #The program uses a while loop to repeatedly ask the user to enter a password until the input matches the correct password.
        print("Password accepted!") #If the user enters the correct password, the program prints "Password accepted!" and exits the loop.
    else:
        print("Incorrect password. Try again.") #If the user enters an incorrect password, it prompts the user to try again.
