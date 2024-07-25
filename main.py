"""
COP3502C Lab 9 Software Engineering
Lance Daley

Understand purpose and usefulness of version control.
"""

def encode(password):
    new_password = ""
    for char in password:
        new_password += str((int(char) + 3) % 10)
    return new_password

def decode(password):
    # coding for Jason
    pass

def display_menu():
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def main():
    while True:
        display_menu()
        selection = int(input("Please enter an option: "))
        if selection == 1:
            password = input("Please enter the password to encode: ")
            new_password = encode(password)
            print("Your password has been encoded and stored!")
        elif selection == 2:
            print("placeholder for Jason")
            # coding for Jason
        elif selection == 3:
            break
        else:
            print("Please enter a valid option")


if __name__ == '__main__':
    main()

