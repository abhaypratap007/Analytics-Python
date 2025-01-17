# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:05:58 2021

@author: Singh
"""
#-----------------Apply Family of Functions--------------------------------
#To apply our own functions to dataset, pandas provides three functions from
#apply family of functons: pipe(), apply(), applymap()

# pipe():Table wise Function Application.
# It performs the custom operation for the entire dataframe.
import pandas as pd
# own function
def adder(adder1,adder2):return adder1+adder2

#Create a Dictionary of series
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
     'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}

print(type(d))
print(d)
df = pd.DataFrame(d)
print (df)
print (df.pipe(adder,2))

# apply():Row or Column Wise Function Application.
# It performs the custom operation for either row wise or column wise.
import numpy as np
#Create a DataFrame
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
     'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}

df = pd.DataFrame(d)
print (df)
#Row Wise Fxn Application:
#row wise mean
print (df.apply(np.mean,axis=1))

#Column Wise Fxn Application:
#column wise mean
print (df.apply(np.mean,axis=0))

# applymap():Element wise Function Application.

# applymap():Element wise Function Application.
# It performs specified operation on all the elements of the dataframe. 

#Create a DataFrame
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
     'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}

df = pd.DataFrame(d)
print (df)

#Example 1:
print (df.applymap(lambda x:x*2))
#Example2:
import math as m
print (df.applymap(lambda x:m.sqrt(x)))

#Ex-1. check odd or even no.
num = int(input("Enter a number: "))

if num % 2 == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
#Ex-2. ------------   
def evenoddfun(num):
    if num%2==0:
        print(num,'no is even')
    else:
        print(num,'no is odd')
evenoddfun(21)
#Ex-3. -------------------------
input_list = [14, 18, 31, 11, 13, 87, 103,
              27, 64, 96, 22, 48, 17, 15, 11, 28, 47]

new_even_list = [m for m in input_list if m % 2 == 0]
new_odd_List  = [m for m in input_list if m % 2 != 0]

print("Even numbers are available in list are :")
print(new_even_list)
print("Odd numbers are available in list are :")
print(new_odd_List)
