
# coding: utf-8

# In[1]:


# Import Required Packages 
import pandas as pd
import numpy as np
import pandas_profiling
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import sklearn 
from sklearn.model_selection import train_test_split
from sklearn import metrics


# In[2]:


#Approach by uploading the fiel to jupyter using read_csv
data = pd.read_csv(r"HR_comma_sep.csv")


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


data_cat = data.select_dtypes('object')


# In[6]:


data_cat


# In[7]:


# dummification by encoding 
from  sklearn.preprocessing import LabelEncoder
encoding_list = ['department','salary']
data[encoding_list] = data[encoding_list].apply(LabelEncoder().fit_transform)


# In[8]:


data


# In[9]:



# Approach 2
Y= data["left"]
X = data.drop(['left'], axis=1)


# In[10]:


# Train and test split

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=62, stratify=Y)
x_train.shape
x_test.shape
y_train.shape
y_test.shape


# In[11]:



from sklearn.ensemble import RandomForestRegressor
forest = RandomForestRegressor(max_depth = 10, n_estimators = 100, random_state = 1)


# In[14]:


forest.fit(X, Y)


# In[21]:



import pickle
pickle.dump(forest, open('HR_model.pkl', 'wb'))

