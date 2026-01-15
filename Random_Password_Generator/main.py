import random

length = int(input("Enter the desired length of the password: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'      
include_special = input("Include special characters? (y/n): ").lower() == 'y'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!@#$%^&*()-_=+[]{}|;:,.<>?/`~'
character_pool = lowercase_letters
if include_uppercase:
    character_pool += uppercase_letters
if include_numbers:
    character_pool += numbers
if include_special:
    character_pool += special_characters
if length < 1:
    print("Password length must be at least 1.")
else:
    password = ''.join(random.choice(character_pool) for _ in range(length))
    print(f"Generated password: {password}")    
print("Thank you for using the Random Password Generator!")

