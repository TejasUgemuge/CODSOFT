import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a random password with the specified length and complexity."""
    
    # Base character set
    characters = string.ascii_lowercase
    
    # Add other character sets based on user preferences
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Get user input for password length
    length = int(input("Enter the desired length of the password: "))
    
    # Get user preferences for complexity
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"Generated password: {password}")

if __name__ == '__main__':
    main()
