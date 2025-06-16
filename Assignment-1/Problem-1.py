import numpy as np
array = np.random.randint(1,51,size = (5,4))
print(array)

row_max = np.max(array, axis=1)
print(row_max)

mean = np.mean(array)
filtered = array[array <= mean]
print(filtered)

# List of elements visited along the boundary of the array in clockwise order, starting from the top-left corner.
def numpy_boundary_traversal(matrix):
    top = list(matrix[0])
    right = list(matrix[1:4, 3])
    bottom = list(matrix[4][::-1])
    left = list(matrix[1:4, 0][::-1])
    return top + right + bottom + left
print(numpy_boundary_traversal(array))