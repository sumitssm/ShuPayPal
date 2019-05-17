#!/usr/bin/env python
# coding: utf-8

# In[8]:


print ("Login Script by Usman Khan")

CorrectUsername = "Usman"
CorrectPassword = "UsmanKhan"

loop = 'true'
while (loop == 'true'):
    username = input("Please enter your username: ")
    if (username == CorrectUsername):
        password = input("Please enter your password: ")
        if (password == CorrectPassword):
            print ("Logged in successfully as " + username)
            loop = 'false'
        else:
            print ("Password incorrect!")
    else:
        print ("Username incorrect!")


# In[ ]:
