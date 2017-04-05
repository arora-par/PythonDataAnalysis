
# coding: utf-8

# ## Cricket Matches Analysis

# ### Calculate the average score for each team which host the game and win the game

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

df = pd.read_csv('Data/cricket_matches.csv') 


# In[5]:

df = df[['home', 'away', 'winner', 'innings1', 'innings2', 'innings1_runs', 'innings2_runs']]
df.head()


# In[6]:

df = df[df['home'] == df['winner']]
df.head()


# In[7]:

df['winner_runs'] = df.apply(lambda x:x['innings1_runs'] if x['innings1'] == x['home'] else x['innings2_runs'], axis = 1)
df.head()


# In[8]:

df = df.groupby('home').agg({'winner_runs':np.mean})
print('Team-wise avg for home wins - top 5 (df.head()) :\n')
print(df.head())


# In[9]:

os.makedirs('Output', exist_ok=True)


# In[10]:

df.to_csv('Output/Q3Part1.csv')


# In[11]:

print('Completed - results are saved in Output/Q3Part1.csv')


# In[ ]:



