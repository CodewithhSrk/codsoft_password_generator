
import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
   
    length = int(input("Number of  password length: "))
    alphabets_count = int(input("Number of  alphabets in password: "))
    digits_count = int(input("Number of digits in password: "))
    special_characters_count = int(input("Number of special characters in password: "))
    
    characters_count = alphabets_count + digits_count + special_characters_count

    if characters_count > length:
        print("Total count of characters is greater than the password length.")
        return

    password = []

    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    for i in range(digits_count):
        password.append(random.choice(digits))

    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))
            
    random.shuffle(password)

    print("Generated Password:", "".join(password))

generate_random_password()
