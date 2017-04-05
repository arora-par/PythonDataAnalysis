
# coding: utf-8

# ### Employee Compensation Analysis

# ### Find out the highest paid departments in each organization group by calculating mean of total compensation for every department

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


# In[5]:

df = df[['Organization Group', 'Department', 'Total Compensation']]


# In[6]:

grouped = df.groupby(by=['Organization Group', 'Department']).mean()
flattened = grouped.reset_index()
final = flattened.groupby(by='Organization Group').agg({'Department':max, 'Total Compensation':max})
final = final.sort_values('Total Compensation', ascending=False)


# In[7]:

os.makedirs('Output', exist_ok=True)


# In[8]:

final.to_csv('Output/Q2Part1.csv')


# In[9]:

print('Completed - results are saved in Output/Q2Part1.csv')

