import random
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    print_quick_picks(number_of_quick_picks)


def print_quick_picks(number_of_quick_picks):
    for i in range(number_of_quick_picks):
        quick_picks = []
        for number in range(6):
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if random_number in quick_picks:
                random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_picks.append(random_number)
        quick_picks.sort()
        for number in quick_picks:
            print(f"{number:2}", end=" ")
        print()


main()
