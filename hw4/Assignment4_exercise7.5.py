#Python program to clarify the difference between ravel() and flatten()
import numpy as np


print('\nChecking flatten()')
a = np.array([[1, 2, 4], [8, 16, 32]])
print('Original array:\n', a)
b = a.flatten()
print()
print('Original array after making changes in flattened array:\n', a)


 
print('\n\nChecking ravel()')
x = np.array([[1, 2, 4], [8, 16, 32]])
print('Original array:\n', x)
y = x.ravel()
print()
print('Original array after making changes in flattened array:\n', x)



