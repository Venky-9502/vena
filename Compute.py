#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python modules
#-module is a collection of functions
#-The file should be saved as .py file(python script file)


# In[7]:


def mean_value(*n):
    sum=0
    counter=0
    for x in n:
        counter=counter +1
        sum+=x
    mean =sum/counter
    return mean


# In[9]:


mean_value(1,2,3,4,5,6)


# In[8]:


#PRoduct of given numbers
def product(*n):
    result=1
    for i in range(len(n)):
        result *=n[i]
    return result


# In[10]:


product(5,3,12)


# In[ ]:




