# This is the default to use the generate function from password_generator.py

def main():
    from password_generator import generate # Import the generate function from password_generator.py
    from sys import argv # Import the argv module from sys

    while True:
        print("Welcome to the password generator!\nIf you want to exit type 'exit' at any time!")
        usage = ""
        length = ""

        if len(argv) == 1: # If there are no arguments
            usage = input("What is the password for? ") # Ask the user what the password is for
            if usage == "exit": # If the user types exit, exit the program
                print("Goodbye!")
                break
        else: # Make the first argument into the usage of the password
            usage = argv[1]

        if len(argv) == 1 or len(argv) == 2:
            length = input("How long should the password be? ") # Ask the user how long the password should be
            if length == "exit":
                print("Goodbye!")
                break
        else: # Make the second argument into the length of the password
            length = argv[2]

        try: # Try to convert the length to an integer
            generate(usage, int(length)) # If it works, use the generate function from password_generator.py
            if len(argv) >= 2: # If you use arguments than the program will just break to save you time
                break
        except ValueError:
            print("Please enter a number for the password length!")
            continue



main() # Run the main function

# Now check the pass.txt anytime for your passwords!
# Enjoy your new password generator!
# Check out my other projects on my GitHub: https://github.com/ThatBlokeJosh