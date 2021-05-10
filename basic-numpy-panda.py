#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
print(os.listdir("../input/stocknews"))


# In[2]:


Series = pd.Series([3,-5,7,4], index = ['a','b','c','d'])


# In[3]:


type(Series)


# In[4]:


Series


# In[5]:


data = {'Country' : ['Belgium','India','Brazil'],
        'Capital' : ['Brussels','New Delhi','Brassilia'],
        'Population' : [1234,1234,1234]}
datas= pd.DataFrame(data,columns=['Country','Capital','Population'])


# In[6]:


print(type(data))
print(type(datas))


# In[7]:


dictionary={"Name":["John","James","Awi","Kewi"],
           "Age":[15,16,17,18]}
print(dictionary)


# In[8]:


data_dict = pd.DataFrame(data=dictionary,index=range(4),columns=["Name","Age"])
print(data_dict)


# In[9]:


dict_new={"Name":["King","Arthur","Jurdi","Hirdi"],
           "Age":[25,35,45,55]}
dict_new=pd.DataFrame(data=dict_new,index=range(4),columns=["Name","Age"])
print(dict_new)


# In[10]:


data_dict = pd.concat([data_dict,dict_new],axis = 0, ignore_index=True)
print(data_dict)


# In[ ]:





# In[ ]:




