#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np  
import pandas as pd

nodes = pd.read_csv("nodes.csv",  usecols = ["CD_MemberList", "shared name"])
df_node=pd.DataFrame(nodes)

#MemberList= nodes["CD_MemberList"].tolist();
#print(MemberList)


# new df from the column of lists
#split_Members = pd.DataFrame(nodes["CD_MemberList"].tolist())
# display the resulting df
#split_Members

df_node.columns=["name","id"]
df_node


# In[2]:


data = df_node.assign(name=df_node.name.str.split(" ")).explode("name")
#data = df_node.explode('name')
data['name']=data['name'].astype(int)
data


# In[3]:


nodesId = pd.read_csv("default-node.csv",  usecols = ['label', 'name'])
#nodesId
labels = pd.DataFrame(nodesId)
labels['name']=labels['name'].astype(int)
labels


# In[4]:


#data.set_index('name', inplace=True)
#labels.set_index('name', inplace=True)
#df_merged = data.join(labels, how='cross', on='name')

#print(df_merged)
df_merged = data.merge(labels, on='name', how='left')
pd.set_option("display.max_rows", None)
print(df_merged)


# In[ ]:





# In[ ]:




