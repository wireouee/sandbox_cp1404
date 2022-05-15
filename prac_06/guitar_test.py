from guitar import Guitar


def main():
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2013)

    print("{} get_age() - Expected {}. Got {}"
          .format(guitar_1.name, guitar_1.get_age(), guitar_1.get_age()))
    print("{} get_age() - Expected {}. Got {}"
          .format(guitar_2.name, guitar_2.get_age(), guitar_2.get_age()))
    print("{} is_vintage() - Expected {}. Got {}"
          .format(guitar_1.name, guitar_1.is_vintage(), guitar_1.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}"
          .format(guitar_2.name, guitar_2.is_vintage(), guitar_2.is_vintage()))


main()