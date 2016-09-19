"""
Name: Domonkos Nagykaldi
Email: dmnagykaldi@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""

#A:
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: [1, 5, 4, 2, 3]

a[4] = a[2] + a[-2]
Print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: [5]

print(4 in a)
# Prints: [2]

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]

#B:
def remove_all(el, lst):
"""Removes all instances of el from lst. 
Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
Usage: remove_all(1, x)
Would result in: [3, 2, 5, 7]
"""
   for i in range(len(lst))
    if(lst[i] == el)
        lst.remove(el)

#C:
def add_this_many(x, y, lst):
""" Adds y to the end of lst the number of times x occurs in lst. 
Given: lst = [1, 2, 4, 2, 1]
Usage: add_this_many(1, 5, lst)
Results in: [1, 2, 4, 2, 1, 5, 5]
"""
    total = 0
    for i in range(len(lst))
        if(lst[i] == x)
            total++
    for i in range(total)
        lst.append(y)

#D:
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: [2]

print(a[1:-2])
# Prints: [1]

print(a[::-1])
# Prints: [3, 1, 4, 2, 5, 3]

#E:
def reverse(lst):
""" Reverses lst in place. 
Given: x = [3, 2, 4, 5, 1] 
Usage: reverse(x)
Results: [1, 5, 4, 2, 3]
""""
    for i in range(len(lst))
        lst.insert(len(lst),lst[i])