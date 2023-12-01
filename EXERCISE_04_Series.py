#!/usr/bin/env python
# coding: utf-8

# # Series Basics Exercise
# 
# **Work with the `bestsellers.csv` dataset to answer the following questions:**

# ## Part 1
# * Retrieve a series that contains the book Names
# * Retrieve a series that contains the User Ratings
# * Retrieve the first 8 Authors

# In[1]:


import pandas as pd
bestsellers = pd.read_csv("../pandas_csv/bestsellers.csv")
bestsellers.head()


# In[2]:


#Retrieve a series that contains the book Names
bestsellers.Name


# In[3]:


#Retrieve a series that contains the User Ratings
bestsellers["User Rating"]


# In[4]:


#Retrieve the first 8 Authors
bestsellers["Author"].head(8)


# ## Part 2
# * Find the unique Genres
# * Find the number of unique Authors
# * Find the average Price
# * Find the 10 highest prices

# In[5]:


#Find the unique Genres
bestsellers["Genre"].unique()


# In[6]:


#Find the number of unique Authors
bestsellers["Genre"].nunique()


# In[7]:


#Find the average Price
bestsellers["Price"].mean()


# In[8]:


#Find the 10 highest prices
bestsellers.nlargest(10,"Price")


# In[9]:


bestsellers["Price"].nlargest(10)


# ## Part 3
# * Find the top 3 most common book titles in the dataset
# * Create a new dataframe with only Author and User Rating.
# * Using the new dataframe, find the most common combination of Author and User Rating Score.

# In[10]:


##Find the top 3 most common book titles in the dataset
most_common =bestsellers["Name"].value_counts().head(3)


# In[11]:


most_common


# In[12]:


#Create a new dataframe with only Author and User Rating.
new_df = bestsellers[["Author","User Rating"]]
new_df.head()


# In[13]:


#Using the new dataframe, find the most common combination of Author and User Rating Score.
new_df[["Author","User Rating"]].value_counts()


# In[18]:


new_df[["Author","User Rating"]].mode()#find the most common combination of Author and User Rating


# ## Part 4
# * Create a pie chart showing the total number of times each Genre appears in the dataset.
# * Find out the top 10 most prolific authors and plot their number of books as a bar plot
# * BONUS: create a histogram showing the distribution of User Rating scores

# In[14]:


#Create a pie chart showing the total number of times each Genre appears in the dataset.

bestsellers["Genre"].value_counts().plot(kind="pie")


# In[15]:


#Find out the top 10 most prolific authors, and plot their number of books as a bar plot

prolific_authors = new_df["Author"].value_counts().head(10).plot(kind="bar")


# In[16]:


#BONUS: create a histogram showing the distribution of User Rating scores
user_rating = new_df["User Rating"].value_counts().plot(kind="hist")


# In[17]:


user_rating = new_df["User Rating"].value_counts().plot(kind="line")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




