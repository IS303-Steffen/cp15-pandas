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

import pandas as pd # pandas gets you dataframes

# read the excel file into a pandas dataframe with pd.read_excel
dfImportedFile = pd.read_excel(r'dummy_data.xlsx')
print(dfImportedFile)
########
# inserting columns
########

# use .insert on a dataframe to add a column
# .insert(index, "name of column", data)
# for the data, you can either supply a single variable to apply to all rows,
# a list with the exact number of elements as there are rows
# or just provide another column from an existing dataframe.

# try inserting a new column called  "test_column" with "test" as the value for each row
dfImportedFile.insert(0, "test_column", "x")
print()
print(dfImportedFile)

# now make a column called "half_age", at position 2 that is the original age column divided by 2
# put it right after the original age column

dfImportedFile.insert(5, "half_age", dfImportedFile["age"] / 2)
print(dfImportedFile)


#######
# deleting columns / rows
#######

# delete the original age column using del. del is standard python to delete anything
# try deleting the "age" column
del dfImportedFile["age"]
print("\n", dfImportedFile)

# you can also use the .drop method to delete columns or rows.
# axis = 1 means columns, axis = 0 means rows (the default).
# you can add inplace = True

dfImportedFile.drop("test_column", axis=1, inplace = True)
print("\n", dfImportedFile)


# provide a list of indices for it to drop specific rows
# try to drop the 1st and 4th rows.
dfImportedFile.drop(index = [1,4], inplace = True)
print("\n", dfImportedFile)

#########
# adding rows
#########

# there used to be a function called "append" in pandas, but it is now deprecated
# now the main way to add data together is to use df.concat() to stick two dataframes together

# Here I'm just creating a new dataframe and reimporting the original one so it has all the original columns
# then I use .concat to put them together.
new_df = pd.DataFrame({"first_name" : ["Jimmy", "John"], "last_name" : ["Simmy", "Song"], "age" : [20, 21], 
                       "gender" : ["Male", "Female"], "hours_slept" : [8.0, 9.3], "happiness_rating": [87, 93]})

reimported_df = pd.read_excel(r"dummy_data.xlsx")

# note how I use ignore_index = True.
# that makes it so that the 2nd dataframe will have its index numbers
# redone. I recommend doing this.
combined_df = pd.concat([reimported_df, new_df], ignore_index = True)

print("\n", combined_df)

####
# adding individual rows using .loc
#####

# you can also add and individual row using .loc. Its a little cumbersome.
# if you don't want to repeat indexes, then you need to find the max index and add 1 to it
new_max_index = combined_df.index.max() + 1
combined_df.loc[new_max_index] = ["George", "Harrison", 80, "Male", 8, 85]
print("\n", combined_df)







