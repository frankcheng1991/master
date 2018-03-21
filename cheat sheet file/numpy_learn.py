# Numpy notebook

d = {}
d['fish'] = 'wet'
print d['fish']
print d.get('fish', 'N/A')
try:
	print d['monkey']
except:
	print 'error!'
print d.get('monkey', 'N/A') #  Get an element with a default; prints "N/A"

'''
Numpy
Numpy provides a high-performance multidimensional array 
	and basic tools to compute with and manipulate these arrays. 
'''

import numpy as np 

#------------------ Part 1 : Arrays ------------------------#
# full array creating method: url = https://docs.scipy.org/doc/numpy/user/basics.creation.html#arrays-creation
'''
Arrays is a grid of values of the same type.
The number of dimensions is the rank of the array.
the shape of an array is a tuple of integers giving the size of the array along each dimension
'''

'''
for arrays from lower dimensional to high dimensional : column -> row -> width -> ...
1d array: ([1, 2, 3, 4, ...]) -> 1 row n columns
2d array or matrix: ([[1, 2, 3, ...], [4, 5, 6, ...], ...]) -> n row & m columns
r2 = np.array([[1, 2, 3], [4, 5, 6]])
print r2.shape # consequence: row = 2, column = 3
3d array: ([[[1, 2, 3, ...], [4, 5, 6, ...], ...], [[7, 8, 9, ...], [10, 11, 12, ...], ...]])
r3 = np.array([[[1, 2, 3, 1], [4, 5, 6, 1], [0, 0, 0, 1]], [[7, 8, 9, 1], [10, 11, 12, 1], [0, 0, 0, 1]]])
print r3.shape # consequence: width:2 -> row: 3 -> column: 4
'''

a = np.array([1, 2, 3]) # Create a rank 1 array
print type(a)
print a.shape # the shape of an array is a tuple of integers giving the size of the array along each dimension
print [ele for ele in a]

b = np.array([[1, 2, 3], [4, 5, 6]])
print b.shape # row = 2, column = 3
print b[0, 0], b[0, 1], b[1, 0]

print np.array([[1,2.0],[0,0],(1+1j,3.)])

# Numpy also provides many functions to create arrays:
a = np.zeros((3, 2)) # create 3 rows and 2 columns
print a 
print a[2, 1] # the 0 on the last row and last column

b = np.ones((1, 2))
print b

c = np.full((2, 2), 7) # create a constant array
print c

d = np.eye(2) # create 2x2 identity matrix
print d

e = np.random.random((2, 2)) # Create an array filled with random values
print e

f = np.arange(10) # arange() will create arrays with regularly incrementing values.
print f

g = np.arange(2, 10, dtype = float)
print g

h = np.arange(2, 3, 0.1) # step is 0.1
print h

i = np.linspace(1., 4., 6) # create 6 points between 1 and 4 including 4
print i

j = np.indices((2, 4))
print j

#------------------ Part 2 : Array indexing ------------------------#
# Full indexing url: https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
# 1st way: Slicing (basic indexing) -> start:stop:step; output not include stop; when step negative, reverse
	## index for array: [0, 1, 2, 3, ..., -3, -2, -1]
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # create 3x4 matrix, 2 "[" means 2 d
b = a[:2, 1:3] # take row 0, row 1; column 1 and column2 -> 2 by 2 2d matrix
print b
print a[0, 1]

c = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print c[1:7:2] # start:stop:step
print c[-2: 10]
print c[-3: 3: -1] # reverse

d = np.array([[[1], [2], [3]], [[4], [5], [6]]])
d[1:2] # If the number of objects in the selection tuple is less than N , then : is assumed for any subsequent dimensions.
d[..., 0] # Ellipsis expand to the number of : objects needed to make a selection tuple of the same length as x.ndim. 
			#There may only be a single ellipsis present. It equals to d[:, :, 0]
d[..., 0].flatten()
d[:, np.newaxis, :, :] # Each newaxis object in the selection tuple serves to expand the dimensions of the resulting selection by one unit-length dimension. The added dimension is the position of the newaxis object in the selection tuple.

'''
Two ways of accessing the data in the middle row of the array.
Mixing integer indexing with slices yields an array of lower rank,
while using only slices yields an array of the same rank as the
original array:
'''
row_r1 = a[1, :] # Rank 1 view of the second row of a
row_r2 = a[1:2, :] # Rank 2 view of the second row of a
print row_r1, row_r1.shape
print row_r2, row_r2.shape

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print col_r1, col_r1.shape
print col_r2, col_r2.shape

# 2nd way: Integer array indexing (advanced indexing)
'''
a = np.array([
				[1,2,3],
				[4,5,6],
				[7,8,9],
				[10,11,12]
			]) # 2d array: row = 4, column = 3
basic indexing example:
a[(0, 1)] # equals to a[0, 1]
a[[0, slice(None)]]
advanced indexing example:
a[(0, 1), ]
a[[0, 1]]
'''
a = np.array([[1, 2], [3, 4], [5, 6]])
print a[[0, 1, 2], [0, 1, 0]] # The above example of integer array indexing is equivalent to this:
print np.array([a[0, 0], a[1, 1], a[2, 0]]) # this is the basic indexing
print a[[0, 1, 2], [0, 1, 0]].shape

