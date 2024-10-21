'''
NUMBER 3


BASIC QUESTION:
'''


# First step is to  store the needed data or information in a dictionary
info = { 
    "name": "John Doe", #Declare the first given information which is name
    "hometown": "New York", #Declare the first given information which is hometown
    "age": 25 #Declare the third given which is an integer age
}

# Print the values on separate lines using a single print() statement
print(f"Name: {info['name']}\nHometown: {info['hometown']}\nAge: {info['age']}")



'''

ADVANCE QUESTION:

    '''

# First we need to create a function to ensure that age is a valid number or integer 
def getage():
   
    while True: #Create a statement where stating that it is true 
        agenum = input("Enter your age: ") #Declare a variable that will store the input of the user and print
        try:
            age = int(agenum)  # Try converting the input to an integer
            return age  # Return if successful
        except ValueError:
            print("Please enter a valid integer for age.")  # Retry if failed

# Get user input for name, hometown, and age
name = input("Enter your name: ")  # Declare a variable that will store the input
hometown = input("Enter your hometown: ") # Declare a variable that will store the input
age = getage()  # Declare to use the function to ensure we get a valid integer for age

# Store the information in a dictionary
info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print the values on separate lines using a single print() statement
print(f"Name: {info['name']}\nHometown: {info['hometown']}\nAge: {info['age']}")
