from cryptography.fernet import Fernet


# Generate the key to use for the encryption and decryption
key = Fernet.generate_key()
keys = Fernet(key)


# The plain text to encrypt goes here
text = b'Ologo didan'

# Encrypt here
token = keys.encrypt(text)
print(token)

# Decrypt here
decrypted = keys.decrypt(token)
print(decrypted)
