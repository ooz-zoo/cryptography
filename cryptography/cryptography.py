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

# Get the message from the user
message = input("Enter a message: ")

# Encrypt the message
encrypted_message = encrypt(message)
print("Encrypted message:", encrypted_message)



# Decrypt the message
decrypted_message = decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)