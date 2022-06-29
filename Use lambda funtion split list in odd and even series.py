# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:42:11 2022

@author: kharak.kunware


"""
#Use lambda funtion split list in odd and even series 


number=[10,22,12,34,35,6,7,7,8,87,9,564,325,34,21,34,]

event=list(filter(lambda n:n%2==0, number))

print('no is even',event)

event=list(filter(lambda n:n%2!=0,number))

print('odd numbers:', event)