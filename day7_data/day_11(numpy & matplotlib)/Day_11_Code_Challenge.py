
# Code Challenge 

# Find the mean, median, mode, and range for the following list of values:
# 13, 18, 13, 14, 13, 16, 14, 21, 13


#Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8



"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
import numpy as np

a=np.array([int(x) for x in input("enter the space seperated numbers").split()])
print(a)
a=a.reshape(2,2)

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
from collections import Counter
from scipy import stats

random_list = np.random.randint(5,15,40)

b=stats.mode(random_list)

most_common=Counter(random_list)
print(most_common.most_common(1)[0])

"""

Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)

plt.hist(incomes, bins=50)

mean=np.mean(incomes)
median=np.median(incomes)

incomes=np.append(incomes,100000)

print(np.mean(incomes))

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""
data=np.random.normal(150,20,1000)

plt.hist(data,bins=100)

print(np.var(data))



