#!/usr/bin/env python
# coding: utf-8

# # Assignment 3

# In[9]:


##Q1. Write a function to return nth term of Fibonacci sequence.

def fibonacci(inp) :
    if inp <= 1 :
        return inp
    else : 
        return (fibonacci(inp-1) + fibonacci(inp-2))
    
n = int(input("Enter a Number : "))

if n < 0 :
    print("Enter any +ve Number ")
else :
    for i in range(n) :
        print(fibonacci(i), end = " ")


# In[7]:


## Q2. Write a function to find out GCD of two numbers using EUCLID'S algorithm.
def gcd(n1, n2) :
    if n2 == 0 :
        return n1
    else :
        return gcd(n2, n1 % n2)
    
inp1 = int(input("Enter 1st_Num : "))
inp2 = int(input("Enter 2nd_Num : "))
print("GCD of given" , inp1 ,"and", inp2 ,"are" ,  gcd(inp1, inp2))


# In[8]:


## Q3.Write a function to find LCM of two number in most optimizers way.
# Using Above GCD Function
def lcm(n1, n2) :
    return (n1 / gcd(n1,n2)) * n2

inp1 = int(input("Enter 1st_Num : "))
inp2 = int(input("Enter second Number : "))
print("LCM of", inp1, "and" , inp2 ,"are" , lcm(inp1, inp2))


# In[ ]:





# In[ ]:




