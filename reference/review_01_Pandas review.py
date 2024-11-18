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

# must import pandas (need to install it first)
import pandas as pd

# importing a .csv. using read_csv. See the file "csv fixes.py if you're having trouble"
dfDancers = pd.read_csv('dancers.csv')

# access specific columns
print(dfDancers["Dance"])

# access multiple columns
print(dfDancers[["Name", "Age"]])

# access specific rows, with iloc (you know the specific row)
print(dfDancers.iloc[5])  # Prints row 6 (Python is zero-indexed)

# access specific rows, with loc (you know the specific label index)
print(dfDancers.loc[5])  # Prints row with index label 5 (same as above if default indexing is used)

# access specific rows, with loc (you don't know the row). Let's find rows where the age is 25
print(dfDancers.loc[dfDancers['Age'] == 21])


# access specific cell with iloc (you know the specific row and column)
print(dfDancers.iloc[5, 1])  # Prints the value of the fourth column in row 6

# access specific cell, with loc (you know the specific row's label and column's label)
print(dfDancers.loc[5, 'Age'])  # Prints the 'Age' of the dancer at index label 5

# access specific cell, with loc (you don't know the row but know the condition)
# Assuming you want to get the 'Name' of dancers who are 25 years old
print(dfDancers.loc[dfDancers['Age'] == 25, 'Name'])

# filter using query
# For example, to get dancers with an age greater than 20.
filtered_dancers = dfDancers.query('Age > 20')
print(filtered_dancers)

# sort using sort_values
# For instance, to sort by age
sorted_dancers = dfDancers.sort_values(by='Age', ascending=True)
print(sorted_dancers)