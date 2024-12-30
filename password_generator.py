import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else""
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""

    # Combine pools based on user input
    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        return "Error: No character set selected. Please choose at least one option."

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
        print("Welcome to the Password Generator!")

        # Take user inputs for password requriments
        while True:
            try:
                length = int(input("Enter the desired password length (minimum 4): "))
                if length < 4:
                    print("Password length should be at least 4.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")


        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        # Generate the password
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print("\n Your generated password is:", password)

if __name__ == "__main__":
        main()

