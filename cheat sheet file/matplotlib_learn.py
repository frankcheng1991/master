
# Matplotlib is a plotting library. In this section give a brief introduction to the matplotlib.pyplot module, which provides a plotting system similar to that of MATLAB.
'''
url = http://cs231n.github.io/python-numpy-tutorial/#numpy
url_full = https://matplotlib.org/
'''

import matplotlib as mpl 
#import matplotlib.pyplot as plt 

#%matplotlib inline

#------------------ Part 1 : Plotting ------------------------#
## The most important function in matplotlib is plot, which allows you to plot 2D data.
## url = https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
import numpy as np 
import matplotlib.pyplot as plt 
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)

y = np.sin(x)
print y
# Plot the points using matplotlib
plt.plot(x, y)
plt.show() # You must call plt.show() to make graphics appear.

## With just a little bit of extra work we can easily plot multiple lines at once, and add a title, legend, and axis labels:
y_sin = np.sin(x)
y_cos = np.cos(x)
# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()

#------------------ Part 2 : Subplots ------------------------#
## You can plot different things in the same figure using the subplot function.
## url = https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot
## subplot(nrows, ncols, plot_number)
x = np.arange(0, 3 * np.pi, 0.1) # rank 1 array: shape(n,)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up a subplot grid that has height 2 and width 1, and set the first such subplot as active.
plt.subplot(2, 1, 1)
# Make the first plot:
plt.plot(x, y_sin)
plt.title('Sine')
# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

plt.show()

#------------------ Part 3 : Images ------------------------#
## You can use the imshow function to show images.
from scipy.misc import imread, imresize
img = imread('cat.jpg')
img_tinted = img * [1, 0.95, 0.9]
print img_tinted.dtype # float64
# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
'''
# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
'''
plt.imshow(np.uint8(img_tinted))

plt.show()