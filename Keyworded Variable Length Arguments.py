# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 18:49:41 2022

@author: kharak.kunwar
"""
# Keyworded Variable Length Arguments
def person(name,*data):
    print(name)
    print(data)
    
    
    
person('ravi','munsyari',3456789012)   


# in proper way 

def person(name,**data):
    print(name)
    print(data)
    
    
    
person('ravi',place='munsyari',phone_number=3456789012) 


# use for loop 

def person(name,**data):
    
    print(name)
    
    for i,j in data.items():
        
        print(i,j)

    
person('ravi',age=28,place='munsyari',phone_number=3456789012) 