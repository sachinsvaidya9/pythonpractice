# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:17:59 2023

@author: Sachin
"""


user_input = str(input("Enter your Name: "))
text = user_input.split()
a = " "
for i in text: 
    a = a+str(i[0]).upper()

print(a)