print a[[0, 0], [1, 1]]
print np.array([a[0, 1], a[0, 1]])
		# One useful trick with integer array indexing is selecting or mutating one element from each row of a matrix:
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print a
b = np.array([0, 2, 0, 1]) # # Create an array of indices
print a[np.arange(4), b] # Select one element from each row of a using the indices in b
a[np.arange(4), b] += 10 # Mutate one element from each row of a using the indices in b
print a
		# Another example for broadcasting -> url: https://docs.scipy.org/doc/numpy/reference/ufuncs.html#ufuncs-broadcasting
a = np.array([
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[9, 10, 11]
	])
rows = np.array([0, 3], dtype = np.intp)
columns = np.array([0, 2], dtype = np.intp)
print a[rows[:, np.newaxis], columns]
print a[np.ix_(rows, columns)]

# 3rd way: Boolean array indexing:
'''
Boolean array indexing lets you pick out arbitrary elements of an array. 
Frequently this type of indexing is used to select the elements of an array that satisfy some condition. 
Here is an example:
'''
a = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = (a > 2)
'''
Find the elements of a that are bigger than 2;
this returns a numpy array of Booleans of the same
shape as a, where each slot of bool_idx tells
whether that element of a is > 2.
'''
print bool_idx
'''
We use boolean array indexing to construct a rank 1 array
consisting of the elements of a corresponding to the True values
of bool_idx
'''
print a[bool_idx] # We can do all of the above in a single concise statement:
print a[a > 2]
		# Care must only be taken to make sure that the boolean index has exactly as many dimensions as it is supposed to work with.
x = np.array([
		[0, 1],
		[1, 1],
		[2, 2]
	])
# sum(x) or x.sum() -> sum everything 
# columnsum = x.sum(axis = 0)
rowsum = x.sum(-1) # or x.sum(1)
x[rowsum <= 2, :]

rowsum = x.sum(-1, keepdims = True) # If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.
#x[rowsum <= 2]

rows = (x.sum(-1) % 2) == 0
columns = [0, 2]
#x[np.ix_(rows, columns)]

#------------------ Part 3 : Datatypes ------------------------#
# full data types introduction: https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html

x = np.array([1, 2], dtype = np.int64)

#------------------ Part 4 : Array math ------------------------#
## full math functions: url = https://docs.scipy.org/doc/numpy/reference/routines.math.html
## Here are other array mulnipulation: url = https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html
x = np.array([[1, 2], [3, 4]], dtype = np.float64) # 2d matrix
y = np.array([[5, 6], [7, 8]], dtype = np.float64) # 2d matrix

v = np.array([9, 10]) # 1d array
w = np.array([11, 12]) # 2d array
## +
print x + y
print np.add(x, y)
## -
print x - y
print np.subtract(x, y)
## * : not matrix maltiplication, just elementwise product:
print x * y
print np.multiply(x, y)
## /:
print x / y
print np.divide(x, y)
## root square:
print x ** 0.5
print np.sqrt(x)
## use 'dot' to compute the inner product of vectors
print x.dot(y) # alternative way below:
print np.dot(x, y)
print v.dot(w) # for vectors to compute inner product; while v*w compute elementwise product
print np.dot(v, x)
## sum
print x.shape # (row, column)
print np.sum(x) # sum of all element
print np.sum(x, axis = 0) # sum of each column
print np.sum(x, axis = 1) # sum of each row
## use 'T' to transpose 
print x.T
print v.T # Note that taking the transpose of a rank 1 array does nothing, convert it to rank 2 first:
v2 = v[np.newaxis, :]
print v2.T

#------------------ Part 5 : Broadcasting ------------------------#
## URl = https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html
## add the vector v to each row of the matrix x:
x = np.arange(1, 13).reshape(4,3)
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1)) # Stack 4 copies of v on top of each other
print vv
y = x + vv
print y
## numpy broadcasting allow us to perform this computation without actually creating multiple copies of v. Consider this version, using broadcasting:
y = x + v # Add v to each row of x using broadcasting
print y
'''
Explanation:
The line y = x + v works even though x has shape (4, 3) and v has shape (3,) 
due to broadcasting; this line works as if v actually had shape (4, 3), 
where each row was a copy of v, and the sum was performed elementwise.
Broadcasting two arrays together follows these rules:

1. If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.
2. The two arrays are said to be compatible in a dimension if they have the same size in the dimension, or if one of the arrays has size 1 in that dimension.
3. The arrays can be broadcast together if they are compatible in all dimensions.
4. After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.
5. In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension
'''
## in broadcasting, shape(3, ) equals to shape(1, 3); stretching must be from 1 -> n