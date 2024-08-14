from cryptography.fernet import Fernet

def load_key():
    with open("Fernet_w.k", "rb") as key_file:
        return key_file.read()

def decrypt_log():
    key = load_key()
    cipher_suite = Fernet(key)

    with open('Kr_encrypted.txt', 'rb') as log:
        encrypted_data = log.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open('Kr_decrypted.txt', 'w') as log:
        log.write(decrypted_data.decode())

decrypt_log()
print("Decryption complete. It is in file decrypted.")



