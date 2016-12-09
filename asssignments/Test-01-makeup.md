# Domonkos Nagykaldi

## 1: Definitions: 

Using python comments, label all lines that an OOP definition could be applied to.

```python

class Employee:

   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)

emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount

```
-----

### Answer 1

```python
# place answer here
# use this as a template for your other answers
# Class declaration
class Employee:

   empCount = 0
   # Constructor
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   # Member function
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
   # Member function
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

# Class instance
emp1 = Employee("Zara", 2000)
# Class instance
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount



```

-----

## 2: List Functions

Given the list below:

```python
States = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 'New Hampshire', 'Maine', 'Texas']
```

**A)** Sort the list

**B)** Add 'Oklahoma' to the list in alphabetical order without sorting the list again. Actually, write a function that would add an item to the list in alphabetical order. Example:

```python 
def addInOrder(L):
    #add to the list L in the proper order


    #return your ordered list
    return L
```
### Answer 2

```python
# place answer here
# use this as a template for your other answers
States.sort()
def addInOrder(L,item=None):
    #add to the list L in the proper order
    i=0
    while(i < len(L)):
       if(States[i+1] < item):
          i = i+1
    L.insert(i,item)

    #return your ordered list
    return L



```

-----

## 3: Looping over Lists
(10 Points)

Using the following list as an example: `L = [10,20,30,40,50,60,70,80,90,100]` write a function that would divide each value by its index location + 1. Our example list would turn into: `L = [10,10,10,10,10,10,10,10,10,10]`. Remember NOT to get caught up on these values. Your function should work on any list.

Usage:
```python
L =  [10,20,30,40,50,60,70,80,90,100]
NList = addPrevious(L)
print(NList)
# prints: [10,10,10,10,10,10,10,10,10,10]
```

Your answer should consist of just the function definition and none of the usage I provided above.
### Answer 3

```python
# place answer here
# use this as a template for your other answers
def divPrevious(L):
   for i in range(len(L)):
      L[i] = L[i]/(i+1)



```

-----

## 4: Looping over Dictionaries
(10 Points)

Given the following dictionary: 
```python
months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : "May", 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" }
```
Iterate over this dictionary, and create a new one that only uses the first three letters of the month. Also make the new months all lowercase. Your new dictionary should look like:

```
abbr_months = {1:"jan",
        2 :"feb",
        3 :"mar",
        4 : "apr", 
     	5 : "may", 
     	6 : "jun", 
    	7 : "jul",
        8 : "aug",
     	9 : "sep", 
    	10 : "oct", 
        11 : "nov",
        12 : "dec" }
```

To help you look up `string slicing` and `lower`. 

Your answer should include just the code that loops and creates the new dictionary.
### Answer 4

```python
# place answer here
# use this as a template for your other answers
abbr_months = {}
for i in range(12):
   abbr_months[i+1] = (months[i].lower())[0:3]



```

-----

## 5: Min and Max
(10 Points)

- Assume that pythons built in min , max , and sort functions are broken. Write a function that receives a list then traverses the list and returns the `min` , `max`, and `average` values in a tuple.

```python
def miniStats(L):
""" 
@Description: Finds the min,max,and average values in a list
@Params: L (list)
@Returns: tuple (int,int,double)
"""
	# Start with a copy of the list so we don’t modify the original.
	L = L[:]



```

When writing your answer, include the entire function definition (without the comment block).
### Answer 5

```python
# place answer here
# use this as a template for your other answers
def miniStats(L):
   min = L[i]
   max = L[i]
   average = 0
   for i in range(len(L)):
      if(L[i] < min):
         min = L[i]
      if(L[i] > max):
         max = L[i]
      average = average + L[i]
   average = average/len(L)
   return (min,max,average)



```

-----



## 6: Prime Class


Write a class called `myPrimes` that represents a collection of your prime numbers. 
- `addPrime` : 
    - receives a prime number and adds it to your collection of primes
    - it must be checked to make sure it's prime! (should be a private method that does this).
- `removePrime`:
    - a method will remove a prime from your list
- `printPrimes`:
    - this method will print your prime numbers out 
 
### Answer 6

```python
# place answer here
# use this as a template for your other answers
class myPrimes(object):
   def __init__(self):
      primes = []
   def __addPrime(self,num):
      if(num.isPrime()):
         primes.append(num)
   def removePrime(self,num):
      if(primes.contain(num)):
         primes.remove(num)
   def printPrimes(self):
      for i in range(len(L)):
         print primes[i] + ', '


```


-----
