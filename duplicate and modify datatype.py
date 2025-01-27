#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data =pd.read_csv("data_clean.csv")
data


# In[3]:


#Data Structure
print(type)


# In[4]:


data1=data.drop(['Unnamed: 0',"Temp C"],axis=1)
data1


# In[5]:


data.info()


# In[6]:


#Convert the month column datatype to integer data type
data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1


# In[7]:


data1.info()


# In[8]:


#Checkinng the duplicate values in table
#Print the duplicate rows
data1[data1.duplicated()]


# In[9]:


#Print all duplicated rows
data1[data1.duplicated(keep=False)]


# In[12]:


#Change column names(Rename the columns)
data1.rename({'Solar.R': 'Solar','Temp':'Temperature'},axis=1,inplace=True)
data1


# In[15]:


data1.info()


# In[ ]:




