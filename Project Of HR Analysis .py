#!/usr/bin/env python
# coding: utf-8

# # HR_Analysis Using Python:

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


Hr = pd.read_csv("C:/Users/Ranje/OneDrive/Desktop/Excel/HR_Analytics.csv")


# In[3]:


Hr


# In[4]:


Hr.sample


# In[5]:


Hr.shape


# In[6]:


#sample function return the data randomally from the dataSet
Hr.sample()


# In[7]:


Hr.sample(10)


# In[8]:


Hr.head()


# In[9]:


Hr.head(15)


# In[10]:


Hr.head(n=15)


# In[11]:


Hr.tail()


# In[12]:


Hr.tail(n=20)


# In[13]:


#Access The Particular Column using dot(.) Operator and Column Name
Hr.EducationField


# In[14]:


Hr.EducationField.head()


# In[15]:


Hr.EducationField.head(15)


# In[16]:


Hr.EducationField.tail(n=12)


# # Another Way To Access Column Name

# In[17]:


Hr['EducationField']


# In[18]:


Hr['EducationField'].head()


# In[19]:


Hr['EducationField'].tail(15)


# In[20]:


Hr.iloc[0]  #It's represent the zero Number rows of all values with column Name


# In[21]:


# We need a data from index 10 To 20
Hr.iloc[10:20]


# In[22]:


# I need All data of EmpID using loc
Hr.loc[:,'EmpID']


# In[23]:


# I need All data of EmpID using iloc
Hr.iloc[:,0]


# In[24]:


# I need 1st 20 Data of EmpID using iloc
Hr.iloc[:,0].head(20)


# In[25]:


# I need 1st 20 Data of EmpID using loc
Hr.loc[:,'EmpID'].head(20)


# In[26]:


# I need last 15 data from DailyRate using loc
Hr.loc[:,'DailyRate'].tail(15)


# In[27]:


# I need last 15 data from DailyRate using iloc
Hr.iloc[:,5].tail(15)


# In[28]:


# I need b/w 15 To 30 data from DailyRate using iloc
Hr.iloc[15:30]


# In[29]:


# I need b/w 15 To 30 data using iloc
Hr.iloc[15:30].head()


# In[30]:


# I need b/w 15 To 30 data from DailyRate using loc
Hr.loc[15:30,"DailyRate"]


# In[31]:


# I need b/w 15 To 30 data from DailyRate using iloc
Hr.iloc[15:30,5]


# In[32]:


# I need b/w 15 To 30 data from DailyRate using loc and return top 5
Hr.loc[15:30,"DailyRate"].head()


# In[33]:


# I need b/w 15 To 30 data from DailyRate using loc and buttom top 5
Hr.loc[15:30,"DailyRate"].tail()


# In[34]:


Hr


# In[35]:


# Access 'AgeGroup','BusinessTravel', & 'Department' of all HRA using iloc

Hr.iloc[:,[2,4,6]]


# In[36]:


# Access 'AgeGroup','BusinessTravel', & 'Department' of all HRA using iloc B/W 20 To 40

Hr.iloc[20:40,[2,4,6]]


# In[37]:


# Access 'AgeGroup','BusinessTravel', & 'Department' of all HRA using iloc B/W 20 To 40 with Top 5

Hr.iloc[20:40,[2,4,6]].head()


# In[38]:


# Access 'AgeGroup','BusinessTravel', & 'Department' of all HRA using loc

Hr.loc[:,['AgeGroup','BusinessTravel','Department']]


# In[39]:


# Access 'AgeGroup','BusinessTravel', & 'Department' of all HRA using loc with Top 20

Hr.loc[:,['AgeGroup','BusinessTravel','Department']].head(n=20)


# In[40]:


# Access 'AgeGroup','BusinessTravel', & 'Department' of all HRA using loc B/W 20 To 50

Hr.loc[20:50,['AgeGroup','BusinessTravel','Department']]


# In[41]:


# Access 'AgeGroup','BusinessTravel', & 'Department' of all HRA using loc B/W 20 To 50 with buttom 15

Hr.loc[20:50,['AgeGroup','BusinessTravel','Department']].tail(15)


# In[42]:


# Access a particular row using iloc..
Hr.iloc[[15,25,35]]                #it will give us row number 15,25,35 accordly...


# In[43]:


#3:8 --> Represent row & 5:12 --> Represenr Column
Hr.iloc[3:8,5:12]    # it will give us range of row & col..


