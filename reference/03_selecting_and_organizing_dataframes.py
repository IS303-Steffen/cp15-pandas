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

#list of data
dictionary_dancers =  {   "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
                "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
                "Age" : [18, 23, 19, 20, 21, 22, 21]
            }

# Make a dataframe and print it out.
dfDance = pd.DataFrame(dictionary_dancers)

print(dfDance, "\n")

# you can access a specific column by giving its name in square brackets.
# Try printing out just the "Dancer" column
print(dfDance["Dancer"])

# you can access multiple columns by giving a list inside the square brackets
# note, that means two square brackets on each side
# try printing out "Dancer" and "Age"
print(dfDance[["Dancer", "Age"]], "\n")

###################
# .iloc (uses row and column index)
# 0 based indexing
# df.iloc[row_index] to get whole row
# df.loc[row_index, column_index] to get individual cell
#############

# try printing out the 3rd row using iloc
print(dfDance.iloc[2], "\n")

# try printing out the 3rd row, 3rd column using iloc
print(dfDance.iloc[2, 2], "\n")

# you can access the last element by using -1, second to last using -2, etc.
# try printing everything from the last row of the dataframe:
print(dfDance.iloc[-1], "\n")

# Try to change the age of the 3rd row, 3rd column to 30
dfDance.iloc[2,2] = 30

print(dfDance, "\n")

##########
# you can access multiple rows or columns using a colon : to specify a starting a stopping index
# it will grab everything at the starting, but stop before the stopping index:

# try to grab the first 3 rows, and the 2nd to 3rd columns:
print()
print(dfDance.iloc[[3, 6], 0:3])


###################
# .loc (uses row and column labels)
# note this is confusing, because by default, the row label and row index is the same.
# BUT, if you get a specific cell, then use the column lable, not the column index.
# df.loc[row_label, column_label]
#############

#try to get the 3rd row with .loc
print(dfDance.loc[2], "\n")

# try to get the age of the person in the 3rd row with .loc
print(dfDance.loc[2, "Age"], "\n")

# Note: you can also use .at for the same thing. It is faster but can only access single cells
# It is a little more computationally efficient, so if you are only accessing individual cells, feel free to use
# .at ,but .loc will work too
print(dfDance.at[2, "Age"])


# you can access multiple rows or columns using a colon : to specify a starting row/column, and then an ending
# row/column. But notice that it is inclusive, and grabs the start and stopping index.

# try to grab the first 3 rows, and the 2nd to 3rd columns:
# try specifying the 1st to 3rd columns too just for fun. It grabs everything in between.
print()
print(dfDance.loc[0:2, "Dancer":"Age"])


#############
# loc has this big advantage over iloc:
# you can use "boolean indexing" to find rows that match a logical condition
# df.loc[df['column'] > 19], etc.
#############

# Let's find rows where the age is 21
print()
print(dfDance.loc[dfDance['Age'] == 21])

# find just the names of dancers that have an age of 21
print()
print(dfDance.loc[dfDance['Age'] == 21, "Dancer"])


####
# Multiple conditions!!
###
# Note that in the file called "filtering_data" we'll go over a slightly easier way to do this,
# but that way has some limitations.

'''
To add multiple logical conditions, you need to:
    1. put each condition in parentheses
    2. Use panda's version of operators:
        - and: &
        - or: |
        - not: ~

    e.g. df.loc[(df["Column"] == "X") & (df["Column2"] < 10)]
'''
# try to find the rows where the age is over 22, or the type of dance is Tango
print()
print(dfDance.loc[(dfDance["Age"] > 22) | (dfDance["Type"] == "Tango")])

# do the same thing, but only show the Dancer name
print()
print(dfDance.loc[(dfDance["Age"] > 22) | (dfDance["Type"] == "Tango"), "Dancer"])

########
# Updating entire columns
########

# try to add 10 years to everyone's age:
dfDance["Age"] += 10
print(dfDance, "\n")

# try to subtrack 7 years to only those over 30
dfDance.loc[dfDance["Age"] > 30 , "Age"] -= 7
print(dfDance, "\n")

'''
Note that what you can do here is one of the main advantages
of using pandas over other data types / importing Excel files
with openpyxl. You can make changes to entire columns / subsections
without looping over things. It is very computationally efficient.
Plus, it is fewer lines of code.
'''

#######
# Getting just the values of a dataframe
########

# if you just want the data in a format to directly use (like strings)
# you can use .values. It returns everything in a list, with each row after that in a list.
print(dfDance.values)