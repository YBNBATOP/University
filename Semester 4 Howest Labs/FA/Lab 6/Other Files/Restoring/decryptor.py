from cryptography.fernet import Fernet

# Assuming the key is stored in a variable called 'key'
key = "hfUogC40RsWhbqdeD5Ib6QBE4XQTYEUZAYhaBeOy_bw="
cipher_suite = Fernet(key)

# Open the encrypted file in binary mode
with open('Idea3.md', 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the data
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Open the file to write the decrypted data in text mode
with open('Idea3.md', 'w') as decrypted_file:
    decrypted_file.write(decrypted_data.decode())
