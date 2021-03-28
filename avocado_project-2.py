#!/usr/bin/env python
# coding: utf-8

# # My Avocado Journey 

# ### This is my very first project. I want to compare avocado prices and consumption between 2 regions of USA - California and Albany.

# In[66]:


import numpy as np #importing necessary libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('avocado.csv') #creating dataset


# In[3]:


df.head(5)


# In[4]:


df.dtypes


# In[5]:


df.columns #let see the columns in dataset


# In[6]:


df['region'].unique() #checking for regions


# In[7]:


df.isnull().sum()


# ### Excellent! There aren't empty raws.

# #### Let's make some changes with columns.

# In[79]:


df.rename({'Small Bags':'Small Hass', 'Large Bags':'Large Hass', 'XLarge Bags':'XL Hass'}, axis=1, inplace=True)
df[['Year', 'Month', 'Day']] = df['Date'].str.split('-', n=2, expand=True)
df.drop(columns=['Date', 'Unnamed: 0', '4046', '4225', '4770'], inplace=True)


# In[31]:


df = df[['Day','Month','Year', 'region', 'AveragePrice', 'Total Volume', 'type','Total Bags','Small Hass',
                  'Large Hass', 'XL Hass']]
df.head()


# In[37]:


df_cali = df [ df['region'] == 'California']
df_albany = df [ df['region'] == 'Albany']


# In[36]:


#CALI
#df_cali['AveragePrice'].describe() #getting the most important info about prices
#df_cali[df_cali['AveragePrice'] == 0.67]
#df_cali[df_cali['AveragePrice'] == 2.58]
#df_cali['AveragePrice'].max()- df_cali['AveragePrice'].min()
# The cheapest awokado in California was sold in Feb 2017 and the most expensive one was sold in Oct 2016. The difference between those prices was about 1.91$ - huge difference.


# In[38]:


df_both = df_cali.append(df_albany)
df_both


# In[70]:


df_both.groupby(['region', 'Year']).describe().AveragePrice


# In[77]:


data_Pivot = df_both.pivot_table(values='AveragePrice', index='Month'], columns='region', aggfunc=pd.Series.nunique)
data_Pivot.plot(kind='line', figsize = (15,10))

