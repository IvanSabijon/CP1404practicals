email_to_name = {}


def main():
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation != "y" and confirmation != "":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    name = email.split("@")[0]
    name = name.split(".")
    name = " ".join(name).title()
    return name


main()
