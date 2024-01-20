#!/usr/bin/env python
# coding: utf-8

# ### Addition of Numbers :

# In[7]:


num1 = input('Enter 1st number :')
num2 = input('Enter 2nd number :')
num1 = float(num1)
num2 = float(num2)
result = num1 + num2
print(f'sum of no :{num1:0.2f} + {num2:0.2f} is {result:0.2f}')


# ### Multipication of Numbers :

# In[ ]:


num1 = input('Enter 1st number :')
num2 = input('Enter 2nd number :')
num1 = float(num1)
num2 = float(num2)
result = num1*num2
print(f'Multipication of {num1:.2f} and {num2:.2f} is {result:.2f}')


# #### Temperature conversion formula :
# ![Screenshot%202023-10-20%20153447.png](attachment:Screenshot%202023-10-20%20153447.png)

# In[ ]:


celsius = float(input('Enter Temperature in celsius :'))
fahrenheit = 1.8 *celsius + 32
kelvin = 273.15 + celsius
print(f'{celsius:.2f} celsius = {fahrenheit:.2f} fahrenheit')
print(f'{celsius:.2f} celsius = {kelvin:.2f} kelvin')


# ### Rectangle Area and perimeter :
# - Area = l*b
# - perimeter = 2(l+b)

# In[ ]:


l = float(input('Enter Length of a Rectangle :'))
b = float(input('Enter Breath of a Rectangle :'))
area = l*b
perimeter = 2*(l + b)
print(f'Area = {area : .2f}')
print(f'Perimeter = {perimeter : .2f}')


# ### Triangle area  :
# - Area = 1/2 * Base * Height

# In[5]:


b = float(input('Enter the base of a triangle :'))
h = float(input('Enter the height of a triangle :'))
area = 1/2 *b*h
print(f'Area = {area : .2f}')


# ### Check if a Number is Even or Odd:

# In[10]:


def check_even_odd(num):
    if num % 2 == 0 :
        return "even"
    else:
        return "odd"


# In[11]:


check_even_odd(22)


# In[12]:


def even_odd(n):
    if n % 2 == 0:
        print('The number is EVEN!')
    else:
        print('The number is ODD!')


# In[13]:


even_odd(17)


# ### Find the Factorial of a Number:

# In[24]:


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
no = int(input("Enter a number"))
result = factorial(no)
print(f'The Factorial of {no} is {result}')


# In[23]:


factorial(5)


# In[25]:


factorial(7)


# ### Check if a Number is Prime:

# In[30]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
no = int(input('Enter a Positive number :'))
result = is_prime(no)
print(f"The number {no} is {'prime' if result else 'not prime'}")


# In[28]:


is_prime(4)


# In[29]:


is_prime(2)


# ### Generate Fibonacci Series:

# In[31]:


def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
result = fibonacci(num_terms)
print(f"The Fibonacci series is: {result}")


# In[32]:


fibonacci(3)


# In[33]:


fibonacci(5)


# In[ ]:




