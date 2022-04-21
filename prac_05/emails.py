email_collection = {}
email = input("Email: ")
while email != "":
    part_1 = email.split('@')
    part_2 = part_1[0].split('.')
    name = part_2[0].title()
    identification = input("Is your name {} Ward? (Y/n) ".format(name)).title()
    if identification != "Y" and identification != "":
        name = input("Name: ").title()
    email_collection[name] = email
    email = input("Email: ")
print()
for key, value in email_collection.items():
    print("{} ({})".format(key, value))
