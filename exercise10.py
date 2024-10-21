'''
EXERCISE 10
'''


def is_even(number): #Define a function 

 #Check if the number is even.
    #This function checks if a number is even by returning True 
    #if number % 2 == 0 (even) and False otherwise (odd)
  
    return number % 2 == 0 

def main():
   
    # Ask the user for a number
    user_input = input("Please enter a number: ")
    
    # Attempt to convert the input to an integer and Prompts the user for a number and attempts to convert it to an integer.
    try:
        number = int(user_input)
        
        # Determine if the number is even or odd
        if is_even(number): #If the conversion is successful, it calls the is_even function to check if the number is even.
            print(f"{number} is even.")
        else: #Depending on the result from is_even, it prints whether the number is even or odd
            print(f"{number} is odd.")
    except ValueError: #If the conversion fails, it prints an error message.
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

