# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 07:35:27 2022

@author: khara
"""

#constructor

class Employee:
    def __init__(self,name,age,salary,gander):
        self.name=name
        self.age=age
        self.salary=salary
        self.gander=gander
        
    def Employee_details(self):
        print('Employee name is',self.name)
        print('Employee age is',self.age)
        print('Employee salary is',self.salary)
        print('Employee gander is',self.gander)
    
e1=Employee('kharak.kunwar',28,30000,'male')
e1.Employee_details()