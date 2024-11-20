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

# =================
# LIST TO DATAFRAME
# =================

'''
OVERVIEW
--------
These are a few examples of putting lists into a DataFrame. I don't cover it
in class since using dictionaries is easier since that more elegantly handles
column lables. You'll have to manually add column labels afterwards if you use
lists.
'''

import pandas as pd 

# list of dances
dances_list = ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"]

# 1. CREATE A DATAFRAME FROM A LIST
# Use the list provided above to make a DataFrame. Print it out afterwards.
df_dances = pd.DataFrame(dances_list)
print(df_dances, '\n')


# Another list of data
names_dances_list = [
    ["Ballet","Jane"],
    ["Jazz", "Hadley"],
    ["Modern", "Lyla"],
    ["Tap", "London"],
    ["Tango", "Zoey"],
    ["Square", "Millie"],
    ["Hip-Hop", "Beck"]
]

# 2. CREATE A DATAFRAME FROM A LIST
# Create another DataFrame and print it out using the above list.
df_dances_2 = pd.DataFrame(names_dances_list)
print(df_dances_2, "\n")

# 3. RENAME THE COLUMNS
# if you wanted to rename the columns, you can change the .columns attribute of
# the dataframe give it a list of column titles, like "Dancer Type"
# and "Dancer Name"
column_labels = ["Dance Type", "Dancer Name"]
df_dances_2.columns = column_labels
print(df_dances_2, "\n")

