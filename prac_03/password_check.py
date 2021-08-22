MINIMUM_SET = 10


def main():
    password = get_password()
    print_password(password)


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_SET:
        print("Invalid password")
        password = input("Password: ")
    return password


def print_password(password):
    print("*" * len(password))


main()
