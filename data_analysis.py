import numpy as np
import pandas as pd

# reads the data and puts it into a dataframe
grades_df = pd.read_csv('grades.csv')

print(grades_df.columns)

# creates a new dataframe to put data into instead of transforming the old one
new_grades_df = pd.DataFrame()

# setting up new data frame and extracting just the data I need
new_grades_df['gender'] = grades_df['Gender']
new_grades_df['student_name'] = grades_df['Student Name']
new_grades_df['current_course'] = grades_df['Current Course']
new_grades_df['credits'] = grades_df['Number of Credits']
new_grades_df['pre_algebra'] = grades_df['DSA Avg.']
new_grades_df['algebra_1'] = grades_df['DSA Avg..1']
new_grades_df['algebra_2'] = grades_df['DSA Avg..2']
new_grades_df['honors_algebra_2'] = grades_df['DSA Avg..3']
new_grades_df['geoemetry'] = grades_df['DSA Avg..4']
new_grades_df['honors_geometry'] = grades_df['DSA Avg..5']
new_grades_df['math_apps'] = grades_df['DSA Avg..6']
new_grades_df['personal_finance'] = grades_df['DSA Avg..7']
new_grades_df['trigonometry'] = grades_df['DSA Avg..8']
new_grades_df['advanced_algebra'] = grades_df['DSA Avg..9']
new_grades_df['honors_pre_calculus'] = grades_df['DSA Avg..10']


