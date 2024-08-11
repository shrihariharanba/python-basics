# In a .py file, write a program which calculates the number of characters in a string.
#
# The string should be entered using input() and assigned to a variable.
#
# Use print() twice at the end of your program.  The first print() will print the string that the user entered and the second print() will display the number of characters in the string.  For example, if the user entered the string "hello world", the number of characters would be 11.

user_str = input("Please enter a string.")

count = 0  # This variable will be used to hold the number of characters in the string.
# This for loop adds 1 to count for each character in user_str.
for char in user_str:
    count += 1

print(user_str)
print(count)
