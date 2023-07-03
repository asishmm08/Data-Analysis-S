#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd 


# In[96]:


df=pd.read_excel(r"C:\Users\asish\Downloads\Data analytis project\Customer Call List.xlsx")


# In[98]:


df


# In[99]:


df=df.drop_duplicates()


# In[100]:


df=df.drop("Not_Useful_Column", axis = 1)
df


# In[ ]:





# In[101]:


df["Last_Name"]=df["Last_Name"].str.strip("..._/")
df


# In[48]:





# In[102]:


df["Phone_Number"]=df["Phone_Number"].str.replace("[^a-zA-Z0-9]","")
df


# In[103]:


df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))


# In[104]:


df["Phone_Number"]=df["Phone_Number"].apply(lambda x: x[0:3]+'-'+x[3:6]+'-'+x[6:10])


# In[58]:


df


# In[105]:


df["Phone_Number"]=df["Phone_Number"].replace('nan--','')
df["Phone_Number"]=df["Phone_Number"].replace('Na--','')


# In[106]:


df


# In[107]:



df[["Sreet","State","Zipcode"]]=df["Address"].str.split(',',2,expand=True)


# In[67]:


df


# In[108]:


df.drop('Address',axis=1)


# In[109]:


df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('No','N')
df


# In[110]:


# df.replace('na','')
# df.replace('NaN','')

df=df.fillna('')
df


# In[111]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)


# In[112]:


df


# In[113]:


for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)


# In[114]:


df


# In[115]:


df = df.reset_index(drop=True)
df


# In[ ]:




