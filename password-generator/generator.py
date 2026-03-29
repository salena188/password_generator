# class PasswordGenerator:
#     def generate(self):
#         print(" Password generated successfully")
#
#
# # ⭐ This makes the file runnable
# if __name__ == "__main__":
#     my_generator = PasswordGenerator()
#     my_generator.generate()
import random
import string
import os


class PasswordGenerator:

    def generate_password(self, length=12):
        characters = (
            string.ascii_letters +   # a-z A-Z
            string.digits +          # 0-9
            string.punctuation       # symbols
        )

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def save_password(self, website, username, password):
        # Save file in project root
        file_path = os.path.join(os.path.dirname(__file__), "..", "passwords.txt")

        with open(file_path, "a") as f:
            f.write(f"Website : {website}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Password: {password}\n")
            f.write("-" * 30 + "\n")

        print(" Password saved successfully!")


# MAIN PROGRAM (runs when file executed directly)
if __name__ == "__main__":

    pg = PasswordGenerator()

    print(" Password Generator & Saver")

    website = input("Enter website name: ")
    username = input("Enter username/email: ")

    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        length = 12

    password = pg.generate_password(length)

    print(f"\nGenerated Password: {password}")

    pg.save_password(website, username, password)
