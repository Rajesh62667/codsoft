import random
import string

def generate_password(length):
    """Generate a random password containing letters, digits, and punctuation."""
    if length < 4:
        return "Password length should be at least 4 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter your desired password length: "))
            if length < 4:
                print("Password length must be at least 4. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        password = generate_password(length)
        print("\nGenerated Password:", password)

        again = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting the Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
