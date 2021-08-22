# 1.
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read()
print(f"Your name is {name}")

# 3.
in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

# 4.
result = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    result += int(line)
in_file.close()
print(result)
