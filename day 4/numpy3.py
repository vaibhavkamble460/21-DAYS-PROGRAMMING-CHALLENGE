#joining of two 1D array
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
#joining of two 2D array among rows
import numpy as np
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr_y = np.concatenate((arr3, arr4), axis=1)
print(arr_y)
#joining of two 2D array using stack function
arr5 = np.array([1, 2, 3])
arr6 = np.array([4, 5, 6])
arr_f = np.stack((arr1, arr2), axis=1)
print(arr_f)
#stacking along rows
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)
#stacking along column
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)
#stacking along height
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)
#splitting array
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3) #makes 3 division ao array
print(newarr)
#accessing splitted array by index
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])
#spliiting of 2D array
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
#The example below also returns three 2-D arrays, but they are split along the row (axis=1).
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
#searching array
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
#search sorted
#There is a method called searchsorted() which performs a binary search in the array, and returns
# the index where the specified value would be inserted to maintain the search order.
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
#to search more than one value
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
#sorting array
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
#sorting array alphabetically
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
#sorting 2D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
#filtering array
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
#directly filtering

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
#adding of two list
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)