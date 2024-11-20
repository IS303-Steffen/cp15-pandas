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

#list of data
dict_dancers =  {   "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
                "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
                "Age" : [18, 23, 19, 20, 21, 22, 21]
            }


import pandas as pd
# given the above dictionary, make a dataframe and,
# using filtering, show all the dancers that dance Jazz or Square
