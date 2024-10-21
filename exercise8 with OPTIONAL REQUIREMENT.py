'''
BASIC QUESTION 
EXERCISE 8
'''
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #Create a list of names and intialize them

search_name = "Sam" # Define the name to search for Sam

if search_name in names: # Search for the name in the list. If the condition is true then print the statement
    print(f"{search_name} found in the list!") #Print if the condition is met 
else:
    print(f"{search_name} not found in the list.") #Else print if condition is false



'''
OPTIONAL REQUIREMENT 
'''

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #Create a list of names and intialize them

# Allow the user to input the search term
search_term = input("Enter the name you want to search for (or press Enter to search for 'Sam'): ")

#If the user didn't enter a name, default to searching for "Sam"
if not search_term:
    search_term = "Sam" 

# Search for the name in the list
if search_term in names: #If the condition is true then print the statment
    print(f"{search_term} found in the list!")
else: #if condition is false then print the statement 
    print(f"{search_term} not found in the list.")
