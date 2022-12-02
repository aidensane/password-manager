pwd = input("What is the master password? ")

while True:
    mode = input(
        "Would you like to add a new password, view exiting ones or quit? (view/add/q): ")
    if mode == "q":
        break

    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue
