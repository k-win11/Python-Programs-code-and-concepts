# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:32:36 2022

@author: 91798
"""
rohit_total_expence=[10,30,50,70,40]
rahul_total_expence=[27,59,30,20]

def total_moth_expence(exp):
    total=0
    for itmes in exp:
        total+=itmes
    return total


rohit_expence=total_moth_expence(rohit_total_expence)
print(rohit_expence)
rahul_expence=total_moth_expence(rahul_total_expence)
print('rahul total monthly expence',rahul_expence)