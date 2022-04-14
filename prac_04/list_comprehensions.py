# 3.List comprehensions
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

# one more example, using filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# in lowercase format
lower_list = []
for lowercase in full_names:
    name_lowercase = lowercase.lower()
    lower_list.append(name_lowercase)
print(lower_list)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# from the above list of strings
number_list = []
for num in almost_numbers:
    number = int(num)
    number_list.append(number)
print(number_list)



# greater than 9 from the numbers (not strings) you just created
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
num_list = []
for number in almost_numbers:
    number = int(number)
    if number > 9:
        num_list.append(number)
    else:
        pass
print(num_list)
