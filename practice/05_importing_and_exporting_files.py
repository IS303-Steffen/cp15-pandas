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

# =============================
# IMPORTING AND EXPORTING FILES
# =============================

'''
OVERVIEW
--------
Pandas includes a lot of functions that start with .read_ like .read_csv()
You can pull in several types of data into DataFrames. This will be especially
useful once we work with databases.

You can also export a DataFrame to several different file types using any of
the .to_ methods like .to_csv()

'''
import pandas as pd


# 1. IMPORTING FILES AS DATAFRAMES
# Import the included dancers.csv file. using pd.read_csv() .csv stands for
# "comma separated values" and is a common way of storing data.
# Print out the DataFrame after you import the .csv file.


# 2. ALTER THE DATAFRAME THEN EXPORT IT
# Add an asterisk to everyone's name, then save it as altered_dancers.csv
# Using the .to_csv() method. If you don't want the indices to be included
# add the parameter "index" with False as the argument


# 3. EXPORT TO AN EXCEL FILE
# Export your DataFrame to an Excel file called altered_dancers.xlsx using
# the .to_excel() method.



'''
SOME NOTES ON .read_excel()
---------------------------
- If your Excel Workbook has multiple sheets, it just grabs the first one by 
  default
- You can use the "sheet_name" parameter to specify a sheet name to enter. You
  can enter the number of the sheet (1 for the first, etc.) or the name of the
  sheet.
- If you enter None as the argument, then it will give you all of the sheets
  as a dictionary of DataFrames.

'''


# 4. READ AN EXCEL FILE
# Import the mock_grades.xlsx file to a DataFrame and print it out


# 5. READ A SPECIFIC SHEET OF AN EXCEL FILE
# Use the "sheet_name" parameter of read_excel() to get the "ACC 200" sheet
# into a DataFrame. Print out the DataFrame


# 6. GET ALL SHEETS OF AN EXCEL FILE
# Set "sheet_name" equal to None. Print out the dictionary you get back.


'''
CAN I EXPORT MULTPLE DATAFRAMES TO ONE EXCEL WORKBOOK?
------------------------------------------------------
If you want to export mulitple dataframes into one Excel file,
you need to pip install xlsxwriter and then make a ExcelWriter object
with pandas. I won't cover that, but look it up if that sounds interesting.
'''
