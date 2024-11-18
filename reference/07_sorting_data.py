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

import numpy as np
import pandas as pd
            
dict_dancers =  {   "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
                "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
                "Age" : [18, 23, 19, 20, 21, 22, 21]
            }

#Calling DataFrame constructor
dfDance = pd.DataFrame(dict_dancers)
print(dfDance)

# to sort, you can use .sort_values on any dataframe.
# try printing out the result of sorting on "Age"
print()
print(dfDance.sort_values("Age"))
print()
print(dfDance)

##########
# inplace
###########
# You can also add inplace = True. This will alter the order of the original dataframe
# try sorting by age without printing it out,
# and then in the line after print out the original dataframe

#########
# descending order 
#########
# if you want it sorted by descending, just set ascending = False
# try sorting by age descending in place, then print out the result
dfDance.sort_values("Age", ascending=False, inplace=True)

print("\n", dfDance)

##########
# sorting by multiple columns
##########
# if you provide a list of columns (e.g. in square brackes) as the first argument, you can sort by
# multiple columns
# try sorting by Age, and then Dancer.
# bonus: alter it to make it so that it is sorting by age in ascending order, and then by Dancer in Descending order
dfDance.sort_values(["Age", "Dancer"], ascending = [True, False], inplace=True)
print("\n",dfDance)