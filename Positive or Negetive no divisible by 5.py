# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 09:28:27 2023

@author: Sachin
"""

# Create an input variable: “number”

number = input("Enter a number: ")

# Convert the input variable from string to integer

number = int(number)

# Use ‘elif’ loop to check whether the given number is positive and divisible by 5 or not.

if number + abs(number) == 0 and number%5 == 0:
        		print("the given number is negative & divisible by 5")
elif number + abs(number) == 0 and number%5 != 0:
        		print("the given number is negative & not divisible by 5")
elif number + abs(number) != 0 and number%5 == 0:
            	print("the given number is positive & divisible by 5")
else:
        		print("the given number is positive & not divisible by 5")

