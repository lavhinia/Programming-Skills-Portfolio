
'''
BASIC QUESTION 
'''

# Create a user input that will ask for the capital of france 
answer = input("What is the capital of France? ").strip() 
''' 
Declare a variable that will store users input and a strip function to give user a space 
or remove whitespaces 

'''

# Check if the answer is the same exactly "Paris" with proper capitalization
if answer == "Paris": #Declare a conditional statement that if the answer is 'Paris' it should be true and print
    print("Correct! The Capital of France is",answer)
else: #Declare an else statement if the answer is false 
    print("Wrong. The correct answer is Paris.")

'''
ADVANCE QUESTION
'''

answeruser = input("What is the capital of France? ") # Declare a variable and create an input statement that will ask the user

# Create an if else statement that will allow the system to read answer 
if answeruser.strip().lower() == "paris": #use lower() in order to ignore the capitalization
    print("Correct! The capital of France is Paris.") #print the statement 
else:
    print("Wrong! The correct answer is Paris.") #if the statement is not correct 



# Create a dictionary with a list of countries and their capitals
# It allows to store 10 European countries with their capitals
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Sweden": "Stockholm",
    "Portugal": "Lisbon",
    "Greece": "Athens"
}

# Start the quiz
print("WELCOME to the EUROPEAN CAPITAL Quiz! Goodluck and let's test your KNOWLEDGE")
score = 0

'''Declare a for loop that will allow to read the country-capital pair in the dictionary through each country 
and ask the user for its capital'''

for country, capital in capitals.items():
    #Ask the question and get user's answer
    answer = input(f"What is the capital of {country}? ").strip()

    #Check if the answer is correct (case-insensitive)
    #By using the function of .lower() it allows to use lowercase to read any capitalization
    if answer.lower() == capital.lower():
        print("Correct!")
        score += 1 #If the user answer is correct it will increment the score value by 1
    else:
        print(f"Wrong. The capital of {country} is {capital}.")

#Display the final score
print(f"\nQuiz Complete! Your score: {score} out of {len(capitals)}")
