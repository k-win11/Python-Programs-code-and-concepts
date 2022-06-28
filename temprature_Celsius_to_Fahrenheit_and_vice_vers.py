# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:45:35 2022

@author: khara
"""

print('Calculate the temprature Celsius to Fahrenheit and vice versa and Use "f" for Celsius to Fahrenheit and "c"  Fahrenhei to Celsiu')

use_sign=(input("Select (f) or (c):",     ))


temp=int(input("Enter the temprature:", ))
F='fahrebheit'
C='celsius'
if use_sign=='f':
    
    temp1=temp * (9.0/5.0) + 32.0
    
    print('temprature in fahrenheit:', temp1)
    
elif use_sign=='c':
    
    temp2=temp - 32.0 * (5.0/9.0)
    
    print('temprature in celsius:', temp2)
    
else:
    print("Needs to be (f) or (c)!")
   
    
    
    
       
    


      
