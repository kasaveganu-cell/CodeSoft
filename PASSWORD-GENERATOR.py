import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters     
    digits = string.digits              
    symbols = string.punctuation        

    # Combine all characters
    all_characters = letters + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password


# User Input
try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Please enter a valid positive number.")
    else:
        password = generate_password(length)

        # Display Password
        print("Generated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")