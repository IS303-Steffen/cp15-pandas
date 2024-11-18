import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ======
# PANDAS
# ======

'''
OVERVIEW
--------
The main point of using Pandas is because in Pandas you get access to a
datatype (class) called a dataframe,
which is sort of like a mini spreadsheet with rows and columns

Some benefits of using it are:
    - makes it really easy to import from external sources of data like .csv
      files, excel, sql databases
    - also makes it easy to export to those sources
    - works well with existing python data types like lists and dictionaries
    - makes it easy to deal with messy data, especially missing values
    - has options for filtering and sorting data

You probably won't see the biggest benefits of this until we start working with
databases.

If they don't seem that useful, just be patient.
At first, the plan is just to use them with lists and dictionaries before doing
stuff with external sources.
'''

import pandas as pd
    
# dictionary with two lists
lstNames =  {"Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
             "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"]}

# create a dataframe using the dictionary, then print it out. Notice the column names!
dfDance = pd.DataFrame(lstNames)

print(dfDance)

'''
To remember:
    - The lists in the dictionary have to have the same number of values (like Type can't have 10 types, and then Dancer only has 8 dancers)
    - Easiest way to get around this for now is to just insert blank strings or None for empty values.
'''