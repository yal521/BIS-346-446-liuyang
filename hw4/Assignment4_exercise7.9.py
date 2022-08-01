import numpy as np

#array having elements from 1 to 15
lst = np.arange(1,16)
print(lst)

#reshape array into 3x5 array
lst1 = np.reshape(lst,(3,5))
print(lst1)

#select row 2
print("\nrow 2: ", end='')
print(lst1[2])

#select column 5
print("\ncolumn 5: ", end='')
print(lst1[:,4])

#select rows 0 and 1
print("\nrows 0 and 1: ", end='')
print(lst1[:,0:2])

#select columns 2 - 4
print("\ncolumn 2 - 4: ", end='')
print(lst1[:,2:5])

#select columns in row 1 and column 4
print("\nrow1column4: ", end='')
print(lst1[1,4])


#select element in rows 1 and 2 that are in columns 0, 2 and 4
print("\nElement at row 1 and 2 that are in column 0,2,4: ", end='')
print(lst1[1:3, [0,2,4]])


