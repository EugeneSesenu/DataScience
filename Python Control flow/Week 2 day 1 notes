#!/usr/bin/env python
# coding: utf-8

# # Control flow

# == ---> is a boolean condition
# 

# In[2]:


a, b = 0, 1
amax = 100
L = []
while True:
    (a,b) = (b, a + b)
    if a > amax:
        break 
        L.append(a)
print(L)


# In[5]:


def double(x):
    return x * 2


# In[6]:


double(2)


# In[ ]:


x=input("Give an integer: ")
x=int(x)
if x >= 0:
    a=x


# In[ ]:


def f():            # outer function
    b=2
    def g():        # inner function
        # nonlocal b # Without this nonlocal statement,
        b=3         # this will create a new local variable
        print(b)
    g()
    print(b)
f()


# In[ ]:


def length(*t, degree == 2 ):
    s = 0 
    for x in t:
        s + = abs(x)** degree
    return s ** (1/degree )
print(length (-4, 5))
print(length (-4, 3), degree = 3)


# In[ ]:


length()


# * Global variable  are readable in a local scope

# * A function is a code of block which only runs when it is called.
# 

# * sort() ---> sort array automatically goes from ascending order to descending order

# *  ^(*t) tuple displays a padded tuple used in parameters of function

# In[ ]:




