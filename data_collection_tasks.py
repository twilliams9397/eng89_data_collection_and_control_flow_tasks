# Task 1

name = "name"
name = input("What is your name?  ")
Name = name.capitalize()
print("Welcome to Pycharm, " + Name)

# Task 2

full_name = "full_name"
full_name = input("What is your full name, separated by a space?   ")
first_name = (full_name.split())[0]
First_Name = first_name.capitalize()
surname = (full_name.split())[1]
Surname = surname.capitalize()
print("Welcome to Pycharm, {}".format(First_Name + " " + Surname))