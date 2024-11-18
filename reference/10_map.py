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

# read the excel file into a pandas dataframe with pd.read_excel
dfImportedFile = pd.read_excel('dummy_data.xlsx')
print(dfImportedFile)

# changing an entire column's data:
# let's change everyone's age to 99
dfImportedFile["age"] = 99
print(dfImportedFile)

# let's change everyone's age_repeated to be their hours_slept:
dfImportedFile["age"] = dfImportedFile["hours_slept"]
print(dfImportedFile)

# one cool way to update column values is using .map
# .map and .apply are really cool functions that can change any data using custom functions and specifications
# we don't have time to dive into it, but I do want to show you using .map with a dictionary

# Let's say you want to change gender to show M or F instead of Male or Female
# a dictionary is a great way to do that:
genderDictionary = {"Male" : "M", "Female" : "F"}

# remember how dictionaries work, if you give it a matching key, it gives you the value:
valueFromDictionary = genderDictionary["Male"]
print(f"Dictionary value: {valueFromDictionary}")

# you can use a dictionary across a whole column using .map(dExampleDictionary)
# change the gender column so that it only shows "M" and "F"
dfImportedFile["gender"] = dfImportedFile["gender"].map(genderDictionary)
print(dfImportedFile)
