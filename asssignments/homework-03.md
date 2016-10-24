# OOP Repeat

### Defining a Class

When defining a class, we use the following syntax :

```python 
class OurClass(ParentClass):
"""Definition of class here (methods and class variables)."""



```

Where `OurClass` is the name of the new class and `ParentClass` is the name of the class it inherits from.

If were not going to inherit from one of our class definitions, the we replace `ParentClass` with `object`.

-----

### Defining a Method
To define a method, we write it almost exactly the same way as when we define functions but the first argument we always include is self, which we use to refer to the instance we used to call the method.

```python
class OurClass(ParentClass):
    def class_method(self, arg):
        # body goes here




```

-----


### Using a Class or Its Attributes
Finally, to use a class or instance’s attributes, we use ”dot notation”, which is aptly named for the use of the magic dot. The dot asks the class for the value of the attribute. So, if we have a method or variable, `bar`, of a class or instance, `foo`, we access it by saying:
”foo.bar” which says ”Almighty foo class, what is the value of the attribute bar?”

Typically, attributes are defined in the `__init__` function of a class:

```python
class OurClass(ParentClass):
    bar = "Fruit Bar" # class attribute

    def __init__(self, bar_name):
        self.bar = bar_name # instance attribute

    def method(self, arg):
        # body goes here
```

Once an object is constructed, you can also access the attribute by using dot notation outside of the class definition:

```python
new_bar = OurClass(’Crazy Bar’)
print(new_bar.bar)

# prints:
’Crazy Bar’


```

### Class vs. Object

When discussing objects and classes, it is helpful to distinguish between the definition of a class and the instance of a class (an object).

- The `instance` is referred to as an “object”, 
- The `definition` is the actual “class”. 
- Using the previous example: We used the definition `OurClass` to create an instance called `new_bar`. Now that `new_bar` exists, it is an `object` !


## Skittles Example

```python

As a starting example, consider the classes `Skittle` and `Bag`, which will be used to represent a single piece of Skittles candy and a bag of Skittles respectively.

class Skittle(object):
    """A Skittle object has a color to describe it."""
    def __init__(self, color):
        self.color = color

class Bag(object):
    """A Bag is a collection of Skittles. All bags share the
    number of Bags ever made (sold) and each bag keeps track of
    its Skittles in a list.
    """

    number_sold = 0

    def __init__(self):
        self.skittles = []
        Bag.number_sold += 1

    def tag_line(self):
        """Print the Skittles tag line."""
        print("Taste the rainbow!")

    def print_bag(self):
        print([s.color for s in self.skittles])

    def take_skittle(self):
        """Take the first skittle in the bag (from the front of
        the skittles list).
        """
        return self.skittles.pop(0)

    def add_skittle(self, s):
        """Add a skittle to the bag."""
        self.skittles.append(s)

```

- In this example, we have the attribute `number_sold`, which is a `class attribute`. 
- Also we have the method called `__init__` . That is called when you make a new instance of the class (constructor). 
- So, if you `write a = Bag()`, that makes a new `instance` of the Bag class (calling init to do so) and then returns self, which you can think of as a dictionary that holds all of the attributes of the object.
- To make a new `class attribute`, you use the name of the class with dot notation: `Bag.new_var = 10` makes a new class attribute `new_var` in the Bag class and assigns it the value of 10. 
- To make a new instance attribute, you use the name of the instance attribute: `a.new_var2 = 10`. 

### Questions

**1)** What does Python print for each of the following:

```python 
johns_bag = Bag()
johns_bag.print_bag()
# what prints?

for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# what prints?

s = johns_bag.take_skittle()
print(s.color)
# what prints?

print(johns_bag.number_sold)
# what prints?

print(Bag.number_sold)
# what prints?

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# what prints?

print(Bag.number_sold)
# what prints?

print(soumyas_bag.number_sold)
# what prints?
```

### Answer 1

```python
# answers here

```

**2)**  Write a new method for the Bag class called take color, which takes a color and
removes (and returns) a Skittle of that color from the bag. If there is no Skittle
of that color, then it returns `None`.

```python
def take_color(self, color):






```


### Answer 2

```python
# answer here

```

**3.** Write a new method for the Bag class called take all, which takes all the Skittles
in the current bag and prints the color of the each Skittle taken from the bag.

```python
def take_all(self):




```

### Answer 3

```python
# answer here

```