# In[ ]:





# # Search And Filter Operations

# In[44]:


Hr


# In[45]:


# i want all sale
Hr.Department == 'Sales'


# In[46]:


HD = Hr.Department.loc[Hr.Department == 'Sales']


# In[47]:


HD


# In[48]:


HD = Hr.Department.loc[Hr.Department == 'Sales'].count()


# In[49]:


HD


# In[50]:


HD = Hr.Department.loc[(Hr.Department == 'Sales') | (Hr.EducationField == 'Life Sciences')]
HD


# In[51]:


HD = Hr.Department.loc[(Hr.Department == 'Sales') | (Hr.EducationField == 'Life Sciences')].count()
HD


# In[52]:


HD = Hr.Department.loc[(Hr.Department == 'Sales') & (Hr.EducationField == 'Life Sciences')]
HD


# In[53]:


HD = Hr.Department.loc[(Hr.Department == 'Sales') & (Hr.EducationField == 'Life Sciences')].count()
HD


# In[54]:


H_Age = Hr.loc[Hr.AgeGroup <='40']
H_Age


# In[55]:


H_Age = Hr.loc[Hr.AgeGroup <= '40'].isnull()


# In[56]:


H_Age


# In[57]:


H_Age = Hr.loc[Hr.AgeGroup <= '40'].isnull().count()


# In[58]:


H_Age


# In[59]:


# I need all record 'AgeGroup' <=40 And Department Sales should have 
H_Age = Hr.loc[(Hr.AgeGroup <= '40') & (Hr.Department == "Sales")]
H_Age


# In[60]:


# i need Top 20 it's have
H_Age = Hr.loc[(Hr.AgeGroup <= '40') & (Hr.Department == 'Sales')].head(20)
H_Age


# In[61]:


# i need Top 20 it's have
H_Age = Hr.loc[(Hr.AgeGroup <= '30') & (Hr.Department == 'Research & Development')].head(20)
H_Age


# In[62]:


H_Age = Hr.loc[(Hr.AgeGroup <= '30') & (Hr.Department == 'Research & Development')].count()
H_Age


# In[63]:


H_Age = Hr.loc[(Hr.Department.isin(['Research & Development','Sales'])) & (Hr.AgeGroup <= '30')]
H_Age


# In[64]:


# i need 'Life Sciences','Medical' & 'Marketing' with Deparment 'Sales'

Hm = Hr.loc[(Hr.EducationField.isin(['Life Sciences','Medica','Marketing'])) & (Hr.Department == 'Sales')]
Hm


# In[65]:


# i need 'Life Sciences','Medical' & 'Marketing' with Deparment 'Sales'

Hm = Hr.loc[(Hr.EducationField.isin(['Life Sciences','Medica','Marketing'])) & (Hr.Department == 'Sales')]
Hm


# In[66]:


# i need 'Life Sciences','Medical' & 'Marketing' with Deparment 'Sales' with top 20

Hm = Hr.loc[(Hr.EducationField.isin(['Life Sciences','Medica','Marketing'])) & (Hr.Department == 'Sales')].head(20)
Hm


# In[67]:


# i need 'Life Sciences','Medical' & 'Marketing' with Deparment 'Sales' with top 20

Hm = Hr.loc[(Hr.EducationField.isin(['Life Sciences','Medica','Marketing'])) & (Hr.Department == 'Sales')].isnull()
Hm


# In[ ]:





# In[68]:


# i need 'Life Sciences','Medical' & 'Marketing' with Deparment 'Sales' Or DistanceFromHome <=5

Hm = Hr.loc[(Hr.EducationField.isin(['Life Sciences','Medica','Marketing'])) & (Hr.Department == 'Sales') | (Hr.DistanceFromHome <= 5)]
Hm


# In[69]:


# i need 'Life Sciences','Medical' & 'Marketing' with Deparment 'Sales' Or DistanceFromHome <=5

Hm = Hr.loc[(Hr.EducationField.isin(['Life Sciences','Medica','Marketing'])) & (Hr.Department == 'Sales') | (Hr.DistanceFromHome <= 5)].head()
Hm


# # Handling Missing Values:

# In[70]:


Hr.dtypes


# In[71]:


H = Hr.OverTime.unique()
H


# In[72]:


HAG = Hr.AgeGroup.unique()
HAG


# In[73]:


