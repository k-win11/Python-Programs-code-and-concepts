# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 07:24:16 2022

@author: khara
"""
#Add extra perametrs

class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    
    
p2=Phone()

p2.set_color('Red')
p2.set_cost('5000')

p2.show_color()

p2.show_cost()
    
