# Do all of this in a .py file in Pycharm
#
# Create a function called name_printer which takes 1 parameter and prints it
#
# Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.
#
# Call name_printer() with the variable "name" as its argument.

def name_printer(user_name):
    print(user_name)


name = input("Please enter your name.")
name_printer(name)