HAG = Hr.AgeGroup.unique()
HAG


# In[74]:


H_yearSWith = Hr.astype({'YearsWithCurrManager':object})
H_yearSWith


# In[75]:


Hr.dtypes


# In[76]:


Hr


# In[ ]:





# In[77]:


import matplotlib.pyplot as plt


# In[78]:


plt.figure(figsize=(30, 10))       #Adjust width and height as needed
plt.bar(Hr['AgeGroup'],Hr['Department'],color = 'green',edgecolor="r")
plt.gca().set_facecolor('#000000')
plt.title('AgeGroup V/S Department',fontsize=30,fontweight='bold')
plt.xlabel('AgeGroup',fontsize=24)
plt.ylabel('Department',fontsize=24)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


# In[79]:


plt.figure(figsize=(30, 10))       #Adjust width and height as needed
plt.bar(Hr['Age'],Hr['EducationField'],color='b',edgecolor="greenyellow")
plt.gca().set_facecolor('#000000')
plt.title('Age V/S EducationField',fontsize=30,fontweight='bold')
plt.xlabel('Age',fontsize=24)
plt.ylabel('EducationField',fontsize = 24)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()


# In[ ]:





# In[80]:


plt.figure(figsize=(30, 10)) 
plt.plot(Hr['Age'],Hr['BusinessTravel'],color = 'r',marker = '*')
plt.gca().set_facecolor('#000000')
plt.title('Age V/S BusinessTravel',fontsize = 30,fontweight='bold')
plt.xlabel('Age',fontsize = 18)
plt.ylabel('BusinessTravel',fontsize = 18)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()


# In[81]:


plt.figure(figsize=(30, 10)) 
plt.plot(Hr['Age'],Hr['BusinessTravel'],color = 'g',marker = '*')
plt.gca().set_facecolor('#000000')
plt.plot(Hr['Age'],Hr['EducationField'],color = 'b',marker = '>')
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.show()


# In[82]:


plt.figure(figsize=(10, 20)) 
plt.scatter(Hr['AgeGroup'],Hr['DailyRate'],color = 'c',marker = '*')
plt.gca().set_facecolor('#000000')
plt.title('AgeGroup V/S DailyRate',fontsize = 30,fontweight = 'bold')
plt.xlabel('AgeGroup',fontsize = 18)
plt.ylabel('DailyRate',fontsize = 18)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()


# In[83]:


plt.figure(figsize=(10, 20)) 
plt.scatter(Hr['AgeGroup'],Hr['DailyRate'],color = 'c',marker = '*',cmap = 'hot')
plt.colorbar()
plt.gca().set_facecolor('#000000')
plt.title('AgeGroup V/S DailyRate',fontsize = 30,fontweight = 'bold')
plt.xlabel('AgeGroup',fontsize = 18)
plt.ylabel('DailyRate',fontsize = 18)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()


# In[84]:


plt.figure(figsize=(30, 10))
plt.stem(Hr['DistanceFromHome'])
plt.gca(). set_facecolor('#000000')
plt.title('DistanceFromHome',fontsize=30,fontweight='bold')
plt.xlabel('Candidate',fontsize = 18)
plt.ylabel('Years',fontsize = 18)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.show()


# In[85]:


plt.figure(figsize=(30, 10))
plt.stem(Hr['TotalWorkingYears'],linefmt = 'c')
plt.gca(). set_facecolor('#000000')
plt.title('TotalWorkingYears',fontsize=30,fontweight='bold')
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.show()


# In[86]:


plt.figure(figsize=(30, 10))
plt.stem(Hr['YearsWithCurrManager'],markerfmt = "D",linefmt = 'r')
plt.gca(). set_facecolor('#000000')
plt.title('YearsWithCurrManager',fontsize=30,fontweight='bold')
plt.xlabel('Managers',fontsize = 18)
plt.ylabel('Years',fontsize = 18)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.show()


# In[87]:


plt.figure(figsize=(30, 10))
plt.stem(Hr['YearsInCurrentRole'],markerfmt = "D",linefmt = 'b')
plt.gca(). set_facecolor('#000000')
plt.title('YearsInCurrentRole',fontsize=30,fontweight='bold')
plt.xlabel('Candidate',fontsize = 18)
plt.ylabel('Years',fontsize = 18)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.show()


# In[ ]:





# #                                      #THANK YOU

# In[ ]:





# In[ ]:





# In[ ]:




