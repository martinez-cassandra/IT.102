#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Cassandra

# rot13 - caesar cipher with a shift of 13

def rot13(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

message = input("input your text to rotate no spaces or numbers: ")
shift = 13
encrypted = rot13(message, shift)
decrypted = rot13(encrypted, -shift)

print(f"encrypted {encrypted}")
print(f"decrypted {decrypted}")