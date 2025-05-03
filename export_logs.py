# export_logs.py
import os
from encryptor import decrypt_data

HOME_DIR = os.path.expanduser('~')
HIDDEN_FILE_PATH = os.path.join(HOME_DIR, '.my_secret_keystrokes')
KEY_FILE_PATH = os.path.join(HOME_DIR, '.my_secret_key')
EXPORT_PATH = os.path.join(HOME_DIR, 'my_keystrokes_export.txt')

def export_logs():
    with open(KEY_FILE_PATH, 'rb') as kf:
        key = kf.read()
    with open(HIDDEN_FILE_PATH, 'rb') as f:
        lines = f.readlines()

    with open(EXPORT_PATH, 'w') as out:
        for line in lines:
            decrypted = decrypt_data(line.strip(), key)
            out.write(decrypted + '\n')

    print(f"✅ Logs exported to {EXPORT_PATH}")

if __name__ == "__main__":
    export_logs()
