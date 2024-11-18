# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

import pandas as pd

dict_dancers =  {   "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
                "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
                "Age" : [18, 23, 19, 20, 21, 22, 21]
            }

# given the above dictionary, make a dataframe,
# loop through it, and add 3 to the age of every dancer who's first name starts with "L". 
# You might have to refer back to your original dataframe when you add 3 to the age,
# depending on how you write it.

# Reminder Hint:
example_string = "strings are like lists of characters"
print(example_string[0])


df_dancers = pd.DataFrame(dict_dancers)
print(df_dancers)

# using iterrows()
for index, row in df_dancers.iterrows():
    if row["Dancer"][0] == "L":
        df_dancers.iloc[index, 2] += 3
print(df_dancers)

# # not using iterrows()
for index, row in enumerate(df_dancers["Dancer"]):
    if row[0] == "L":
        df_dancers.loc[index, "Age"] += 3

print(df_dancers)

# alternate without doing a loop
df_dancers.loc[df_dancers["Dancer"].str[0] == "L", "Age"] += 3
