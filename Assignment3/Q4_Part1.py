
# coding: utf-8

# ## Movie awards analysis
# 

# ### Extract data from awards column to create multiple columns

# In[1]:

print('Start of script...')


# In[2]:

import numpy as np
import pandas as pd
import datetime
import os
import re


# In[3]:

print('Reading Data/employee_compensation.csv...')


# In[4]:

df = pd.read_csv('Data/movies_awards.csv') 


# In[5]:

df = df[['Title', 'Year', 'Awards']]


# In[6]:

df = df[pd.notnull(df['Awards'])]
df.head()


# In[7]:

p = re.compile('^((Won? (\d+) (\w*(\s\w*)*)( & )?)?(Nominated for? (\d+) (\w*(\s\w*)*))?\u002e\s?)?((Another )?(((\d+) win\w?)( & )?)?((\d+) nomination\w?)?\u002e)?$')


# In[8]:

def extract_awards(row):
    if pd.notnull(row['Awards']):
        m = p.match(row['Awards'])
        if m:
            spl_win_count = m.group(3)
            spl_win_type = m.group(4)
            if spl_win_count and spl_win_type:
                if spl_win_type[-1] == 's':
                    spl_win_type = spl_win_type[:-1]
                spl_win_type = spl_win_type + ' Wins'    
                row[spl_win_type] = spl_win_count
            
            spl_nom_count = m.group(8)
            spl_nom_type = m.group(9)
            if spl_nom_count and spl_nom_type:
                if spl_nom_type[-1] == 's':
                    spl_nom_type = spl_nom_type[:-1]
                spl_nom_type = spl_nom_type + ' Nominations'    
                row[spl_nom_type] = spl_nom_count
                                
            another_win_count = m.group(15)
            if another_win_count:
                row['Awards_Won'] = another_win_count
                if spl_win_count:
                    row['Awards_Won'] = int(row['Awards_Won']) + int(spl_win_count)
            else:  
                row['Awards_Won'] = 0
                
            another_nom_count = m.group(18)
            if another_nom_count:
                row['Nominations'] = another_nom_count
                if spl_nom_count:
                    row['Nominations'] = int(row['Nominations']) + int(spl_nom_count)
            else:
                row['Nominations'] = 0                
        else:
            row['Awards_Won'] = 0
            row['Nominations'] = 0
    else:
        row['Awards_Won'] = 0
        row['Nominations'] = 0
    return row    


# In[9]:

df = df.apply(extract_awards,axis=1)
df = df.fillna(0)
df.head()


# In[10]:

os.makedirs('Output', exist_ok=True)


# In[11]:

df.to_csv('Output/Q4Part1.csv')


# In[12]:

print('Completed - results are saved in Output/Q4Part1.csv')


# In[ ]:



