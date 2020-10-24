# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:26:53 2020

@author: RebekahDSK
"""

import pandas as pd
import numpy as np
coders_df = pd.read_csv(r"C:\Users\RebekahDSK\Desktop\gwu-arl-data-pt-09-2020-u-c\02-Homework\04-Python-Pandas\03-Pandas-Project\Mini-Project-Part-1\Resources\2016-FCC-New-Coders-Survey-Data.csv")
print(coders_df)

# Inspect all columns
print(coders_df.columns)

# Create a new table using the following columns:
# [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 29, 30, 32, 36, 37, 45, 48, 56, 110, 111]
Extracted_coders_df = coders_df.iloc[:,[0, 1, 2, 3, 4, 7, 8, 9, 10,11, 29, 30, 32, 36, 37, 45, 48, 56, 110, 111]]
print(Extracted_coders_df)

Extracted_coders_df.dtypes

# Get a count of all 0.0 and 1.0
Extracted_coders_df['AttendedBootcamp'].value_counts()

# Replace all instances of "0.0" with No, and all instances of "1.0" with "Yes" in the 'Attended Bootcamp' column
Extracted_coders_df["AttendedBootcamp"]= Extracted_coders_df["AttendedBootcamp"].replace({0:"No", 1:"Yes"})
Extracted_coders_df

# Extract rows corresponding only to people who attended a bootcamp
attended_bootcamp = Extracted_coders_df.loc[Extracted_coders_df["AttendedBootcamp"] == "Yes"]
attended_bootcamp

# Calculate average age of attendees
age_average = attended_bootcamp["Age"].mean()
age_average

# Calculate how many attendees hold degrees
unique_degrees = (attended_bootcamp["SchoolDegree"].value_counts())
unique_degrees

# Calculate average post-bootcamp salary
avg_post_bootcamp = attended_bootcamp["BootcampPostSalary"].mean()
avg_post_bootcamp
​
# Calculate how many people attended a bootcamp
count = attended_bootcamp["AttendedBootcamp"].value_counts()
count

#Count number of attendees who self-identify as male; female; or are of non-binary gender identification
gender = (attended_bootcamp["Gender"].value_counts())
gender