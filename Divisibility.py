# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:37:39 2023

@author: Sachin
"""
# Divisibility by 3

num = input("Enter a number to check the divisibility by 3: ")

num = str(num)

n = 0

for digit in num:
    int_digit = int(num)
    n += int_digit
if n % 3 == 0:
    print("The given number is divisible by 3.")
else:
    print("The given number is not divisible by 3.")

################################################################

# Divisibility by 5

n = input("Enter a number to check the divisibility by 5: ")

if n[-1] == '0' or n[-1] == '5':
    print("The given number is divisible by 5.")
else:
    print("The given number is not divisible by 5.")
    
#################################################################


