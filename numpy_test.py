import numpy as np

a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

# Get Dimension
a.ndim

# Get Shape
b.shape

# Get Type
a.dtype

# Get Size
a.itemsize

# Get total size
a.nbytes


# Get number of elements
a.size


a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get a specific element [r, c]
a[1, 5]

# Get a specific row 
a[0, :]


# Get a specific column
a[:, 2]

# Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1:-1:2]


a[1,5] = 20

a[:,2] = [1,2]
print(a)

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

b[0,1,1]
print(b)

# replace 
b[:,1,:] = [[9,9,9],[8,8]]
print(b)