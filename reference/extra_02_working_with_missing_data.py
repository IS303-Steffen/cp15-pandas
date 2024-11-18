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
    
#list of data
lstNames =  {   "Type" : [ np.nan, "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
                "Dancer" : ["Jane", np.nan, "Lyla", "London", "Zoey", "Millie", "Beck"],
                "Age" : [18, 23, 19, "A", 21, 22, 21]
            }

#Calling DataFrame constructor on list
dfDance = pd.DataFrame(lstNames)

print(dfDance.isnull())

dfDance.fillna("MISSING", inplace=True)

print(dfDance)