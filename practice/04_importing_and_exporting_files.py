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

######
# Importing to Pandas
######
# you can import files as pandas dataframes.
# write pd.read_ and look at all the functions you have available. 
# let's just to pd.read_csv and get the dancers.csv file I've given you.:



# print out your imported file


# add an asterisk to everyone's name, then save it as altered_dancers.csv



######
# Exporting
######

# after any dataframe, type .to and see the functions that dataframes have built in
# for exporting. Try just using .to_csv or .to_excel.
# give it a filepath. I also usually add index = False to prevent the row index from being added
# as its own column, but occasionally, you might want to keep it.


########
# EXCEL
########


# read_excel works, but just some stuff to be aware of with multiple sheets:
# If your excel workbook as multiple sheets, it will just grab the first one by default
# try importing the mock_grades.xlsx file and printing it out.



# you can specify a specific sheet by index or by name:
# try to get the 2nd sheet by either putting sheet_name = 1 or sheet_name = "ACC 200"
# print it out.



# or, you can specify sheet_name = None and then it will return all the sheets as dataframes
# separated in a dictionary with the sheet name as the key and the dataframe as the value


#####
# Can I export to excel?
#####

# Yes, just use .to_excel.
# If you want to export mulitple dataframes into one excel file,
# you need to pip install xlsxwriter and then make a ExcelWriter object
# with pandas. I won't cover that, but just google that if it sounds interesting.
