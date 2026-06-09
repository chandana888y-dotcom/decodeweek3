import random
import string

def generate_password(length):
    # Characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure password contains at least:
    # 1 uppercase, 1 lowercase, 1 digit, 1 special character
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill remaining length
    password += random.choices(characters, k=length - 4)

    # Shuffle password characters
    random.shuffle(password)

    return ''.join(password)

def main():
    print("=" * 40)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Password length must be at least 4.")
            return

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()