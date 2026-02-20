import random

class PasswordGenerator:
    def create_password(self, length):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#"
        password = ""
        
        for _ in range(length):
            password += random.choice(chars)
        
        return password


# Main program
length = int(input("Enter password length: "))

pg = PasswordGenerator()
print("Your Password:", pg.create_password(length))