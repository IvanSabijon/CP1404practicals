MINIMUM_SET = 10
password = input("Password: ")
while len(password) < MINIMUM_SET:
    print("Invalid password")
    password = input("Password: ")
print("*" * len(password))
