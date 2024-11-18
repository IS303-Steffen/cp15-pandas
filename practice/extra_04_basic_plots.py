import matplotlib.pyplot as plot
import pandas as pd

dfImportedFile = pd.read_excel('dummy_data.xlsx')
print(dfImportedFile)
# you can also do math functions on columns by accessing a column in a dataframe and doing a function like .sum(), .count() or .median()

# find the median hours slept of the filtered data:
med_hours_slept = dfImportedFile['hours_slept'].median()
print(med_hours_slept)


# group by
#dfPostgres2.groupby("column_to_group_on")["column_to_a_calculation_on"].sum()
result = dfImportedFile.groupby("gender")["hours_slept"].mean()

print(result)

######
# charts
######

# also a topic we could spend weeks on, but you can dive more into that in data analytics courses

# basic idea is that you specify a chart type
# and tell it the axis
# do a bar graph with the x-axis as gender and the y-axis as 
result.plot(kind='bar')
plot.title = "Average Hours slept by gender"
plot.xlabel("Gender")
plot.ylabel("Hours Slept")
plot.show()
