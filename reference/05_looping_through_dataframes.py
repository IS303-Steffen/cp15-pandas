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

#Calling DataFrame constructor
dfDance = pd.DataFrame(dict_dancers)

print(dfDance)
# Lots of different ways to loop through dataframes.
# Note that if you want to do something like "add 5 to everyone's age"
# loops aren't the fastest way to do things, but it is still good to know

##### COLUMN NAMES:
# if you don't specify anything it gives you the column names
# try printing out all the column names in a loops
for column_name in dfDance:
    print("default is the column name:", column_name)

# GET ROW NAMES OF A SPECIFIC COLUMN
# you can also just loop through a specific column
# try print out all the names of the dancers by looping through the "Dancer" column.
for dancer_name in dfDance["Dancer"]:
    print(dancer_name)

# GET ROW NAMES OF ALL COLUMNS:
# Try combining the above two loops to loop through everything.
for column_name in dfDance:
    print(f"Current column name: {column_name}")

    for row_value in dfDance[column_name]:
        print(f"current row value of {column_name}: {row_value}")


# ITERROWS() TO DIRECTLY GET EACH ROW
# iterrows(): gives you an index and the whole row
# notice how this is different than iter_rows() from openpyxl
# no underscore. This also returns an index.
# try printing out each individual column of each row.
for index, row in dfDance.iterrows():
    print(f"Index: {index}") # this is the index of the row it is on
    print("This is current entire row:")
    print(row)  
    print("this is accessing individual columns in that one row:")
    print(row["Type"], row["Dancer"], row["Age"]) # 

