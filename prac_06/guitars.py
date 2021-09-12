from prac_06.guitar import Guitar


def main():
    """Guitar program."""
    guitars = []
    number = 0

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) : ${:.2f} added.".format(name, year, cost))
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for guitar in guitars:
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {number + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
