# This is the code for the data collection and control flow tasks
### Data Collection Tasks
```python
# Task 1

name = "name"
name = input("What is your name?  ")
Name = name.capitalize()
print("Welcome to Pycharm, " + Name + "!")

# Task 2

full_name = "full_name"
full_name = input("What is your full name, separated by a space?   ")
first_name = (full_name.split())[0]
First_Name = first_name.capitalize()
surname = (full_name.split())[1]
Surname = surname.capitalize()
print("Welcome to Pycharm, {} {}!".format(First_Name, Surname))
```
### Control Flow Task
```python
while True:
    rating = str(input("What film rating would you like information for?  "))
    if rating == "universal":
        print("Everyone can watch.")
        rating = str(input("What other film rating would you like information for?  "))
    elif rating == "pg":
        print("General viewing, but some scenes may be unsuitable for young children")
        rating = str(input("What other film rating would you like information for?  "))
    elif rating == "12":
        print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
        rating = str(input("What other film rating would you like information for?  "))
    elif rating == "15":
        print("No one younger than 15 may see a 15 film in a cinema.")
        rating = str(input("What other film rating would you like information for?  "))
    elif rating == "18":
        print("No one younger than 18 may see an 18 film in a cinema.")
        rating = str(input("What other film rating would you like information for?  "))
    else:
        print("We could not give you information for this rating, please try again.")
        rating = str(input("What film rating would you like information for?  "))
    if rating == "exit":
        exit()
```