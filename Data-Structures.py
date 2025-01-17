# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:38:04 2021

@author: Singh
"""
x = 10
print(x)
#where x is a varible entities of a program that hold a value.
#A value(10) is a data type,the Data-type is basically the type od value that
#you assign to the variable.

print("hello world")  
print("hello \nworld")  #print in next line
print("hello \tworld")  #print with tab

name = ''' Hey there, 
Abhay this side !!''' #triple codes using for Spanning strings over multiple lines.
print("name")

#Numbers
#a=3 , b=5  #a and b are number objects 

#String
str1 = 'Hello Students' #string str1
print(str1)
str2 = ' how are you' #string str2  
str2
#slicing in python is a mechanism to select a range of items from sequence
print (str1[0:5]) #printing first five character using slice operator  
(str1[0:5])
print (str1[4]) #printing 5th character of the string  
print (str1*2) #printing the string twice  
print (str1 + str2) #printing the concatenation of str1 and str2

#Lists
l  = [1, "hi", "python", True] 
print (l[3:])  
print (l[0:2])
print (l);  
print (l + l);  
print (l * 3);
print (type(l))
#Lets try mutation 
l[1] = "Bye"
print(l)
#create empty list
emp = []
print(type(emp))
#Tuple
t  = ('hi', 'python', 2, 4) 
t 
#slicing in python is a mechanism to select a range of items from sequence
print (t[1:]);  
print (t[0:2]);  
print (t);  
print (t + t)
print (t * 3)  
print (type(t)) 
#Lets try mutation 
t[1] = "Bye"
print (t)

#mutation
nest = (l,t)
print(nest)

#Dictionary
d = {1:"Jimmy", 2:'Alex', 3:'john', 4:'mike'}
d
print("1st name is "+d[1])  
print("2nd name is "+ d[4]) 
print (d); 
print (d.keys());  
print (d.values());

#----ADVANCED----
#list
#ordered collection of items; sequence of items in a list
shoplist =['apple','carrot','mango', 'banana']
shoplist
len(shoplist)
print(shoplist)

#add item to list
shoplist.append('rice')
shoplist

#sort
shoplist.sort()  #inplace sort
shoplist

#index/select
shoplist[0]
shoplist[0:4]

#delete item
del shoplist[0]
shoplist

#Tuple
#Used to hold multiple object; similar to lists; less functionality than list
#immutable - cannot modify- fast ; ( )
zoo = ('python','lion','elephant','bird')
zoo
len(zoo)
languages = 'c', 'java', 'php'  #better to put (), this also works
languages

#Dictionary - like an addressbook. use of associate keys with values
#key-value pairs { 'key1':value1, 'key2':value2} ; { } bracket, :colon

student = {'A101': 'Abhinav', 'A102': 'Rohit', 'A103':'Rahul', 'A104': 'Karan'}
student
student['A103']
print('Name of rollno A103 is ' +student['A103'])
del student['A104']
student
len(student)

#for rollno, name in student.items():
    #print('name of {} is {} '.format(rollno, name) )

#Lets test Mutation: 
#adding a value
student['A104'] = 'Hitesh'
student

#Set
#Sets are unordered collections of objects; ( [ , ])
teamA = set(['india','england','australia','sri lanka','ireland'])
teamA
teamB = set(['pakistan', 'south africa','bangladesh','ireland'])
teamB

#Checking whether a data value exists in a set or not.
'india' in teamA
'india' in teamB

#Adding values in a set
teamA.add('china')
teamA  #puts in order
teamA.add('india')
teamA  #no duplicates
teamA.remove('australia')
teamA

#Create dataframe :
import pandas as pd
 
#Create a DataFrame
d = {'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
            'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
            'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
                    'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
                    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
                               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
                               'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}

print(d)

df = pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
df

#View a column of the dataframe in pandas:
df['Name']

#View two columns of the dataframe in pandas:
df[['Name','Score','Exam']]

#View first two rows of the dataframe in pandas:
df[0:2]

#slice array
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(matrix)
print(matrix[0:2, 1:3])
