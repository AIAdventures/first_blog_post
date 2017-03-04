# What version of Python do you have?

import sys
import tensorflow as tf
import sklearn as sk
import numpy as np
import pandas as pd

print("Python {}".format(sys.version))
print('TensorFlow {}'.format(tf.__version__))
print('Pandas {}'.format(pd.__version__))
print('Scikit-Learn {}'.format(sk.__version__))

for x in range(1,10):
	print(x)

sum = 0 
for x in range(1, 10): #for loops must end with a semicolon
	sum += x
	print("adding {} gives {}".format(x, sum))
print("the total sum is {}".format(sum))

#now to look at lists and sets, the python data structures are amazingly flexible!
#think of python, in numerical computing as a supercharged calculator

c= ['a', 'b', 'c']
print(c)
#dont need to define counting variable, interate over the collection
for x in c: 
	print(x)

#now to look at sets, sets do not allow duplicates. when adding input sets add.
c = set()
c.add('a')
c.add('b')

print(c)

'''we should get into matricies and this is were most of computation is going to happen
lets start with looking at numpy arrays'''

#lets create some sample arrays

p = np.zeros(10, dtype = int) #dtype is force the type of value that is held in the array
print(p) 

q = np.ones((3,5), dtype = float)
print(q)

#force the the value in each maxtrix place

z = np.full((5,5), 2)

print(z)

'''ok, lets try something more interesting. a 5,5 matrix of normally distributed variables.
with mean zero standard deviation of 1
'''
mnd = np.random.normal(0, 1, (5,5))

print(mnd)

''' and for completeness and list of numpy standard data types which will end this start of python.


Data type	Description
bool_	Boolean (True or False) stored as a byte
int_	Default integer type (same as C long; normally either int64 or int32)
intc	Identical to C int (normally int32 or int64)
intp	Integer used for indexing (same as C ssize_t; normally either int32 or int64)
int8	Byte (-128 to 127)
int16	Integer (-32768 to 32767)
int32	Integer (-2147483648 to 2147483647)
int64	Integer (-9223372036854775808 to 9223372036854775807)
uint8	Unsigned integer (0 to 255)
uint16	Unsigned integer (0 to 65535)
uint32	Unsigned integer (0 to 4294967295)
uint64	Unsigned integer (0 to 18446744073709551615)
float_	Shorthand for float64.
float16	Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
float32	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
float64	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
complex_	Shorthand for complex128.
complex64	Complex number, represented by two 32-bit floats
complex128	Complex number, represented by two 64-bit floats

'''




























