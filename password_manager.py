from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key() + master_pwd.encode()
fer = Fernet(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


def view():  # function to view saved passwords.
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            # splits data into username and password for easier readability.
            print("User: ", user, "|", "Password: ",
                  fer.decrypt(password.encode()).decode())


def add():  # function to add a new password.
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')


while True:
    mode = input(
        "Would you like to add a new password, view exiting ones or quit? (view/add/q): ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
