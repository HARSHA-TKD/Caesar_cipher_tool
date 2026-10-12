# ==========================================
#        CAESAR CIPHER TOOL v2.0
#        Python Cryptography Project
# ==========================================

import os


# Terminal colors
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
SILVER = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    print(CYAN + BOLD + r"""
   ____  __    ____  ____  ___  ____ 
  / ___)(  )  (  _ \( ___)/ __)( ___)
  \___ \ )(__  )   / )__) \__ \ )__) 
  (____/(____)(_)\_)(____)(___/(____)

       C A E S A R   C I P H E R
             TOOL v2.0
""" + RESET)
    print(SILVER + "       Encrypt | Decrypt | Brute Force" + RESET)
    print(BLUE + "========================================" + RESET)


def caesar_cipher(message, shift):
    result = ""

    # Normalize large and negative shifts
    shift = shift % 26

    for char in message:

        # Handle uppercase letters
        if "A" <= char <= "Z":
            new_position = (ord(char) - ord("A") + shift) % 26
            result += chr(new_position + ord("A"))

        # Handle lowercase letters
        elif "a" <= char <= "z":
            new_position = (ord(char) - ord("a") + shift) % 26
            result += chr(new_position + ord("a"))

        # Keep everything else unchanged
        else:
            result += char

    return result


def get_shift():
    while True:
        try:
            return int(input(CYAN + "\nEnter shift value: " + RESET))
        except ValueError:
            print(RED + "Invalid input! Enter a whole number." + RESET)


def encrypt_message():
    message = input("\nEnter your message: ")
    shift = get_shift()

    result = caesar_cipher(message, shift)

    print(GREEN + "\n[+] ENCRYPTION COMPLETE" + RESET)
    print(SILVER + "Encrypted message: " + RESET + BOLD + result + RESET)


def decrypt_message():
    message = input("\nEnter encrypted message: ")
    shift = get_shift()

    result = caesar_cipher(message, -shift)

    print(GREEN + "\n[+] DECRYPTION COMPLETE" + RESET)
    print(SILVER + "Decrypted message: " + RESET + BOLD + result + RESET)


def brute_force():
    message = input("\nEnter encrypted message: ")

    print(CYAN + "\nTrying every possible shift...\n" + RESET)

    for shift in range(26):
        result = caesar_cipher(message, -shift)
        print(f"Shift {shift:02}: {result}")

    print(GREEN + "\n[+] All 26 possibilities displayed." + RESET)


def show_about():
    print(CYAN + BOLD + "\nABOUT THIS PROJECT" + RESET)
    print("Tool       : Caesar Cipher Tool v2.0")
    print("Language   : Python")
    print("Technique  : Alphabet substitution")
    print("Features   : Encrypt, decrypt, brute force")
    print("\nNote: Caesar cipher is not secure for real secrets.")


def main():
    while True:
        clear_screen()
        show_banner()

        print("\n" + BOLD + "MAIN MENU" + RESET)
        print(CYAN + "[1]" + RESET + " Encrypt a message")
        print(CYAN + "[2]" + RESET + " Decrypt a message")
        print(CYAN + "[3]" + RESET + " Brute-force all shifts")
        print(CYAN + "[4]" + RESET + " About this tool")
        print(CYAN + "[5]" + RESET + " Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            encrypt_message()
        elif choice == "2":
            decrypt_message()
        elif choice == "3":
            brute_force()
        elif choice == "4":
            show_about()
        elif choice == "5":
            print(GREEN + "\nThanks for using Caesar Cipher Tool!" + RESET)
            print(SILVER + "Stay curious. Keep learning. Stay ethical." + RESET)
            break
        else:
            print(RED + "\nInvalid choice! Select an option from 1 to 5." + RESET)

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nExiting Caesar Cipher Tool. Goodbye!")