import numpy as np
from numpy.core.fromnumeric import mean
import pandas as pd
from pandas.core.arrays import integer


# Step 2: Perform data preparation and cleaning

# Load the data set into a dataframe using Pandas
performance_df = pd.read_csv('StudentsPerformance.csv')

# explore the number of columns and rows in the dataset.
shape = performance_df.shape
print(f'Rows = {shape[0]}')
print(f'Columns = {shape[1]}')

print('Header Names:')
print(performance_df.columns)

# Math Section - Determine how to take out data who score 10 or below.
print('Math Information')
math_series = pd.Series(data=performance_df['math score'])
print(f'Average Math Score = {math_series.mean().round(1)}')
print(f'Range = {math_series.max()-math_series.min()}')

# Reading Section - Determine how to take out data who score 10 or below.
print('Reading Information')
reading_series = pd.Series(data=performance_df['reading score'])
print(f'Average Reading Score = {reading_series.mean().round(1)}')
print(f'Range = {reading_series.max()-reading_series.min()}')

# Writing Section - Determine how to take out data who score 10 or below.
print('Writing Information')
writing_series = pd.Series(data=performance_df['writing score'])
print(f'Average Writing Score = {writing_series.mean().round(1)}')
print(f'Range = {writing_series.max() - writing_series.min()}')

# demograph info
demo_info_titles = performance_df.columns[:5]
print(demo_info_titles)

for title in demo_info_titles:
    performance_df[title] = performance_df[title].astype('string')

print(performance_df.dtypes)

# gender breakdown of average scores
print(performance_df.groupby('gender').mean().round(1))

# free/reduced lunch breakdown
print(performance_df.groupby(['lunch','gender']).mean().round(1))

# parental level of education breakdown
print(performance_df.groupby('parental level of education').mean().round(1))

# race/ethnicity and gender
print(performance_df.groupby(['race/ethnicity','gender']).mean().round(1))

# test prep breakdown
print(performance_df.groupby(['gender','test preparation course']).mean())

# math score influences
print(performance_df.groupby(['parental level of education','race/ethnicity']).mean())




