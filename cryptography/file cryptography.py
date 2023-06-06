

import string

# Define the alphabet
alphabet = string.ascii_lowercase

# Define the key
key = 'qwertyuiopasdfghjklzxcvbnm'

# Define the encryption function
def encrypt(message):
    encrypted_message = ''
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_char = key[index]
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Define the decryption function
def decrypt(message):
    decrypted_message = ''
    for char in message:
        if char in key:
            index = key.index(char)
            decrypted_char = alphabet[index]
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def encrypt_file(file_path, encrypted_file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        encrypted_content = encrypt(content)
    with open(file_path, 'w') as file:
        file.write(encrypted_content)

def decrypt_file(file_path, decrypted_file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        decrypted_content = decrypt(content)
    with open(file_path, 'w') as file:
        file.write(decrypted_content)


# Usage example
file_path = 'encrypted.txt'
encrypted_file_path = 'decrypted.txt'

# Encrypt the file
encrypt_file(file_path, encrypted_file_path)
print(f"File '{file_path}' encrypted and saved as '{encrypted_file_path}'.")

# Decrypt the file
decrypt_file(encrypted_file_path, file_path)
print(f"File '{encrypted_file_path}' decrypted and saved as '{file_path}'.")
