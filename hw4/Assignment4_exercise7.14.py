import numpy as np

array1=np.array([[0,1],[2,3]])
print(f"array1:\n {array1}")
array2=np.array([[4,5],[6,7]])
print(f"array2:\n {array2}")
array3=np.vstack((array1,array2)) # array1 will be on top of array2
print(f"array3:\n {array3}")
array4=np.hstack((array1,array2)) # array2 will be to the right of array1
print(f"array4:\n {array4}")
array5=np.vstack((array4,array4)) # vertical stacking
print(f"array5:\n {array5}")
array6=np.hstack((array3,array3)) # horizontal stacking
print(f"array6:\n {array6}")

