# This Generator is designed to create an unlimited amount of passwords directly within the terminal
# Author: NameReach

import random
import string

class Colors:
    RED   = "\033[91m"
    YELLOW  = "\033[93m"
    GREEN = "\033[92m"
    CYAN  = "\033[96m"
    BLUE  = "\033[94m"
    BOLD  = "\033[1m"
    RESET = "\033[0m"

def colorize(text, color):
    return f"{color}{text}{Colors.RESET}"

def generate_password(length=16, uppercase=True, numbers=True, special=True):
    characters = string.ascii_lowercase

    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special:
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?"

    password = [random.choice(characters) for _ in range(length)]
    random.shuffle(password)
    return "".join(password)

def check_strength(password):
    score = 0

    if len(password) >= 8:  score += 1
    if len(password) >= 12: score += 1
    if len(password) >= 20: score += 1
    if any(c in string.ascii_uppercase for c in password): score += 1
    if any(c in string.digits for c in password):          score += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password): score += 1

    if score <= 2:
        return "Weak 😬",        Colors.RED,    "██░░░░░░░░"
    elif score <= 4:
        return "Medium 😐",      Colors.YELLOW, "█████░░░░░"
    elif score == 5:
        return "Strong 💪",      Colors.GREEN,  "████████░░"
    else:
        return "Very strong 🔒", Colors.GREEN,  "██████████"
    
def show_result(password):
    label, color, bar = check_strength(password)

    print()
    print(colorize("─" * 50, Colors.BLUE))
    print(colorize("  🔑 Your password:", Colors.BOLD))
    print()
    print(f"  {colorize(password, Colors.CYAN + Colors.BOLD)}")
    print()
    print(colorize(f"  Strength: {bar} {label}", color))
    print(f"  Length:   {len(password)} characters")
    print(colorize("─" * 50, Colors.BLUE))
    print()
    
def run():
    print()
    print(colorize("╔══════════════════════════════════════╗", Colors.BLUE))
    print(colorize("║    🔐  PASSWORD GENERATOR  🔐          ║", Colors.BLUE + Colors.BOLD))
    print(colorize("╚══════════════════════════════════════╝", Colors.BLUE))
    print()

    try:
        entry = input(colorize("  Password length (default: 16): ", Colors.YELLOW)).strip()
        length = int(entry) if entry else 16
        length = max(4, min(length, 128))
    except ValueError:
        length = 16

    def yes_no(question, default=True):
        hint = "[Y/n]" if default else "[y/N]"
        answer = input(colorize(f"  {question} {hint}: ", Colors.YELLOW)).strip().lower()
        return default if answer == "" else answer in ("y", "yes")

    uppercase = yes_no("Include uppercase letters (A-Z)?")
    numbers   = yes_no("Include numbers (0-9)?")
    special   = yes_no("Include special characters (!@#...)?")

    try:
        entry = input(colorize("  How many passwords? (default: 1): ", Colors.YELLOW)).strip()
        amount = int(entry) if entry else 1
        amount = max(1, min(amount, 20))
    except ValueError:
        amount = 1

    print()
    for i in range(amount):
        if amount > 1:
            print(colorize(f"  Password {i + 1}/{amount}:", Colors.BOLD))
        password = generate_password(length, uppercase, numbers, special)
        show_result(password)

    again = input(colorize("  Generate new passwords? [y/N]: ", Colors.YELLOW)).strip().lower()
    if again in ("y", "yes"):
        run()
    else:
        print(colorize("\n  Goodbye! Stay safe! 👋\n", Colors.GREEN))
        
if __name__ == "__main__":
    run()