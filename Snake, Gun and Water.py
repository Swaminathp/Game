#!/usr/bin/env python
# coding: utf-8

# In[2]:


#game project, done in jupyter notebook:
import random
listy = ['w','s','g'] 

you = input("Enter your object:\n") 
    
def game(comp, you):
     
    if you not in listy:
        print('Enter a valid object')
    else:
        if comp==you:
            print('Computer chose', comp, ',you chose', you, ',The game is tie!')
        elif comp == 'w':
            if you == 'g':
                print('Computer chose', comp, ',you chose', you, '. You lost!')
            else:
                print('Computer chose', comp, ',you chose', you, '. You won!')
        elif comp == 's':
            if you == 'w':
                print('Computer chose', comp, ',you chose', you, '. You lost!')
            else:
                print('Computer chose', comp, ',you chose', you, '. You won!')
        elif comp == 'g':
            if you == 's':
                print('Computer chose', comp, ',you chose', you, '. You lost!')
            else:
                print('Computer chose', comp, ',you chose', you, '. You won!')
    
randnum = random.randint(1,3)
    
if randnum == 1:
    comp = 's'
elif randnum ==2:
    comp = 'w'
else:
    comp = 'g'
    
game(comp,you)


# In[ ]:





# In[11]:





# In[ ]:




