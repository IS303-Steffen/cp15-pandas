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
# FILTERING USING CONDITIONS
# ==========================

'''
OVERVIEW
--------
You now know how to get access to parts of a DataFrame and change the data.
But what if you want to only get / change the data based on some condition,
like only those 20 years and older?

I will show 2 ways of doing this: 

1. .query()
    - You write a condition similar to an SQL query. The main disadvantage is
      that it isn't easy to change the data using this. It is an easy way to
      get the data though.

2. boolean indexing (with .loc)
    - This lets you specify specific rows to grab and makes it easy to alter
      the data in the same go. I think the syntax of this is more confusing,
      but being able to alter data makes it very useful.


OTHER WAYS I WILL NOT SHOW YOU
------------------------------
I will NOT show examples of the following. But here are short descriptions.
Feel free to look them up if they sound useful.

- .isin()
    - returns rows where a column's value matches a provided list of values.
- .between()
    - returns rows that are between 2 values (inclusive). Useful for numerical
      data
- .nlargest() and .nsmallest()
    - returns the smallest or largest n number of rows in a column you specify.
- .where() and .mask()
    - you specify a condition and it either keeps just those rows or everything
      except those rows. Similar to boolean indexing.
- .apply()
    - combine with boolean indexing to use custom functions in your filtering
- .filter()
    - allows you to specify rows or columns to select based on conditions of 
      the index or the column label, rather than the data itself.
'''

import pandas as pd

dancers_dict = {
    "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
    "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
    "Age" : [18, 23, 19, 20, 21, 22, 21]
}

df_dancers = pd.DataFrame(dancers_dict)
print(df_dancers, "\n")

# =======================
# FILTERING WITH .query()
# =======================

# 1. FILTER USING .query()
# Show all columns, but only for those age 21 and older. Use .query
print(df_dancers.query("Age > 21"), "\n")

# 2. FILTER USING .query(), SHOW A SINGLE COLUMN
# Show only 21 or older, but just show the Dancer column. Use .query.
# Just use brackets after the query method to get the "Dancer" column.
print(df_dancers.query("Age > 21")["Dancer"], '\n')

# 3. FILTER USING .query() WITH MULTIPLE CONDITIONS
# Show only 21 or older that have a dance Type of Jazz
print(df_dancers.query("Age > 21 and Type == 'Jazz'"), '\n')

# 4. CHANGE YOUR DATAFRAME WITH .query() BY USING inplace=True
# Print out your DataFrame. Then run a query to only retain those with an age
# over 21, but add the parameter inplace with True as the argument. Print out
# your DataFrame again. What happened?
print(df_dancers, '\n')
df_dancers.query("Age > 21", inplace=True)
print(df_dancers, '\n')

'''
DO I NEED TO USE inplace=True?
------------------------------
These 2 lines of code accomplish the same thing:

df_dancers = df_dancers.query("Type == 'Modern'")
df_dancers.query("Type == 'Modern'", inplace = True)
'''

# ============================
# BOOLEAN INDEXING WITH .loc[]
# ============================

'''
Boolean indexing just means you are getting the indexes with a True or False
value attached to them. 

I personally think this is uglier, but also much more useful because you can
change the values that you get. .query() only lets you get the values.
'''

# recreating the DataFrame just in case the previous code messes it up.
df_dancers = pd.DataFrame(dancers_dict)
print(df_dancers, "\n")

# 5. PRINT OUT BOOLEAN INDEX RESULTS OF A CONDITION
# Print out this piece of code: df_dancers["Age"] > 21
# What is it giving you? Why is this useful?

print(df_dancers["Age"] > 21, '\n')

# 6. FILTER USING BOOLEAN INDEXING WITH .loc[]
# Use .loc[] but inside the brackets, put df_dancers["Age"] > 21. That will
# provide the specific rows to keep and which to get rid of.
print(df_dancers.loc[df_dancers["Age"] > 21], '\n')

# 7. FILTER USING BOOLEAN INDEXING, SHOW A SINGLE COLUMN
# Do the same thing as above, but only show the Age column
print(df_dancers.loc[df_dancers["Age"] > 21, "Age"])

# 8 UPDATE VALUES BASED ON BOOLEAN INDEXING FILTERING
# This is the main advantage of boolean indexing over .query.
# Add 3 to the age of any dancer that is exactly 21 years old. Print out the
# DataFrame to make sure your changes happened.
df_dancers.loc[df_dancers["Age"] == 21, "Age"] += 3
print(df_dancers, '\n')


'''
MULTIPLE CONDITIONS WITH BOOLEAN INDEXING
-----------------------------------------
To add multiple logical conditions, you need to:
    1. put each condition in parentheses
    2. Use panda's version of operators:
        - and: &
        - or:  |
        - not: ~

    e.g. df.loc[(df["Column"] == "X") & (df["Column2"] < 10)]
'''

# 9. FILTER USING MULTIPLE CONDITIONS
# Print out dancers under 22 or any that dance the Tango
print(df_dancers.loc[(df_dancers["Age"] < 22) | (df_dancers["Type"] == "Tango")], '\n')

# 10. FILTER USING MULTIPLE CONDITIONS
# Do the same thing, but only print out the Dancer name.
print(df_dancers.loc[ (df_dancers["Age"] < 22) 
                    | (df_dancers["Type"] == "Tango"), "Dancer"], '\n')

# 11. UPDATE VALUES BASED ON FILTER
# Using the same filter as above, add an asterisk * to the end of Dancer names
# that match the filter. Print out your DataFrame again to make sure the change
# was successful.
df_dancers.loc[ (df_dancers["Age"] < 22)
              | (df_dancers["Type"] == "Tango"), "Dancer"] += '*'

print(df_dancers)

'''
TIP
---
Remember that what you are doing here is one of the main advantages of using
pandas over other data types / importing Excel files with openpyxl. You can
make changes to entire columns / subsections without using loops. It is very
computationally efficient. Plus, it is fewer lines of code.
'''
