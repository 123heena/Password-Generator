import random
import string

def generate_password(length=12):
    """Generate a secure random password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input for password length
try:
    length = int(input("Enter password length (minimum 8): "))
    if length < 8:
        print("Password length should be at least 8 characters!")
    else:
        print(f"Generated Password: {generate_password(length)}")
except ValueError:
    print("Invalid input! Please enter a number.")
