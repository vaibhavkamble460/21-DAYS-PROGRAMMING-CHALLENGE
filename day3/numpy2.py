import numpy as np
#shape of an array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
#shape of an array who"s dimensions are given by user
arr2 = np.array([1, 2, 3, 4], ndmin=5)
print(arr2)
print('shape of array :', arr2.shape)
#reshaping 1D to 2D
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr3.reshape(4, 3)#The outermost dimension will have 4 arrays, each with 3 elements
print(newarr)
#reashaping 1D to 3D
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr4.reshape(2, 3, 2)
print(newarr1)
#checking that after reshaping it is view or copy
arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr5.reshape(2, 4).base) #it is a view
#Flattening array means converting a multidimensional array into a 1D array.
arr6 = np.array([[1, 2, 3], [4, 5, 6]])
newarr2 = arr6.reshape(-1)
print(newarr2)
#iterating through 1d array
arr7 = np.array([1, 2, 3])
for x in arr7:
  print(x)
#iterating through 2d array
arr8 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr8:
  print(x)
#Iterate on each scalar element of the 2-D array:
arr9 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr9:
  for y in x:
    print(y)
#iterating through 3d array
arr10 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr10:
  print(x)
#funtion neditor to iterate through aaray
arr11 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr11):
  print(x)
#ietrating through different data type
arr12 = np.array([1, 2, 3])
for x in np.nditer(arr12, flags=['buffered'], op_dtypes=['S']):
  print(x)
#
arr13 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)