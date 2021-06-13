#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# In[1]:


## Q1. Write a lambda expression to extract first word of a string
first_word= lambda a:a.split()[0]
first_word("I’m not superstitious, but I am a little stitious.")


# In[2]:


##Q2. Write a function to extract first word of s string (with many words separated by space)
def first_word(s):
    return s.split()[0]
first_word("I’m not superstitious, but I am a little stitious.")


# In[3]:


## Q3. Extract the first word from every string from list of strings by using map function.

strings = ["Hear about the new restaurant called Karma?",
           "There’s no menu: You get what you deserve.",
           "What did the left eye say to the right eye?",
           "Between you and me, something smells."]
def function1(strings):
    return strings.split()[0]

result= map(function1, strings)

print(list(result))


# In[4]:


## Q4. write a function to return a list of prime factors of a given number.
num = int(input("Enter number: "))

def prime_factors(number):
    l=[]
    for i in range(2,(number+1)):
        if(number%i==0):
            flag = 1
            for j in range(2, (i//2+1)):
                if(i%j==0):
                    flag=0
                    break
                
            if(flag == 1):
                l.append(i)
    print(l)
prime_factors(num)


# In[6]:


## Q5.Write a function that finds 2nd largest among 4 numbers (repetitions are allowed , without sorting)
def secondlargest(n):
    first_num =set(n)
    first_num.remove(max(first_num))
    print(max(first_num))
n= [int(i)for i in input("Enter 4 numbers :").split()]
secondlargest(n)


# In[ ]:




