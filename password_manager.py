

master_pwd = input("What is the master password? ")


def view():  # function to view saved passwords.
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            # splits data into username and password for easier readability.
            print("User: ", user, "|", "Password: ", password)


def add():  # function to add a new password.
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + '\n')


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
