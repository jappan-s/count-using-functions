#!/usr/bin/env python
# coding: utf-8

# In[3]:


def str(s):
    UPPER_CASE=0 
    LOWER_CASE=0
    for c in s:
        if c.isupper():
           UPPER_CASE+=1
        elif c.islower():
           LOWER_CASE+=1
        
    print ("Original String : ", s)
    print ("number of upper case characters : ", UPPER_CASE)
    print ("number of lower case Characters : ", LOWER_CASE)

str('The quick Brow Fox')


# In[ ]:





# In[ ]:




