from guitar import Guitar


def main():
    guitar_list = []
    print("My guitars!")
    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitar_name = input("Name: ")
    while guitar_name != "" and guitar_name != " ":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar_checkin = Guitar(guitar_name, guitar_year, guitar_cost)
        print("{} ({}) : ${} added."
              .format(guitar_checkin.name, guitar_checkin.year, guitar_checkin.cost))
        guitar_list.append(guitar_checkin)
        guitar_name = input("Name: ")
    print()
    print("... snip ...")
    print()
    print("These are my guitars:")
    if guitar_list:
        for i, guitar in enumerate(guitar_list, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
