'''
Exercise: 

Write a program to accept a string from the user and display characters 
that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

Expected Output:

Orginal String is  pynative
Printing only even index chars
p
n
t
v
'''
str = input("Pls write your string here: ")

str1 =str[::2]

print(str1)

str_len = len(str)

char = (str[:str_len-1:2])

for i in char:
    print(i)
            
print(f"Original string is {str}")

print("printing only even index chars")

word = list(str)

word_char = [i for i in word[::2]]

for char in word_char:
    print(char)
