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

'''
The main point of using Pandas is because in Pandas you get access to a datatype called a dataframe,
which is sort of like a mini spreadsheet with rows and columns

Some benefits of using it are:
    - makes it really easy to import from external sources of data like .csv files, excel, sql databases
    - also makes it easy to export to those sources
    - works well with existing python data types like lists and dictionaries
    - makes it easy to deal with messy data, especially missing values
    - has options for filtering and sorting data

You probably won't see the biggest benefits of this until we start working with databases.
If they don't seem that useful, just be patient.
Today the plan is just to use them with lists and dictionaries before doing stuff with external sources.

'''

import pandas as pd # note, you don't need the "as pd" part, but for whatever reason, that's how most programmers refer to pandas

#list of data
lstNames = ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"]

# store a dataframe by calling the DataFrame constructor and give it a list as an argument.


# try printing out the dataframe
# Every piece of data gets its own row. Rows are numbered 0, 1, 2, etc. That is the row index
# Columns can have titles, but by default it is just 0, 1, 2, etc.



# Another list of data
lstNames2 = [ ["Ballet","Jane"], ["Jazz", "Hadley"], ["Modern", "Lyla"], ["Tap", "London"], ["Tango", "Zoey"], ["Square", "Millie"], ["Hip-Hop", "Beck"]]

# put this new list into a new dataframe




# if you wanted to rename the columns, you can change the .columns attribute of the dataframe
# give it a list of column titles, like "Dancer Type" and "Dancer Name"



# you can also change the row names through the index attribute.
# Not really useful for what we'll do in class, but good to know
# dfDance2.index = ["A", "B", "C", "D", "E", "F", "G"]
