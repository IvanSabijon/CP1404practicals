from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 15000)

print("{} get_age() - Expected 99. Got {}".format(guitar.name, guitar.get_age()))
print("{} get_age() - Expected 8. Got {}".format(another_guitar.name, another_guitar.get_age()))
print("{} is_vintage() - Expected True. Got {}".format(guitar.name, guitar.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))
