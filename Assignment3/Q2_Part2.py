
# coding: utf-8

# ## Employee Compensation Analysis

# In[1]:

print('Start of script...')


# In[2]:

import numpy as np
import pandas as pd
import datetime
import os


# In[3]:

print('Reading Data/employee_compensation.csv...')


# In[4]:

df = pd.read_csv('Data/employee_compensation.csv') 


# ### Filter data by calendar year and find average salary (Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# 

# In[5]:

df1 = df[df['Year Type'] == 'Calendar']
df1 = df1[['Employee Identifier', 'Salaries', 'Overtime', 'Other Salaries', 'Retirement', 'Health/Dental', 'Other Benefits']]
df1.head()


# In[6]:

df1['Avg Salary Across Categories'] = df1.apply(lambda x:(x[1] + x[2] + x[3])/3, axis=1)
df1['Avg Benefits Across Categories'] = df1.apply(lambda x:(x[4] + x[5] + x[6])/3, axis=1)


# In[7]:

print('Avg salaries and benefits - top 5 (df.head()):\n')
print(df1.head()[['Employee Identifier','Avg Salary Across Categories', 'Avg Benefits Across Categories']])


# ### Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)

# In[8]:

df2 = df1[df['Overtime'] > 0.05 * df['Salaries']][['Employee Identifier','Salaries', 'Overtime']]
print('Overtime greater than 5% of salary - top 5 (df.head()):\n')
print(df2.head())


# ### For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value. Display the top 5 Job Families according to this percentage value using df.head()

# In[9]:

df3 = df[['Job Family', 'Total Benefits', 'Total Compensation']]
df3.head()


# In[10]:

df3 = df3.groupby('Job Family').agg({'Total Benefits':np.mean,'Total Compensation':np.mean})
df3.head()


# In[11]:

df3['Percentage'] = df3['Total Benefits'] / df3['Total Compensation'] * 100
df3 = df3.sort_values('Percentage', ascending=False)
print('Percentage of Benefits/Compensation for each Job Family :\n')
print(df3.head())


# In[12]:

os.makedirs('Output', exist_ok=True)


# In[13]:

df3.to_csv('Output/Q2Part2.csv')


# In[14]:

print('Completed - results are saved in Output/Q2Part2.csv')

