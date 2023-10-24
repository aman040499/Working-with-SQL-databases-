#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3


# In[3]:


con = sqlite3.connect("chinook.db")


# In[4]:


cur = con.cursor()


# In[5]:


for row in cur.execute('SELECT * FROM Census_Data;'):
    print(row)


# In[6]:


con.close()


# In[7]:


import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("chinook.db")

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM Census_Data;'):
    print(row)
  

# Be sure to close the connection
con.close()


# In[8]:


con = sqlite3.connect("chinook.db")
cur = con.cursor()
cur.execute('''
          INSERT INTO Census_Data (COMMUNITY_AREA_NUMBER,COMMUNITY_AREA_NAME )
          VALUES
                (78, 'Lakeshore')               
          ''')

for row in cur.execute('SELECT * FROM Census_Data;'):
    print(row)

# Be sure to close the connection
con.close()


# In[10]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///chinook.db')


# In[13]:


get_ipython().system('pip install sqlalchemy==1.3.9')
get_ipython().system('pip install ibm_db_sa')
get_ipython().system('pip install ipython-sql')


# In[16]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///chinook.db')


# In[21]:


get_ipython().run_cell_magic('sql', '', "SELECT\n    name\nFROM\n    sqlite_master\nWHERE\n    type='table'\n")


# In[19]:


get_ipython().run_line_magic('sql', 'select * from chicago_crime_data')


# In[20]:


get_ipython().run_cell_magic('sql', '', "\nCREATE TABLE Fam(Name TEXT, Age INTEGER, Profession TEXT, Major TEXT);\nINSERT INTO Fam (Name, Age) VALUES('Pam', 50);\nINSERT INTO Fam (Name, Age) VALUES('Miranda', 32);\nINSERT INTO Fam (Name, Age) VALUES('Pascal', 45);\nINSERT INTO Fam (Name, Age) VALUES('Dave', 12);\nINSERT INTO Fam (Name, Age) VALUES('Emmy', 23);\n\nUPDATE Fam SET Profession='Unknown' WHERE Profession ISNULL\n")


# In[22]:


get_ipython().run_line_magic('sql', 'select*from fam')


# In[ ]:





# In[ ]:





# In[ ]:





# In[33]:


import pandas as pd
result = get_ipython().run_line_magic('sql', 'select * from movies')
dataframe = result.DataFrame()
dataframe


# In[ ]:




