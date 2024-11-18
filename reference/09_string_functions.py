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

import pandas as pd # pandas gets you dataframes


# read the excel file into a pandas dataframe with pd.read_excel
dfImportedFile = pd.read_excel('dummy_data.xlsx')
print(dfImportedFile)

# you can access string functions and apply them to entire columns using .str
# try applying .upper() to all the last names in the dummy data set.

dfImportedFile["last_name"] = dfImportedFile["last_name"].str.upper()

print()
print(dfImportedFile)


# remember .split() from your first project?
# pandas has its own version of split that works on columns.
# after accessing a column, add .str.split("character to split by", expand = True)
# expand makes it so it separates out what you split into separate columns in a new dataframe

# split the gender column by the letter "a", store it in a new dataframe, and print that dataframe out
dfSeparatedNames = dfImportedFile["gender"].str.split("a", expand = True)
print(dfSeparatedNames)



