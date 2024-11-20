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

# =======================================
# PRACTICE - ACCESSING DATA IN DATAFRAMES
# =======================================

# PRACTICE
'''
Practice Problem: Managing a Classroom with Pandas
'''

students_dict = {
    "Names" : ["Frank", "Jacob", "James", "Alice", "Emily"],
    "Math" : [45, 56, 78, 88, 99],
    "English" : [90, 87, 99, 99, 23],
    "Science" : [12, 56, 98, 44, 55]
}


# PART 1:
# Convert the dictionary to a Pandas DataFrame and print it out.
import pandas as pd
df_students = pd.DataFrame(students_dict)
print(df_students)


# PART 2: 
# - print all data but for only those that have a Math score over 85
# - do the same as above, but only show the names of the students.

print()
print(df_students.loc[df_students["Math"] > 85])
print()
print(df_students.loc[df_students["Math"] > 85, "Names"])

# PART 3: 
# - Show all columns for all students that got an 85 or above in 
#   English, but also got a 50 or below in Science
# - Change the Math score of these students to be None, then print the
#   DataFrame again. Note that in Pandas, None will turn into NaN, meaning
#   "not a number"

print(df_students.loc[(df_students["English"] >= 85) & (df_students["Science"] <= 50)])
df_students.loc[(df_students["English"] >= 85) & (df_students["Science"] <= 50), "Math"] = None
print(df_students)
