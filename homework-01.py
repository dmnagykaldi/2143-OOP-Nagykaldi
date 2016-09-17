"""
Name: Domonkos Nagykaldi
Email: dmnagykaldi@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""

#A:
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1, 5, 4, 2, 3

a[4] = a[2] + a[-2]
Print(a)
# Prints: 1, 5, 4, 2, 6

print(len(a))
# Prints: 5

print(4 in a)
# Prints: 2

a[1] = [a[1], a[0]]
print(a)
# Prints: 1, [5, 1], 4, 2, 6