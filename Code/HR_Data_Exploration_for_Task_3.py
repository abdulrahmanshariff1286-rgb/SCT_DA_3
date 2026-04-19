#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas matplotlib seaborn')


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\Abdul Rahman\OneDrive\Desktop\SkillCraft Technology\Task 3\HR_Attrition.csv')


# In[5]:


# Count 'Yes' and 'No' in the Attrition column
attrition_counts = df['Attrition'].value_counts()

# Calculate the percentage (Total 'Yes' / Total Rows * 100)
attrition_rate = attrition_counts['Yes'] / len(df) * 100
print(f"Overall Attrition Rate: {attrition_rate:.2f}%")


# In[6]:


# Calculate Department Attrition
dept_attrition = df.groupby('Department')['Attrition'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
# Rename the columns for clarity
dept_attrition.columns = ['Department', 'Attrition Rate (%)']

# Do the exact same thing for Job Role, and sort it from highest to lowest
role_attrition = df.groupby('JobRole')['Attrition'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
role_attrition.columns = ['JobRole', 'Attrition Rate (%)']
role_attrition = role_attrition.sort_values(by='Attrition Rate (%)', ascending=False)


# In[7]:


# Save to CSV files, without the row index numbers
dept_attrition.to_csv('attrition_by_department.csv', index=False)
role_attrition.to_csv('attrition_by_role.csv', index=False)


# In[9]:


plt.figure(figsize=(8, 5)) # Set the size of the canvas
# Draw a bar chart using the department data table
sns.barplot(x='Department', y='Attrition Rate (%)', data=dept_attrition, palette='viridis')
plt.title('Attrition Rate by Department')
plt.savefig('attrition_by_department.png') # Save the image
plt.close() # Clear the canvas


# In[10]:


plt.figure(figsize=(8, 5))
# Draw a boxplot comparing those who stayed ('No') vs left ('Yes') based on Income
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, palette='Set2')
plt.title('Monthly Income vs Attrition')
plt.savefig('income_vs_attrition.png')
plt.close()


# In[ ]:




