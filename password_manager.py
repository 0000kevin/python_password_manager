from posixpath import split
import pwd
from cryptography.fernet import Fernet

'''
# using the Fernet import to generate a key to encrypt the passwords with, only need to run once to generate the key.
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        return key

# View username and password - decrypt password using fernet
def view():
    with open("passwords.txt","r") as pwd_file:
        for line in pwd_file.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("Username: ",user,"| Password: ",fer.decrypt(password.encode()).decode())

# Add username and password to file, encrypt and encode password with Fernet
def add():
    name = input("Username: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as pwd_file:
        pwd_file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# being password manager

key = load_key()
fer = Fernet(key)

while True:
    menu = input("Choose an number option from the menu: \n1. Add new password \n2. View existing passwords \n3. Quit \n")
    if menu.isdigit:
        menu = int(menu)
        if menu == 1:
            print("Add new password")
            add()
        elif menu == 2:
            print("View existing passwords")
            view()
        elif menu == 3:
            print("Quitting.")
            break
        else:
            print("Choose a valid option")
            continue
    else:
        print("Choose a number.")
        continue