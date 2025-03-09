import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user-selected criteria."""
    character_set = ""
    if use_letters:
        character_set += string.ascii_letters  # Uppercase and lowercase letters
    if use_numbers:
        character_set += string.digits         # Numbers 0-9
    if use_symbols:
        character_set += string.punctuation      # Symbols (e.g., !, @, #, etc.)

    if not character_set:
        print("Error: You must choose at least one type of character.")
        return None

    # Generate a random password of the specified length
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the length.")
        return

    # Get user preferences for character types
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
