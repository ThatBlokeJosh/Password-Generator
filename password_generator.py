import random
import os

numbers = "0123456789"
alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "+-*/#$@&!~%?"
password = []
pass_use = input("What is this password for? ")
pass_length = int(input("Password length: "))


def generate():
    for i in range(pass_length):
        random_number = random.randint(0, 3)

        if random_number == 0:
            password.append(numbers[random.randint(0, 9)])

        elif random_number == 1:
            password.append(alphabet[random.randint(0, 25)])
        
        elif random_number == 2: 
            password.append(upper_alphabet[random.randint(0, 25)])

        elif random_number == 3:
            password.append(symbols[random.randint(0, 11)])


generate()
    
password_text = "".join([str(item) for item in password])
print(f"Your password: {password_text}")

file_path = './pass.txt'
file_exists = os.path.isfile(file_path)

f = open(file_path, 'a')
f.write(f'{pass_use} password: {password_text}\n')

f.close()


