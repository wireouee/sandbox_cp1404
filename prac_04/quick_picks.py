import random
ticket_number = int(input("How many Quick Picks: "))
for line in range(ticket_number):
    num_list = []
    for row in range(6):
        number = random.randint(1, 45)
        num_list.append(number)
    num_list.sort()
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(*num_list))