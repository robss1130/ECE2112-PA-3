#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: Print the first and last five rows of the resulting cars ##
# ### Then save it into Surname_Pandas-P1.py ##

# In[21]:


#Import the Pandas library
import pandas as pd


# ## I have no idea where to place the spreadhsheet file so I run a code that shows where the directory path is ##

# In[24]:


#os is a library that provides functions that interacts with the operating system
import os


# In[28]:


current_directory = os.getcwd()

#display where the current directory is
print(current_directory)


# In[38]:


# I change the working directory to make things well-ordered
os.chdir('C:\\Users\\PC\\Documents\\Python Codes\\Modules\\Save_files')

print(os.getcwd())


# In[52]:


#Load the spreadsheet file
cars = pd.read_csv('C:\\Users\\PC\\Documents\\Python Codes\\Modules\\Save_files\\cars.csv')


# In[54]:


#Display the first five rows
print(cars.head())


# In[56]:


#Display the last five rows
print(cars.tail())


# In[ ]:




