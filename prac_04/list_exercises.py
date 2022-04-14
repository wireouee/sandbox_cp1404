# 1.Basic list operations
num_list = []
for ques in range(5):
    num = int(input("Number: "))
    num_list.append(num)
print("The first number is {}".format(num_list[0]))
print("The last number is {}".format(num_list[-1]))
print("The smallest number is {}".format(min(num_list)))
print("The largest number is {}".format(max(num_list)))
print("The average of the numbers is {}".format(sum(num_list)/5))

# 2.Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

