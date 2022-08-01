#array initialisation
array1 = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
array2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

#traversing the array and multiplying each element and storing the result in the array1 
for i in range(3):
    for j in range(3):
        array1[i][j] = array1[i][j] * array2[i][j]

print(array1)
