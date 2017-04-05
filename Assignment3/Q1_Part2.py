
# coding: utf-8

# ## NYC Collision Analysis

# ### For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)

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

df = pd.read_csv('Data/vehicle_collisions.csv', index_col = 3) 


# In[5]:

df.head()


# In[6]:

df = df[['VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE', 'VEHICLE 5 TYPE']]


# In[7]:

df['VEHICLES_INVOLVED'] = df.notnull().sum(axis=1)


# In[8]:

df = df.reset_index()[['BOROUGH','VEHICLES_INVOLVED']]


# In[9]:

df = df.pivot_table(index='BOROUGH', columns='VEHICLES_INVOLVED', aggfunc=len, fill_value=0)


# In[10]:

os.makedirs('Output', exist_ok=True)


# In[11]:

df.to_csv('Output/Q1Part2.csv')


# In[12]:

print('Completed - results are saved in Output/Q1Part2.csv')

