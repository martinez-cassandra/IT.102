#!/usr/bin/env python3
# Script that Generates a Password
# By Cassandra


import random
import string

def create_password():
    print("\n--- Secure Password Generator ---")

    # Ask for password length
    while True:
        try:
            length = int(input("How long should the password be? (Minimum 8): "))
            if length < 8:
                print("Password must be at least 8 characters long.")
            else:
                break
        except ValueError:
            print("Please enter a number.")

    # Ask what types of characters to include
    use_upper = input("Include uppercase letters (A-Z)? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters (a-z)? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers (0-9)? (y/n): ").lower() == "y"
    use_symbols = input("Include special characters (!@#$...) ? (y/n): ").lower() == "y"

    # Make sure the user picked at least one type
    if not (use_upper or use_lower or use_numbers or use_symbols):
        print("You must choose at least one character type!")
        return None

    # Character groups
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    number_digits = string.digits
    special_symbols = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

    # Build a list of selected groups
    chosen_groups = []
    if use_upper:
        chosen_groups.append(uppercase_letters)
    if use_lower:
        chosen_groups.append(lowercase_letters)
    if use_numbers:
        chosen_groups.append(number_digits)
    if use_symbols:
        chosen_groups.append(special_symbols)

    # Start building the password with at least one character from each chosen group
    password_characters = []
    for group in chosen_groups:
        password_characters.append(random.choice(group))

    # Combine all selected groups into one grouping
    all_allowed_characters = "".join(chosen_groups)

    # Add random characters until we reach the required length
    while len(password_characters) < length:
        password_characters.append(random.choice(all_allowed_characters))

    # Shuffle so the order isn't predictable
    random.shuffle(password_characters)

    # Turn list into a string
    return "".join(password_characters)


# Program loop
while True:
    new_password = create_password()

    if new_password:
        print("\nYour secure password is: ", new_password)

    repeat = input("\nWould you like to make another password? (y/n): ").lower()
    if repeat != "y":
        print("Have a great day!")
        break