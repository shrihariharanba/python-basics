# The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:
#
# F = 1.8 * C + 32
#
# Where F is the Fahrenheit temperature and C is the Celsius temperature.
#
# In a .py file, create a variable and assign it an integer representing a celsius temperature that is entered as user input().  input()'s message should prompt the user to enter an integer value.
#
# For this programming challenge, you will then write a function called fahrenheit that takes in an integer representing a Celsius temperature as its argument.  The function will return the Fahrenheit equivalent temperature of that argument to 1 place after the decimal.
#
# At the end of your program, display the Fahrenheit equivalent in a print statement message formatted like so:  "The Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]".
#
# To make sure that the function works, run your program multiple times and call the function on different user entered integer values both negative and positive.
#


celsius = int(input("Please enter an integer value for degrees celsius. "))


def fahrenheit(cel):
    # The second argument of round() is 1 since we only want the Fahrenheit temperature to be displayed with 1 number
    # after the decimal point
    return round((1.8 * cel + 32), 1)


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")
