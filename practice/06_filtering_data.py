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


'''
You can use the .query function on dataframes.
personally, I think this is nicer and easier to read.
however, it is only meant to select a subset of data. Boolean indexing might be better
if you need to change the underlying data after you filter.
'''

# PRACTICE
# Show all columns, but only for those age 21 and older. Use .query


# Do the same thing, but with boolean indexing


# Show only 21 or older, but just show the Dancer column. Use .query


# Show only 21 or older, but just show the Dancer column. Use boolean indexing


# Advantage of boolean indexing: updating the df after you filtered
# Add 3 to the age of everyone 21 or older:


# to do that with .query, you have to do a workaround with .index and still use .loc


# but if you just want to grab a subset, and especially if the criteria are a little complex
# I think .query is much more straightforward.

# try printing out only those above 21 and their type is Jazz



########
## affecting the dataframe in place
########

# print out your dataframe


# Now, without printing, do a query (like age over 21) on the dataframe
# but also add inplace = True to the query function



# now print out your dataframe again. Notice that by putting inplace = True, you altered the 
# original dataframe.


# essentially the same as setting your df variable equal to the result of your query.

'''
    These 2 lines of code accomplish the same thing:

        dfDance = dfDance.query("Type == 'Modern'")
        dfDance.query("Type == 'Modern'", inplace = True)

'''
