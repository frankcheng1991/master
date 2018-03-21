# Scipy_learn

'''
Numpy provides a high-performance multidimensional array and basic tools to compute with and manipulate these arrays. 
SciPy builds on this, and provides a large number of functions that operate on numpy arrays and are useful for different types of scientific and engineering applications.
url_short = http://cs231n.github.io/python-numpy-tutorial/#numpy
Url_full = https://docs.scipy.org/doc/scipy/reference/index.html
'''

import numpy as np

#------------------ Part 1 : Image operations ------------------------#
## functions to read images from disk into numpy arrays, to write numpy arrays to disk as images, and to resize images
from scipy.misc import imread, imsave, imresize
img = imread('cat.jpg')
print img.dtype, img.shape
'''
# We can tint the image by scaling each of the color channels
# by a different scalar constant. The image has shape (400, 248, 3);
# we multiply it by the array [1, 0.95, 0.9] of shape (3,);
# numpy broadcasting means that this leaves the red channel unchanged,
# and multiplies the green and blue channels by 0.95 and 0.9
# respectively.
'''
img_tinted = img * [1, 0.95, 0.9]

# Resize the tinted image to be 300 by 300 pixels.
img_tinted = imresize(img_tinted, (300, 300))

# Write the tinted image back to disk
imsave('cat_tinted.jpg', img_tinted)

#------------------ Part 2 : MATLAB files ------------------------#
## The functions scipy.io.loadmat and scipy.io.savemat allow you to read and write MATLAB files.

#------------------ Part 3 : Distance between points ------------------------#
## The function scipy.spatial.distance.pdist computes the distance between all pairs of points in a given set:
from scipy.spatial.distance import pdist, squareform
## Create the following array where each row is a point in 2D space:
x = np.array([
		[0, 1],
		[1, 0],
		[2, 0]
	])
'''
# Compute the Euclidean distance between all rows of x.
# d[i, j] is the Euclidean distance between x[i, :] and x[j, :],
# and d is the following array:
'''
d = squareform(pdist(x, 'euclidean'))
print d
print pdist(x, 'euclidean')

## A similar function (scipy.spatial.distance.cdist) computes the distance between all pairs across two sets of points;


