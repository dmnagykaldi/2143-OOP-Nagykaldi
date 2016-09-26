#Domonkos Nagykaldi fraction_class.py

class fraction(object):
    def __init__(self,w=0,n=None,d=None):
        self.whole = w
        self.numerator = n
        self.denominator = d
    
    def simplify(self):
    	if(self.numerator >= self.denominator):
    		self.whole = (self.numerator / self.denominator)
    		self.numerator = (self.numerator % self.denominator)

    def __str__(self):
    	if(self.whole > 0):
        	return "%d  %d / %d" % (self.whole , self.numerator , self.denominator)
    	else:
    		return "%d / %d" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        f1 = fraction(0,x,y)
        f1.simplify
        return f1

    def __add__(self,rhs):
    	x = (self.numerator * rhs.denominator) + (rhs.numerator * self.denominator)
    	y = (self.denominator * rhs.denominator)
    	f1 = fraction(0,x,y)
    	f1.simplify
    	return f1
        
if __name__ == '__main__':
    a = fraction(0,1,2)
    b = fraction(0,4,5)
    c = a + b
    print(c)