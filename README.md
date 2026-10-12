🔐 Caesar Cipher Tool

"Encrypt. Decrypt. Analyze. Learn."

A Python-based cryptography learning tool featuring Caesar cipher encryption, decryption, and brute-force analysis — wrapped in an interactive terminal interface.

Built as part of my journey into Python development and cybersecurity fundamentals.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Cryptography-Classical%20Cipher-0A66C2?style=for-the-badge" alt="Classical Cryptography">
  <img src="https://img.shields.io/badge/Tests-10%20Cases-2E8B57?style=for-the-badge" alt="10 Unit Tests">
  <img src="https://img.shields.io/badge/Status-Learning%20Project-708090?style=for-the-badge" alt="Learning Project">
</p>---

⚡ Overview

The Caesar Cipher Tool demonstrates how classical substitution ciphers work through a simple, interactive Python application.

Shift letters, reverse encrypted messages, or explore every possible shift with the built-in brute-force feature.

«Project goal: Learn cryptography fundamentals, Python programming, input validation, and automated testing through hands-on development.»

✨ Features

Feature| Description
🔒 Encryption| Convert readable text into shifted ciphertext
🔓 Decryption| Reverse a Caesar cipher shift
💥 Brute-force analysis| Display all 26 possible shifts
🔠 Case preservation| Keep uppercase and lowercase letters intact
🔄 Flexible shifts| Support negative and large shift values
🎨 Terminal interface| Interactive menu with colored status messages
🛡️ Input validation| Handle invalid shift values and menu choices
🧪 Automated testing| Test cipher behavior using Python "unittest"

🖥️ Demo

01 — Main Interface(ENCRYPTION & DECRYPTION)

![Caesar Cipher Tool Main Interface]
(caesar_cipher_tool_demo.png)

The interactive terminal interface and available operations.

02 — BRUTE FORCE SHIFTS

![Caesar Cipher Brute-Force All Shifts]
(caesar_cipher_demo.png)

Example cipher operations performed in the terminal.

🔍 Example

Original message : HELLO WORLD
Shift value      : 3
Encrypted result : KHOOR ZRUOG

Decrypting "KHOOR ZRUOG" with the same shift restores "HELLO WORLD".

⚙️ How It Works

The Caesar cipher shifts each alphabetic character by a specified number of positions.

The transformation uses modular arithmetic to wrap around the alphabet:

[
E(x) = (x + k) \bmod 26
]

Where:

- "x" is the letter's alphabet position.
- "k" is the shift value.
- "E(x)" is the encrypted position.

For decryption, the shift is reversed.

🚀 Getting Started

Requirements

- Python 3
- Git
- No external Python packages required

1. Clone the repository

git clone https://github.com/HARSHA-TKD/caesar-cipher-tool.git
cd caesar-cipher-tool

2. Run the application

python caesar_cipher.py

3. Choose an operation

[1] Encrypt a message
[2] Decrypt a message
[3] Brute-force all shifts
[4] About this tool
[5] Exit

Follow the terminal prompts to perform the desired operation.

🧪 Automated Testing

The project includes unit tests written with Python's built-in "unittest" framework.

Run the tests with:

python -m unittest -v test_caesar_cipher

The test suite covers:

- Encryption and decryption
- Uppercase, lowercase, and mixed-case text
- Spaces and punctuation
- Alphabet wraparound
- Negative and large shift values
- Empty messages
- Full alphabet rotations

📁 Project Structure

caesar-cipher-tool/
├── caesar_cipher.py
├── test_caesar_cipher.py
├── README.md
└── screenshots/
    ├── main-menu.png
    └── cipher-demo.png

🧠 What I Learned

- Python functions, loops, and conditional logic
- String processing and character conversion
- Modular arithmetic
- Input validation and exception handling
- Writing automated unit tests
- Using Git and GitHub for version control
- Understanding the limitations of classical ciphers

⚠️ Security Disclaimer

The Caesar cipher is an educational cryptographic technique, not a secure encryption method. Its small key space makes it easy to break.

Do not use this tool to protect real passwords, credentials, personal information, or confidential messages.

🛣️ Future Improvements

- [ ] Add a more structured command-line interface
- [ ] Add additional automated edge-case tests
- [ ] Allow users to save results to a text file
- [ ] Add an option to copy results easily
- [ ] Explore modern cryptography concepts using appropriate libraries

👨‍💻 Author

Harsha Vardhan V G

GitHub: "@HARSHA-TKD" (https://github.com/HARSHA-TKD)

---

<p align="center">
  <b>Built with Python • Created for learning • Inspired by cybersecurity</b>
</p>
