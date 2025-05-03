# view_logs.py
import os
from encryptor import decrypt_data

HOME_DIR = os.path.expanduser('~')
HIDDEN_FILE_PATH = os.path.join(HOME_DIR, '.my_secret_keystrokes')
KEY_FILE_PATH = os.path.join(HOME_DIR, '.my_secret_key')

def view_logs():
    with open(KEY_FILE_PATH, 'rb') as kf:
        key = kf.read()
    with open(HIDDEN_FILE_PATH, 'rb') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines, 1):
        decrypted = decrypt_data(line.strip(), key)
        print(f"{idx}. {decrypted}")

if __name__ == "__main__":
    view_logs()
