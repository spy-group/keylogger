# PrivacyGuard Keylogger

**PrivacyGuard Keylogger** is a Python-based keylogging tool designed for educational purposes. It records keyboard activity in an encoded binary format, stores logs in specified files, and detects specific password entries.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [How It Works](#how-it-works)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About the Project

This project demonstrates how to monitor keyboard activity and save logs securely. The logs include timestamps and encoded representations of keys pressed. Additionally, it detects when a predefined admin password is entered and logs it separately.

---

## Features

- Logs all key presses with timestamps.
- Encodes data to maintain confidentiality in binary files.
- Detects and logs admin password entries in a separate file.
- Handles special keys (e.g., space, enter, backspace) with readable labels.
- Saves logs in user-friendly, writable directories.

---

## Built With

- Python 3.x
- [keyboard](https://pypi.org/project/keyboard/) - Python library for keyboard input monitoring

---

## Getting Started

### Prerequisites

Ensure Python 3.x is installed on your system. You can download Python [here](https://www.python.org/downloads/).

Install the required Python library:

```bash
pip install keyboard
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/spy-group/keylogger.git
   cd keylogger
   ```

2. Save the script as `keylogger.py`.

3. Ensure you have write permissions for the `Documents` folder, where logs will be stored.

---

## Usage

1. Open a terminal or command prompt.

2. Run the keylogger script:
   ```bash
   python keylogger.py
   ```

3. The program will:
   - Start monitoring key presses.
   - Save general key logs in `Lecture001.bin`.
   - Save admin password events in `Lecture002.bin`.

4. Stop the keylogger by pressing `Ctrl+C`.

---

## How It Works

### Logging Mechanism

1. **Key Presses:**
   - Each key press is captured using the `keyboard` library.
   - Special keys (e.g., `ENTER`, `SPACE`, `BACKSPACE`) are handled with readable labels.

2. **Encoding:**
   - A simple encoding mechanism adds a layer of security.
   - Data is saved as encoded binary in `.bin` files.

3. **Admin Password Detection:**
   - The script detects when a predefined admin password (`adminpassword`) is entered.
   - Logs this event in a separate file, `Lecture002.bin`.

### Log Files

- **`Lecture001.bin`**: Contains all logged key presses.
- **`Lecture002.bin`**: Contains logs specifically for admin password entries.

---

## Disclaimer

This keylogger is intended for **educational purposes only**. Unauthorized use of keylogging software may violate privacy laws and regulations. Always ensure you have proper authorization before using this tool.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## Contact

For questions or support, feel free to reach out:

- GitHub: [spy-group](https://github.com/yourusername)
- Email: spy-group0@proton.me

---
