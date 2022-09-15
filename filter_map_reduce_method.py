# -*- coding: utf-8 -*-
## filter, map , reduce() methords


x=[2,4,6,8,9,7,6,5,4,3]

#using filter( ) method

even_number=list(filter(lambda n:n%2==0,x)) #filter(funtion,list) use for filtretion
print(even_number)

#using map() method
doubles=list(map(lambda n:n*2,x)) #use for oprations 
print(doubles)


#using reduce() method

from functools import reduce

sum=reduce(lambda a,b:a+b,doubles) # using reduce we add all numbers
print(sum)