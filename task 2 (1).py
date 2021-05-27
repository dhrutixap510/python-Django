#!/usr/bin/env python
# coding: utf-8

# # Task 2

# comments,variable and datatypes

# In[1]:


print("Hello friends")
'''multiline comment
is written like this.
'''


# In[2]:


#variables in python


# In[3]:


a=5
b=20.7
c='Dhrutixa'
print(a)
print("value of b is:",b)
print("my name is:",c)


# In[4]:


#assigning multiple values
a,b,c=5,20.5,'Dhrutixa'
print(a)
print("value of b is:",b)
print("my name is:",c)


# In[6]:


#assigning same value to multiple variables:
a=b=c=5
print(a)
print("value of b is:",b)
print("my name is:",c)


# In[ ]:


#data types in python


# In[7]:


#number datatype
a1=10
print(a1,"is of type",type(a1))


# In[8]:


a1=10
print(a1,"is int?",isinstance(10,int))


# In[9]:


#string datatype
name="patel dhrutixa"

print(name)
print(name[0])
print(name[2:6])
print(name[:5])
print(name[2:])
print(name*2)


# In[10]:


#list datatype
list1=[10,4.5,'dhrutixa']
print(list1)
print(list1[2])


# In[11]:


#tuple datatype
#tuples are immutable
tuple1=(10,30,56.3,"dhrutixa",'patel')
print(tuple1)


# In[13]:


#dictionary
d={1:10,2:'dhrutixa',8:"happy",a:'world'}
print(d[1])
print(d[a])


# In[ ]:




