#!/usr/bin/env python3
# AES Encryption and Decryption
# Implement AES encryption and decryption using Python's cryptography library
# By Cassandra

# These libraries
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Dealing with encryption which is THE KEY
key = os.urandom(32) # This is a 256-bit AES key
iv = os.urandom(16) # This is a 128-bit IV

#Encrypt the message (HOW DO WE DO THIS)
plaintext = b'Confidential message from Cassandra'
# At a minimum it requires 16 bytes
padder = padding.PKCS7(128).padder()
padded_data = padder.update(plaintext) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

#Creating an Encryption

#OUTPUT
print("Ciphertext:", ciphertext.hex())

#Decrypting (Reverse of Encrypting)

decryptor = cipher.decryptor()
decrypted_packets = decryptor.update(ciphertext) + decryptor.finalize()

#Unpad the decrypted packets
unpadder = padding.PKCS7(128).unpadder()
decrypted_data = unpadder.update(decrypted_packets) + unpadder.finalize()

print ("Decrypted:", decrypted_data.decode())