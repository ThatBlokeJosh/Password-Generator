def generate(pass_use, pass_length): # Define the generate function
    import random # Import the random module

    numbers = "0123456789" # Define all the characters that can be used in the password
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "+-*/#$@&!~%?"
    password = [] # Define the password list

    for i in range(pass_length): # For the length of the password
        random_number = random.randint(0, 3) # Generate a random number between 0 and 3

        if random_number == 0: # Check the random number
            password.append(numbers[random.randint(0, 9)]) # If the random number is 0, add a random number to the password

        elif random_number == 1:
            password.append(alphabet[random.randint(0, 25)]) # If the random number is 1, add a random lowercase letter to the password
        
        elif random_number == 2: 
            password.append(upper_alphabet[random.randint(0, 25)]) # If the random number is 2, add a random uppercase letter to the password

        elif random_number == 3:
            password.append(symbols[random.randint(0, 11)]) # If the random number is 3, add a random symbol to the password
    
    password_text = "".join([str(item) for item in password]) # Join the list into a string
    print(f"Your password: {password_text}")

    file_path = './pass.txt' # Define the file path and write the password to the file
    f = open(file_path, 'a')
    f.write(f'{pass_use} password: {password_text}\n')

    f.close() # Enjoy your new password!

# Feel free to use this as a library or use the run file for the default usage of this function    
# Check out my other projects on my GitHub: https://github.com/ThatBlokeJosh
