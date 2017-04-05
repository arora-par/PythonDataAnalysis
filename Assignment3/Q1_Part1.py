
# coding: utf-8

# ## NYC Collision Analysis

# ### For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City

# In[1]:

print('Start of script...')


# In[2]:

import numpy as np
import pandas as pd
import datetime
import os


# In[3]:

print('Reading Data/vehicle_collisions.csv...')


# In[4]:

df = pd.read_csv('Data/vehicle_collisions.csv', index_col = 0, parse_dates=[1]) 


# In[5]:

df.head()


# In[6]:

df = df[ (df['DATE'] > datetime.date(year=2015,month=12,day=31)) & (df['DATE'] < datetime.date(year=2017,month=1,day=1))]


# In[7]:

df['MONTH']= df['DATE'].apply(lambda x: x.month)


# In[8]:

df1 = df[df['BOROUGH'] == 'MANHATTAN']


# In[9]:

df = df.groupby(by='MONTH').count()
df['NYC'] = df['DATE']
df = df['NYC']


# In[10]:

df1 = df1.groupby(by='MONTH').count()
df1['MANHATTAN'] = df1['DATE']
df1 = df1['MANHATTAN']


# In[11]:

combined = pd.concat([df1,df], axis=1)


# In[12]:

combined['PERCENTAGE'] = combined['MANHATTAN'] / combined['NYC'] 


# In[13]:

os.makedirs('Output', exist_ok=True)


# In[14]:

combined.to_csv('Output/Q1Part1.csv')


# In[15]:

print('Completed - results are saved in Output/Q1Part1.csv')

