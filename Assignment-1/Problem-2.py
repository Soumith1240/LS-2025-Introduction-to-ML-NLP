import numpy as np

array = np.random.uniform(0, 10, 20)
array = np.round(array, 2)
print(array)

print("Minimum Value:", np.min(array))
print("Maximum Value:", np.max(array))
print("Median Value:", np.median(array))

modified_array = np.array([x**2 if x < 5 
                           else x 
                                for x in array])
print(modified_array)

def numpy_alternate_sort(arr):
    sorted_arr = np.sort(arr)
    result = []
    i, j = 0, len(sorted_arr) - 1
    while i <= j:
        result.append(sorted_arr[i])
        i += 1
        if i <= j:
            result.append(sorted_arr[j])
            j -= 1
    return np.array(result)

alternate_sorted_array = numpy_alternate_sort(array)
print(alternate_sorted_array)


