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

'''
Practice Problem: Managing a Classroom with Pandas

You are given a task to manage a classroom's score record using Pandas.
The class has 5 students and they have scores in three subjects: Math, English, and Science. 
'''
# Steps:
# 1. Create a Dictionary:(I'm just gonna give this to you for time's sake)
# Make a dictionary with the names of 5 students as keys and a list of their scores
# in Math, English, and Science as values. E.g. "Frank" : [80, 94, 73]

dictionaryStudents = {"Names" : ["Frank", "Jacob", "James", "Alice", "Emily"],
                      "Math" : [ 45, 56, 78, 88, 99],
                      "English" : [90, 87, 99, 99, 23],
                      "Science" : [12, 56, 98, 44, 55]}


# 2. Convert to DataFrame: Convert this dictionary to a Pandas DataFrame and print it out.


# 3. Access Specific Rows and Columns: 
#     - Print the Math scores of all students.
#     - Print the name and scores of all subjects of the third student.


# 4. Update Value: 
#     - Update the English score of the first student to 75.
#     - Update the Science score of the last student to 85.


# Science is the 4th column. Get the last row by doing -1. Or just put 4.


# 5. Filter: 
#     - print all data but for only those that have a Math score over 85
#     - do the same as above, but only show the names of the students.


# 6. More challenging Filter: 
#     - Show the names of all students that got an 85 or above in 
#       English, but a 50 or below in Science


# 7. Updating multiple rows simultaneously
#    - Add 10 to the Math scores of all students
