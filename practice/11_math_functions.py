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

dfImportedFile = pd.read_excel('dummy_data.xlsx')
print(dfImportedFile)
# you can also do math functions on columns by accessing a column in a dataframe and doing a function like .sum(), .count() or .median()

# find the median hours slept of the filtered data:



# group by
#dfPostgres2.groupby("column_to_group_on")["column_to_a_calculation_on"].sum()



# group by
# once again, similar things you can do in pandas or in SQL with postgres:
# in pandas:    (or some other calculation, doesn't have to be sum)

# let's find group by gender, and find the average (mean) hours slept between males and females. Let's use the 
# original data we got from postgres before we filtered it.
# store the results in a dataframe called dfGroupedData