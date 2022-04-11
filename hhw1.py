#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[13]:


a = np.array(
    [[1, 2, 3, 3, 1], 
    [6, 8, 11, 10, 7]]
).transpose()


# In[14]:


a


# In[21]:


mean_a = np.mean(a, axis = 0)


# In[22]:


mean_a


# In[33]:


a_centered=np.subtract(a, mean_a)


# In[34]:


a_centered


# In[35]:


a1=a_centered[:,0]
a2=a_centered[:,1]
a_centered_sp=np.dot(a1,a2)
a_centered_sp


# In[36]:


N=a.shape[0]
N


# In[37]:


np.cov(a.transpose())


# In[38]:


import pandas as pd


# In[39]:


authors = pd.DataFrame({'author_id':[1, 2, 3],
                   'author_name':['Тургенев', 'Чехов', 'Островский']}, columns=['author_id', 'author_name'])


# In[40]:


authors


# In[41]:


books = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 
                     'price':[450, 300, 350, 500, 450, 370, 290]}, 
                      columns=['author_id', 'book_title', 'price'])


# In[42]:


books


# In[45]:


authors_price = pd.merge(authors, books)
authors_price


# In[46]:


top5=authors_price.nlargest(5, 'price')
top5


# In[48]:


df1 = authors_price.groupby('author_name').agg({'price': 'min'}).rename(columns={'price':'min_price'})
df2 = authors_price.groupby('author_name').agg({'price': 'max'}).rename(columns={'price':'max_price'})
df3 = authors_price.groupby('author_name').agg({'price': 'mean'}).rename(columns={'price':'mean_price'})
authors_stat=pd.concat([df1, df2, df3], axis = 1)
authors_stat


# In[ ]:




