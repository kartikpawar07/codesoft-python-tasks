import random
import string

def generate_password(length):
    if length < 4:
        print("Password should be at least 4 characters long.")
        return ""

    # Combine letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)

        if password:
            print("\nGenerated Password: ", password)
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Run the generator
main()
