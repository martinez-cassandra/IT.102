#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Cassandra

# Import necessary Python Modules
import os
import crypt

# Function to test password
def test_password(algorithm_salt, hashed_password, password_guess):
    """Test if a password guess matches the hashed password."""
    try:
        # Use provided algorithm/salt and plaintext password, create hash
        hashed_guess = crypt.crypt(password_guess, algorithm_salt)
        # Compare hashed_password with the just created hash
        return hashed_guess == hashed_password
    except OSError as e:
        # Handle invalid salt/algorithm format
        print(f"Error with crypt: {e}")
        return False

# Open dictionary file 
dir_path = os.path.dirname(os.path.realpath(__file__))
dictionary_path = os.path.join(dir_path, "top10.txt")

try:
    with open(dictionary_path, "r") as f:
        passwords = f.readlines()
except FileNotFoundError:
    print(f"Error: Could not find {dictionary_path}")
    print("Please ensure top10.txt is in the same directory as this script.")
    exit(1)

# Prompt user for Algorithm/salt
algorithm_salt = input("What is the algorithm and salt? ")

# Prompt user for salted hash
hashed_password = input("What is the hashed password? ")

# Loop through each password
match_found = False
for password in passwords:
    password = password.strip()
    if not password:  # Skip empty lines
        continue
    
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        # If a match is found, print and quit
        print(f"Match Found: {password}")
        match_found = True
        break

if not match_found:
    print("No match found in dictionary.")