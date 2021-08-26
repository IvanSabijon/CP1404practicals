"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    list_of_subject_data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        list_of_subject_data.append(parts)
    input_file.close()
    return list_of_subject_data


def display_subject_details(data):
    for element in data:
        print(f"{element[0]} is taught by {element[1]:12} and has {element[2]:3} students")


main()
