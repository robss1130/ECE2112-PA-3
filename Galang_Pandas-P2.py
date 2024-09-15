#!/usr/bin/env python
# coding: utf-8

# In[84]:


#Import the Pandas library
import pandas as pd


# In[90]:


#Load the spreadsheet file
cars = pd.read_csv('cars.csv')


# ## Problem 2: Extract the following information using subsetting, slicing and indexing operations. ##
# ### Then save it into Surname_Pandas-P2.py ##

# ### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars. ###

# In[96]:


#Use iloc to find and print out specific rows/columns and utilize the slicing function
print(cars.iloc[:5, ::2])


# ### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’. ###

# In[203]:


#Use loc to specific and pick the row that contains 'Mazda RX4' in the 'Model' column
mazda = cars.loc[cars['Model'] == 'Mazda RX4']
mazda


# ### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? ###

# In[226]:


#use loc to output the specific row index and the column name
cars.loc [23,'cyl']


# ### d. Determine how many cylinders and what gear type the car models (Mazda RX4 Wag, Ford Pantera L, Honda Civic) has

# In[228]:


cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]


# In[ ]:




