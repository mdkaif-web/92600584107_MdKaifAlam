#write a program to demonstrate different import mechanisms in Python
#import complete module
import math
print(math.sqrt(25))

#import specific function
from math import factorial
print(factorial(5))

#import multiple function
from math import log,factorial,sqrt
print(log(10000))
print(factorial(5))
print(sqrt(4))

#import module with an alias
import math as mt 
print(mt.log10(10000))

#import function with an alias
from math import log10 as l10
print(l10(10000))
