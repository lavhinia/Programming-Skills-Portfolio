



'''
 / OPTIONAL REEQUIREMENT 

'''

def passwordsystem(): #Declare a defined function for a password 
    correct_password = "12345" # Define the correct password
    
    maxattempts = 5  # Define a variable that will set the maximum number of attempts
    attempts = 0  # Start Initializing the attempts from 0 
    
    while attempts < maxattempts:  # If the attempts is less than max attempt then the condition is true 
                                    #Start the password entry loop
       
        user_input = input("Please enter the password: ")   # Ask the user for the password
        
        if user_input == correct_password: #if the condition is true then it will print the statement
            print("Access Successfully") 
            return  # return function to exit the function if the password is correct
        else:
            attempts += 1  
            
            '''By using increment the attempt counter 
            it will count the number of attempts and deduct its remaining'''
      
            remaining_attempts = maxattempts - attempts #Define a value that will deduct the max attempt and no. of attempts
            if remaining_attempts > 0: #nested if remaining attempt is greater than 0 then it will decrease the no. of attempts
                print(f"Incorrect password. You have {remaining_attempts} attempts left.") #if the condition is met it will print this statement
            else: #else if the condition exceeeded, then it will print the block warning
                print("Incorrect password. You're account is blocked.")

# Call the function to start the password process
passwordsystem()
