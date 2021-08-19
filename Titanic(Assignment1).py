#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#importing datasets(training and testing)
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


# In[4]:


#gives starting few rows of the datasets if no value is give takes 5 as default

train.head()  


# In[5]:


#gives ending few rows of the datasets if no value is give takes 5 as default

train.tail()


# In[7]:


#shows shape of the dataset

train.shape


# In[8]:


# To get max,min,count and other stats(gives numerical data)

train.describe()


# In[9]:


# gives info about columns

train.info()


# In[19]:


#to find total of null values

train.isnull().sum()


# In[16]:


#to find null data in percentage

percentage_ofNullValues = train.isnull().sum() *100/len(train)
print(percentage_ofNullValues)


# In[20]:


#to round of values

print(round(percentage_ofNullValues),2)


# In[ ]:




