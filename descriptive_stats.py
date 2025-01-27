#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[10]:


df=pd.read_csv("universities.csv")
df


# In[11]:


np.mean(df["SAT"])


# In[8]:


df.describe()


# In[12]:


np.std(df["GradRate"])


# In[14]:


np.median(df["GradRate"])


# In[17]:


np.var(df["GradRate"])


# In[25]:


np.mean(df["Top10"])


# In[26]:


#Visualize the gradRate using histogram
import matplotlib.pyplot as plt
import seaborn as sns


# In[29]:


plt.figure(figsize=(6,3))
plt.title("Acceptance Ratio")
plt.hist(df["Accept"])


# In[36]:


sns.histplot(df["Accept"],kde=True)#kde=kernal density estimate


# In[37]:


sns.histplot(df["Top10"],kde=True)


# In[39]:


sns.histplot(df["SAT"],kde=True)


# In[41]:


sns.histplot(df["SFRatio"],kde=True)


# In[45]:


sns.histplot(df["GradRate"],kde=True)


# In[54]:


## Observations
#In Acceptance ratio the data distribution is non-symmetrical and right skewed

