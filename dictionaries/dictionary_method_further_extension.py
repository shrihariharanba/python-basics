# Do all of this in a .py file in Pycharm.
#
# paste these 2 dictionaries into your file
#
# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# use .update() to add the contents of another_one to internet_celebrities.
#
# create a variable and assign it a copy of internet_celebrities.
#
# use the .clear() method to get rid of the contents of internet celebrities.
#
# print internet_celebrities.
#
# print the variable you created in step 3.
#

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)  # 2
gamers = internet_celebrities.copy()  # 3
internet_celebrities.clear()  # 4
print(internet_celebrities)  # 5
print(gamers)  # 6