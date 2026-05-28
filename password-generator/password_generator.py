import random
import string
import os


class PasswordGenerator:

    # Generate password with default length = 10
    def generate_password(self, length=10):

        # all possible characters
        characters = (
                string.ascii_letters +  # a-z A-Z
                string.digits +  # 0-9
                string.punctuation  # special symbols
        )

        # generate random password
        password = ''.join(random.choice(characters) for _ in range(length))

        return password

    # Save data to file
    def save_password(self, website, username, password):
        file_path = os.path.join(os.path.dirname(__file__), "..", "passwords.txt")

        with open(file_path, "a") as file:
            file.write(f"Website : {website}\n")
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")
            file.write("-" * 30 + "\n")


# Run program
if __name__ == "__main__":

    pg = PasswordGenerator()

    print("Password Generator and Save")

    # Take user input
    website = input("Enter website name: ")
    username = input("Enter username/email: ")

    # Generate password (default length = 10)
    password = pg.generate_password()

    print("\nGenerated Password:", password)

    # Save to file
    pg.save_password(website, username, password)

    print("Password saved successfully!")