import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)
#create an alias by as
import numpy as np
arr = np.array([7,8,9,10,15])
print(arr)
#to check numpy version
print(np.__version__)
print(type(arr))

arr = np.array(42) #zero dimension array
arr1 = np.array([1, 2, 3, 4, 5]) #one dimension array
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) #two dimension array
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #3 dimension array
print(arr)
print(arr1)
print(arr2)
print(arr4)

#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr4.ndim)

#we can create array of required dimensions
arr3= np.array([1, 2, 3, 4], ndmin=5)
print(arr3)
print('number of dimensions :', arr.ndim)

#To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr5[0, 1, 2])

#array slicing
arr6 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr6[:4])
print(arr6[1:5:2])
arr7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]) #2D
print(arr7[1, 1:4])
print(arr7[0:2, 2])
print(arr7[0:2, 1:4]) #return 2D

#We use the array() function to create arrays,
# this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:
arr8 = np.array([1, 2, 3, 4], dtype='S')
print(arr8)
print(arr8.dtype)

#changing the datatype by coppying the array
arr9= np.array([1.1, 2.1, 3.1])
newarr = arr9.astype('i')
print(newarr)
print(newarr.dtype)

#to make a copy
arr10 = np.array([1, 2, 3, 4, 5])
x = arr10.copy()
arr10[0] = 42
print(arr10)
print(x)

#to make a view
arr11 = np.array([1, 2, 3, 4, 5])
x = arr11.view()
arr11[0] = 42
print(arr11)
print(x)
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)