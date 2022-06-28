# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 19:10:30 2022

@author: khara
"""

# using funtion count odd and even from a list 

def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1 
        else:
            odd+=1
    return even,odd


list=[20,11,24,45,111,556,57,24,11,9]

even,odd=count(list)

print(even,odd)