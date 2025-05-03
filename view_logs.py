# view_logs.py
import os
from encryptor import decrypt_data
import getpass

HOME_DIR = os.path.expanduser('~')
HIDDEN_FILE_PATH = os.path.join(HOME_DIR, '.my_secret_keystrokes')
KEY_FILE_PATH = os.path.join(HOME_DIR, '.my_secret_key')

# Simple hardcoded password (you can change it here)
ACCESS_PASSWORD = "mytracker123"

def view_logs():
    pwd = getpass.getpass("Enter viewer password: ")
    if pwd != ACCESS_PASSWORD:
        print("❌ Incorrect password.")
        return

    with open(KEY_FILE_PATH, 'rb') as kf:
        key = kf.read()
    with open(HIDDEN_FILE_PATH, 'rb') as f:
        lines = f.readlines()

    if not lines:
        print("📂 No logs yet.")
        return

    print("\n📋 Your Logs:")
    print("-" * 50)
    for idx, line in enumerate(lines, 1):
        decrypted = decrypt_data(line.strip(), key)
        print(f"{idx}. {decrypted}")

    print("-" * 50)
    print(f"Total sentences typed: {len(lines)}")

if __name__ == "__main__":
    view_logs()
