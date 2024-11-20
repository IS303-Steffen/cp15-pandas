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

# ==========================
# LOOPING THROUGH DATAFRAMES
# ==========================

'''
OVERVIEW
--------
You can loop through columns and rows of a DataFrame. If you are looping so
that you can update a value in the DataFrame, I'd recommend just seeing if you
can use .iloc or .loc to update a value since that is more computationally 
efficient.
'''

import pandas as pd

dancers_dict = {
    "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
    "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
    "Age" : [18, 23, 19, 20, 21, 22, 21]
}

df_dancers = pd.DataFrame(dancers_dict)
print(df_dancers, "\n")

# 1. LOOP THROUGH COLUMN NAMES
# If you don't specify anything it gives you the column names.
# Try printing out all the column names in a loop.
for column_name in df_dancers:
    print("default is the column name:", column_name)

# 2. GET ROW VALUES OF A SPECIFIC COLUMN
# You can also just loop through a specific column. Try printing out all the
# names of the dancers by looping through the "Dancer" column.
for dancer_name in df_dancers["Dancer"]:
    print(dancer_name)

# 3. GET ROW VALUES OF ALL COLUMNS
# Try combining the above two loops to loop through everything.
for column_name in df_dancers:
    print(f"Current column name: {column_name}")
    for row_value in df_dancers[column_name]:
        print(f"current row value of {column_name}: {row_value}")

# 4. USE .iterrows() TO DIRECTLY GET EACH ROW
# iterrows(): gives you an index and the whole row. Notice how it doesn't have
# an "_" like .iter_rows() from openpyxl.
# try printing out each individual column of each row.

for index, row in df_dancers.iterrows():
    print(f"Index: {index}") # this is the index of the row it is on
    print("This is current entire row:")
    print(row)  
    print("this is accessing individual columns in that one row:")
    print(row["Type"], row["Dancer"], row["Age"]) # 

